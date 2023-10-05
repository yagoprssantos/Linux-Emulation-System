import prettytable
import sqlite3

# Conecte-se ao banco de dados SQLite
db = sqlite3.connect("sistema_mensagens.db")
cursor = db.cursor()
update = db.cursor()

# Função para criar tabela de mensagens se ela não existir
def criar_tabela_mensagens():
    cursor.execute('''CREATE TABLE IF NOT EXISTS mensagens (
                    id INTEGER PRIMARY KEY,
                    remetente TEXT NOT NULL,
                    destinatario TEXT,
                    mensagem TEXT,
                    prioridade INTEGER DEFAULT 0,
                    grupo TEXT,
                    visualizado boolean,
                    data_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )''')
    db.commit()

# Chame a função para criar a tabela de mensagens
criar_tabela_mensagens()

# Função para enviar uma mensagem
def enviar_mensagem(remetente, destinatarios, mensagem, prioridade=0, grupo=None):
    if destinatarios:
        for destinatario in destinatarios:
            cursor.execute("INSERT INTO mensagens (remetente, destinatario, mensagem, prioridade, grupo, visualizado) VALUES (?, ?, ?, ?, ?, ?)",
                           (remetente, destinatario, mensagem, prioridade, grupo, 0))
    elif grupo:
        cursor.execute("INSERT INTO mensagens (remetente, destinatario, mensagem, prioridade, grupo, visualizado) VALUES (?, ?, ?, ?, ?, ?)",
                       (remetente, None, mensagem, prioridade, grupo, 0))
    db.commit()

# Função para listar mensagens de um remetente
def listar_mensagens_remetente(remetente):
    update.execute("UPDATE mensagens set visualizado = 1 WHERE remetente = ?", [remetente])
    cursor.execute("SELECT destinatario, mensagem, prioridade, grupo, visualizado FROM mensagens WHERE remetente = ? ORDER BY prioridade DESC", (remetente,))
    mensagens = cursor.fetchall()
    return mensagens

# Função para listar mensagens de um destinatário
def listar_mensagens_destinatario(destinatario):
    update.execute("UPDATE mensagens set visualizado = 1 WHERE destinatario = ?", [destinatario])
    cursor.execute("SELECT remetente, mensagem, prioridade, grupo, visualizado FROM mensagens WHERE destinatario = ? ORDER BY prioridade DESC", (destinatario,))
    mensagens = cursor.fetchall()
    return mensagens

# Função para listar mensagens de um grupo
def listar_mensagens_grupo(grupo):
    update.execute("UPDATE mensagens set visualizado = 1 WHERE grupo = ?", [grupo])
    cursor.execute("SELECT remetente, mensagem, destinatario, prioridade, visualizado FROM mensagens WHERE grupo = ? ORDER BY prioridade DESC", (grupo,))
    mensagens = cursor.fetchall()
    return mensagens

def verifica_mensagens__nao_lidas ():
    cursor.execute("SELECT visualizado from mensagens WHERE visualizado = 0")
    mensagem = cursor.fetchone()
    if mensagem == None:
        return False
    else:
        return True

# Exemplo de uso
if __name__ == "__main__":
    while True:
        print("\n1. Enviar Mensagem")
        print("2. Listar Mensagens do Remetente/Destinatário")
        print("3. Listar todas as mensagens do banco")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            if (verifica_mensagens__nao_lidas()):
              print('Existem mensagens que ainda não foram lidas, por favor verifica as mensagens que foram enviadas antes de gerar novas mensagens')
              continue

            remetente = input("\nRemetente: ")
            destinatarios = input("Destinatario (deixe em branco se for uma mensagem de grupo): ").split(',')
            mensagem = input("Mensagem: ")
            prioridade = int(input("Prioridade (0 para padrão, 1 para média e 2 para alta): "))
            grupo = input("Grupo (deixe em branco se NÃO for uma mensagem de grupo): ")

            if grupo:
                enviar_mensagem(remetente, None, mensagem, prioridade, grupo)
                print(f"\nMensagem enviada com sucesso para o grupo {grupo}!")
            else:
                enviar_mensagem(remetente, destinatarios, mensagem, prioridade)
                print("\nMensagem enviada com sucesso!")



        if escolha == "2":
            print(f"\n'R' para consultar remetente"
                  f"\n'D' para consultar destinatário"
                  f"\n'G' para consultar grupo")
            opcao = input("Escolha uma opção: ").upper()

            if opcao == 'R':
                remetente = input("Remetente: ")
                mensagens = listar_mensagens_remetente(remetente)
                if mensagens:
                    print("Mensagens de", remetente)

                    # Crie uma tabela bonita
                    table = prettytable.PrettyTable(["Destinatario", "Mensagem", "Prioridade", "Grupo", 'visualizado'])

                    for mensagem in mensagens:
                        destinatario, mensagem, prioridade, grupo, visualizado = mensagem
                        table.add_row([destinatario, mensagem, prioridade, grupo, visualizado])

                    # Imprima a tabela
                    print(table)
                else:
                    print("Nenhuma mensagem encontrada de", remetente)

            elif opcao == 'D':
                destinatario = input("\nDestinatario: ")
                mensagens = listar_mensagens_destinatario(destinatario)
                if mensagens:
                    print("\nMensagens para", destinatario, "\n")

                    # Crie uma tabela bonita
                    table = prettytable.PrettyTable(["Remetente", "Mensagem", "Prioridade", "Grupo", 'visualizado'])

                    for mensagem in mensagens:
                        remetente, mensagem, prioridade, grupo, visualizado = mensagem
                        table.add_row([remetente, mensagem, prioridade, grupo, visualizado])

                    # Imprima a tabela
                    print(table)
                else:
                    print("\nNenhuma mensagem encontrada para", destinatario)

            elif opcao == 'G':
                grupo = input("\nGrupo: ")
                mensagens = listar_mensagens_grupo(grupo)
                if mensagens:
                    print(f"\nMensagens para o grupo {grupo}\n")

                    # Crie uma tabela bonita
                    table = prettytable.PrettyTable(["Remetente", "Mensagem", "Prioridade", "Destinatario", 'visualizado'])

                    for mensagem in mensagens:
                        remetente, mensagem, destinatario, prioridade, visualizado = mensagem
                        table.add_row([remetente, mensagem, prioridade, destinatario, visualizado])

                    # Imprima a tabela
                    print(table)
                else:
                    print(f"\nNenhuma mensagem encontrada para o grupo {grupo}")

            else:
                print("Selecione uma opção válida!")

        elif escolha == "3":
          # Listar todas as mensagens ordenadas por prioridade, incluindo a data
          cursor.execute("UPDATE mensagens set visualizado = 1 WHERE visualizado = 0")
          cursor.execute("SELECT remetente, destinatario, mensagem, prioridade, grupo, visualizado, data_envio FROM mensagens ORDER BY prioridade DESC")
          mensagens = cursor.fetchall()
          if mensagens:
              print(f"\nTodas as Mensagens Ordenadas por Prioridade\n")

              # Crie uma tabela bonita
              table = prettytable.PrettyTable(["Remetente", "Destinatario", "Mensagem", "Prioridade", "Grupo", "visualizado", "Data Envio"])

              for mensagem in mensagens:
                  remetente, destinatario, mensagem, prioridade, grupo, visualizado, data_envio = mensagem
                  table.add_row([remetente, destinatario, mensagem, prioridade, grupo, visualizado, data_envio])

              # Imprima a tabela
              print(table)
          else:
              print("\nNenhuma mensagem encontrada no banco de dados")

        elif escolha == "4":
          break
# Feche a conexão com o banco de dados SQLite quando terminar
cursor.close()
update.close()
db.close()

# Simulador do Sistema Operacional Linux

![Banner](banner.png)

---

## Tabela de Conteúdos

- [Descrição](#descrição)
- [Instalação](#instalação)
- [Uso](#uso)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuindo](#contribuindo)


## Descrição

O Simulador do Sistema Operacional Linux é uma ferramenta educacional abrangente que simula um ambiente Linux simplificado. Ele fornece aos usuários uma experiência prática em trabalhar com componentes de hardware, software e rede em um ambiente simulado e controlado.

Se você é um aspirante a administrador de sistemas, desenvolvedor ou simplesmente curioso sobre como o Linux funciona, este simulador oferece uma maneira segura de explorar e experimentar vários aspectos de um sistema Linux.


## Instalação

Para instalar o simulador, você precisa ter o Python 3 instalado em seu sistema. Você pode baixar o Python no site oficial: https://www.python.org/downloads/

Depois de ter o Python instalado, você pode baixar o código-fonte do simulador do repositório do GitHub:

`git clone https://github.com/yagoprssantos/Linux-System-Simulator.git`


## Uso

Para executar o simulador, navegue até o diretório onde você baixou o código-fonte e execute o seguinte comando: 

`python main.py`

Isso iniciará o simulador e exibirá o menu principal. A partir do menu principal, você pode escolher visualizar informações sobre o hardware, o servidor, a arquitetura de software ou os aplicativos instalados. Você também pode configurar os aplicativos instalados, instalando, desinstalando, iniciando, parando ou gerenciando permissões para eles.


## Funcionalidades

- **Simulação de Hardware**: Experimente as funcionalidades de uma máquina virtual com componentes como CPU, memória e armazenamento.

- **Componentes de Software**: Interaja com um sistema operacional semelhante ao Linux, incluindo kernel e arquitetura de software.

- **Gerenciamento de Pacotes**: Simule um sistema de repositório de software com a capacidade de instalar e desinstalar pacotes.

- **Interface Amigável**: Utilize uma interface intuitiva baseada em menus que torna o sistema acessível a usuários de todos os níveis.


## Estrutura do Projeto

- **main.py**: O ponto de entrada principal para iniciar o simulador do sistema operacional.

- **loading.py**: Módulo contendo funções para animações de carregamento.

- **menus.py**: Definição de vários menus para interação do usuário.

- **machine.py**: Implementação da classe `Machine`, que representa o hardware virtual.

- **linuxOS.py**: Sistema operacional Linux simulado com funções relevantes.

- **kernel.py**: Define a `LinuxKernelAPI` para interações do kernel.

- **appInterface.py**: Fornece uma simulação da interface e gerenciamento de aplicativos.

- **package.py**: Define a classe `Package` para pacotes de software no sistema.

- **refresh.py**: Funcionalidade de limpeza do console fornecida pela classe `Refresh`.

- **server.py**: Representa um servidor para simulações de rede.


## Contribuindo

Se você deseja contribuir para o projeto, faça um fork do repositório e crie uma solicitação de pull. Certifique-se de seguir as convenções de codificação usadas no projeto e escrever testes para qualquer nova funcionalidade.


---

**Aproveite sua jornada de simulação do Linux!**

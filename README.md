# Estrutura de Dados

## Salles Hair

### 1.0 Salles Hair

A **Salles Hair** é uma boutique especializada em acessórios para cabelo, oferecendo uma variedade encantadora de produtos, desde piranhas, presilhas e xuxinhas até uma ampla gama de novidades. Atualmente, a loja expandiu seu catálogo para incluir não apenas os encantadores acessórios, mas também uma seleção de produtos essenciais para cuidados capilares, como gel para pentear, kits de shampoo e cremes para hidratação.

### 2.0 Problema

**Problema 02: Estruturas de dados aplicadas a problemas reais.**

**Sistema escolhido:** Sistema de controle de estoque.

**Descrição:** Desenvolva um sistema de controle de estoque para uma loja, utilizando Python e estruturas de dados que julgue adequadas. O sistema deve possuir, no mínimo, funcionalidades de cadastro de produtos, atualização de estoque, vendas, relatórios de vendas e controle de validade para produtos perecíveis.

### 4.0 Justificativa da estrutura escolhida

A estrutura de dados escolhida como principal foi a lista, pois ela permite uma flexibilidade maior para o CRUD do estoque e para o armazenamento de outros elementos, como o histórico.

### 5.0 Desenvolvimento

O sistema foi desenvolvido a partir de seis classes: `System`, `Menu`, `Stock`, `Report`, `Product` e `Sale`. Estas estão divididas em classes de controle, que estão dentro do arquivo `main.py`, e as de objetos em si, os quais armazenam os dados. A classe `System` é responsável por manter o programa funcionando ao gerenciar os laços de repetição que permitem o funcionamento do sistema e também de criar um estoque fictício para a execução do programa. A classe de menu gerencia as entradas e saídas do usuário e as classes de `Stock`, `Sale`, `Report` e `Product` são utilizadas para organizar as informações. A classe `System` possui um objeto de `Stock`. Este contém objetos de `Product` armazenados em uma lista e métodos que permitem seus respectivos gerenciamentos.

### 6.0 Como Rodar a Aplicação

Para executar a aplicação **Salles Hair**, siga os passos abaixo:

1. **Verifique se o Python está instalado:** Antes de tudo, verifique se você tem o Python instalado em sua máquina. Você pode fazer isso abrindo o terminal (no Windows, o Prompt de Comando ou PowerShell) e digitando o seguinte comando:

    ```bash
    python --version
    ```

    Se o Python estiver instalado, você verá a versão instalada. Caso contrário, você precisará instalar o Python. Você pode baixar o instalador mais recente do Python em [python.org](https://www.python.org/downloads/).

2. **Baixe o código-fonte:** Baixe ou clone o repositório contendo o código-fonte do projeto **Salles Hair** em sua máquina local.

3. **Navegue até o diretório do projeto:** Abra o terminal e navegue até o diretório onde você baixou ou clonou o código-fonte do projeto.

4. **Execute o arquivo `main.py`:** No terminal, execute o seguinte comando para executar o arquivo principal do projeto:

    ```bash
    python main.py
    ```

5. **Interaja com o sistema:** Após executar o comando acima, você será apresentado ao menu principal do sistema **Salles Hair**. A partir daqui, você pode interagir com o sistema utilizando as opções fornecidas pelo menu.

6. **Explore as funcionalidades:** Explore as diversas funcionalidades do sistema, como cadastro de produtos, atualização de estoque, vendas, geração de relatórios e controle de validade para produtos perecíveis.

7. **Encerrando a aplicação:** Para encerrar a aplicação, utilize a opção correspondente no menu ou simplesmente feche a janela do terminal.

Siga esses passos e você será capaz de executar e explorar todas as funcionalidades da aplicação **Salles Hair** em sua máquina local.

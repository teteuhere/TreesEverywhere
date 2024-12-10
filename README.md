# Trees Everywhere

## Descrição

Este projeto, chamado "Trees Everywhere", foi desenvolvido como um teste de admissão para a Youshop em 2024. O objetivo é construir um sistema para gerenciar um banco de dados de árvores plantadas por voluntários globalmente.

O sistema permite que os usuários se registrem, façam login e adicionem informações sobre as árvores que plantaram, incluindo a espécie, local e data de plantio. Além disso, o sistema fornece uma interface administrativa para gerenciar usuários, contas e árvores, e uma API REST para acessar os dados das árvores.

## Modelo de Dados

O modelo de dados do projeto consiste nas seguintes entidades:

*   **Conta:** Armazena informações sobre uma conta, que pode ter vários usuários.
    *   `name`: Nome da conta.
    *   `is_active`: Indica se a conta está ativa ou inativa.
*   **Usuário:** Representa um usuário do sistema, que pertence a uma conta.
    *   `username`: Nome de usuário único.
    *   `password`: Senha do usuário.
    *   `account`: Conta à qual o usuário pertence.
    *   `is_active`: Indica se o usuário está ativo ou inativo.
*   **Perfil:** Armazena informações adicionais do usuário.
    *   `user`: Usuário associado ao perfil.
    *   `about`: Breve descrição do usuário.
    *   `joined`: Data em que o usuário se juntou à plataforma.
*   **Árvore:** Representa uma espécie de árvore.
    *   `common_name`: Nome comum da árvore.
    *   `scientific_name`: Nome científico da árvore.
*   **ÁrvorePlantada:** Representa uma árvore plantada por um usuário.
    *   `tree`: Espécie da árvore plantada.
    *   `planted_by`: Usuário que plantou a árvore.
    *   `planted_at`: Data e hora do plantio.
    *   `latitude`: Latitude do local de plantio.
    *   `longitude`: Longitude do local de plantio.

## Funcionalidades

### Interface Administrativa

*   Gerenciar contas (criar, listar, ativar/desativar).
*   Gerenciar usuários (criar, listar, visualizar detalhes).
*   Gerenciar perfis de usuário (visualizar).
*   Gerenciar árvores (criar, listar, visualizar detalhes).
*   Gerenciar árvores plantadas (listar, visualizar detalhes).

### Interface do Usuário

*   Registrar-se na plataforma.
*   Fazer login na plataforma.
*   Visualizar árvores plantadas por usuários da mesma conta.
*   Adicionar novas árvores plantadas.

### API REST

*   Criar, listar, recuperar, atualizar e excluir contas.
*   Criar, listar, recuperar, atualizar e excluir árvores.
*   Registrar novas árvores plantadas.
*   Listar e recuperar árvores plantadas.

## Tecnologias Utilizadas

*   Python
*   Django
*   Django REST Framework
*   HTML
*   CSS
*   JavaScript

## Instalação

1.  Clone o repositório: `git clone https://github.com/seu-usuario/trees-everywhere.git`
2.  Crie um ambiente virtual: `python3 -m venv .venv`
3.  Ative o ambiente virtual: `source .venv/bin/activate`
4.  Instale as dependências: `pip install -r requirements.txt`
5.  Configure o banco de dados: `python manage.py migrate`
6.  Crie um superusuário: `python manage.py createsuperuser`
7.  Inicie o servidor: `python manage.py runserver`

## Testes

Execute os testes com o comando: `python manage.py test`

## Contribuição

Contribuições são bem-vindas!

## Licença

MIT License

## Autor

[Matheus S.]

## Agradecimentos

Syngred.

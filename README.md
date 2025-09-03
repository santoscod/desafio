Desafio Técnico: Catálogo de Países e Agência de Viagens.

funcionalidade:

CRUD de Roteiros: permite o cadastro de roteiros de viagem personalizados através do painel de administração do Django.

busca: Funcionalidade de busca por nome na lista de países.
Containerização: A aplicação e seu banco de dados (PostgreSQL) são totalmente gerenciados via Docker e Docker Compose.

visualização pública: qualquer visitante pode navegar pela lista de países, ver detalhes de um país específico e os roteiros de viagem associados a ele mesmo.

sincroniza dados de mais de 250 países a partir da API pública [REST Countries](https://restcountries.com/).(API está no sync_countries.py)

tecnologias utilizadas

Back-end: Python 3.11, Django 5+
Banco de Dados: PostgreSQL 14
containerização: Docker, Docker Compose
Front-end: HTML (com Django Templates)

como Executar o Projeto

pré-requisitos:
Docker, Docker Compose

passos:

clone o repositório:
    bash
    git clone [URL_DO_SEU_REPOSITORIO_GIT]
    cd [NOME_DA_PASTA]
    

inicie a aplicação com Docker Compose:
    O comando a seguir irá construir a imagem do Django, baixar a imagem do PostgreSQL e iniciar os contêineres.
    bash
    sudo docker-compose up --build
    
    

prepare o banco de dados (em um segundo terminal):
    abre um novo terminal, vai navegando até a pasta do projeto e execute os seguintes comandos para criar as tabelas, o superusuário e popular o banco com os países:
    bash
    sudo docker-compose exec web python3 manage.py migrate
    sudo docker-compose exec web python3 manage.py createsuperuser
    sudo docker-compose exec web python3 manage.py sync_countries
    criei aqui e funcionou: 
    login:higor
    senha:ch466717

acesse abaixo a aplicação:
Site Principal: [http://localhost:8000/countries/](http://localhost:8000/countries/)

painel de administração: [http://localhost:8000/admin/](http://localhost:8000/admin/)

para abrir o itineraries: http://localhost:8000/itineraries/
    
🌿 Catálogo de Plantas Medicinais — API REST (Django + DRF)

API desenvolvida para catalogar espécies vegetais medicinais, seus usos tradicionais, regiões de ocorrência e referências científicas.
Este projeto foi criado como Projeto Integrador, baseado na estrutura do professor, porém totalmente remodelado para o tema Plantas Medicinais do Cerrado e Outros Biomas Brasileiros.

A API oferece:

• Cadastro de plantas, incluindo imagem

• Cadastro de usos medicinais

• Cadastro de regiões e biomas onde ocorrem

• Cadastro de fontes científicas (artigos, livros, instituições etc.)

• Sistema de filtros, buscas e ordenação

Documentação automática (Swagger + Redoc)

Endpoint especial dashboard com visão completa da planta

📦 Tecnologias Utilizadas

Python 3.12+

Django 5.2.8

Django REST Framework 3.16

Poetry (gerenciador de pacotes)

SQLite (padrão para desenvolvimento)

Pillow (upload de imagens)

drf-spectacular (API Schema / Swagger)

django-filter (filtros avançados)

🚀 Instalação e Execução
1. Clonar o repositório
git clone https://github.com/WillyFortunasc/Projeto_Integrador_API.git
cd Projeto_Integrador_API

2. Instalar dependências com Poetry
poetry install

3. Ativar o ambiente virtual
poetry shell

4. Aplicar migrações
poetry run python manage.py migrate

5. Criar superusuário (opcional, mas recomendado)
poetry run python manage.py createsuperuser

6. Rodar servidor
poetry run python manage.py runserver


A API estará disponível em:
👉 http://127.0.0.1:8000/api/catalogo/

🗂 Estrutura do Banco de Dados (Modelos)
🌿 Planta

Campos:

nome_cientifico

nome_popular

descricao

imagem

risco_extincao

data_registro

Relações:

Many-to-Many com Região

One-to-Many com UsoMedicinal

One-to-Many com FonteCientifica

💊 UsoMedicinal

Campos:

planta (FK)

parte_utilizada

modo_preparo

indicacao

🗺 Regiao

Campos:

nome

descricao

tipo_bioma

plantas (Many-to-Many)

📚 FonteCientifica

Campos:

planta (FK)

titulo

autores

ano

fonte

link

observacoes

🔌 Endpoints Principais

Base URL:

http://127.0.0.1:8000/api/catalogo/

🌿 Plantas
Método	Endpoint	Descrição
GET	/plantas/	Lista todas as plantas
POST	/plantas/	Cadastra planta
GET	/plantas/{id}/	Detalhe
PUT/PATCH	/plantas/{id}/	Atualizar
DELETE	/plantas/{id}/	Remover
GET	/plantas/{id}/dashboard/	Painel completo com usos, regiões e fontes
💊 Usos Medicinais
/usos/

🗺 Regiões e Biomas
/regioes/

📚 Fontes Científicas
/fontes-cientificas/

🔍 Sistema de Filtros
🌿 Planta – filtros disponíveis:
Por nome científico:
/plantas/?nome_cientifico=Hancornia speciosa

Por nome popular:
/plantas/?nome_popular=Mangaba

Por risco de extinção:
/plantas/?risco_extincao=True

Por bioma:
/plantas/?regioes__tipo_bioma=Cerrado

📌 Ordenação (ordering)
Ordenar por nome científico:
/plantas/?ordering=nome_cientifico

Ordenar por nome popular:
/plantas/?ordering=nome_popular

Ordenar por data de registro (mais recentes primeiro):
/plantas/?ordering=-data_registro

🔎 Busca (SearchFilter)

Busca textual em plantas:

/plantas/?search=manga


Campos incluídos na busca:

nome_cientifico

nome_popular

descricao

📊 Endpoint Especial: Dashboard Completo

Mostra tudo de uma planta, já organizado.

Exemplo:

/plantas/1/dashboard/


Retorna:

dados da planta

imagem

usos medicinais

regiões

fontes científicas

📘 Documentação Automática

Disponível graças ao drf-spectacular:

Swagger UI

👉 http://127.0.0.1:8000/api/docs/swagger/

Redoc

👉 http://127.0.0.1:8000/api/docs/redoc/

Schema JSON

👉 http://127.0.0.1:8000/api/schema/

🖼 Upload de Imagens

Faça upload via POST no endpoint de plantas:

Content-Type: multipart/form-data


Exemplo de campo:

imagem: arquivo.jpg


As imagens são armazenadas em:

/media/plantas/

🧪 Acesso ao Admin

👉 http://127.0.0.1:8000/admin/

🎯 Objetivo do Projeto

Este projeto visa integrar conhecimentos de:

Modelagem de dados

Criação de APIs REST

Serialização

Filtros e busca

Documentação automática

Django Admin avançado

Com foco no tema:

🌱 "Catalogação de Plantas Medicinais Brasileiras"

📄 Licença

Este projeto é acadêmico e livre para estudo.
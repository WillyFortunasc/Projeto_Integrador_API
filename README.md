# Catálogo de Plantas Medicinais — API REST (Django + DRF) 🌿

![WhatsApp Image 2025-12-02 at 10 47 39](https://github.com/user-attachments/assets/0d49e420-327b-409b-8c24-5abbd6ad0c98)

API desenvolvida para catalogar espécies vegetais medicinais, seus usos tradicionais, regiões de ocorrência e referências científicas.
Este projeto foi criado como Projeto Integrador, baseado na estrutura do professor, porém totalmente remodelado para o tema Plantas Medicinais do Cerrado e Outros Biomas Brasileiros.

A API oferece:

• Cadastro de plantas, incluindo imagem

• Cadastro de usos medicinais

• Cadastro de regiões e biomas onde ocorrem

• Cadastro de fontes científicas (artigos, livros, instituições etc.)

• Sistema de filtros, buscas e ordenação

• Documentação automática (Swagger + Redoc)

• Endpoint especial dashboard com visão completa da planta

# Tecnologias Utilizadas 📦

• Python 3.12+

• Django 5.2.8

• Django REST Framework 3.16

• Poetry (gerenciador de pacotes)

• SQLite (padrão para desenvolvimento)

• Pillow (upload de imagens)

• drf-spectacular (API Schema / Swagger)

• django-filter (filtros avançados)

# Instalação e Execução 🚀

1. Clonar o repositório: 

``` python

git clone https://github.com/WillyFortunasc/Projeto_Integrador_API.git

cd Projeto_Integrador_API 

```

2. Instalar dependências com Poetry

``` poetry install ```

3. Ativar o ambiente virtual

``` poetry shell  ```

4. Aplicar migrações

``` poetry run python manage.py migrate ```

5. Criar superusuário (opcional, mas recomendado)

``` poetry run python manage.py createsuperuser ```

6. Rodar servidor

``` poetry run python manage.py runserver ```

7. A API estará disponível em:

``` http://127.0.0.1:8000/api/catalogo/  ```

# Estrutura do Banco de Dados (Modelos) 🗂

### Planta 🌿

• nome_cientifico

• nome_popular

• descricao

• imagem

• risco_extincao

• data_registro

### ➔ Relações:

• Many-to-Many com Região

• One-to-Many com UsoMedicinal

• One-to-Many com FonteCientifica

### UsoMedicinal 💊 


• planta (FK)

• parte_utilizada

• modo_preparo

• indicacao

### Regiao 🗺


• nome

• descricao

• tipo_bioma

• plantas (Many-to-Many)

### FonteCientifica 📚 


• planta (FK)

• titulo

• autores

• ano

• fonte

• link

• observacoes

# Endpoints Principais 🔌

• Base URL:

``` http://127.0.0.1:8000/api/catalogo/ ```

• Plantas 🌿

Método	Endpoint	Descrição

GET	/plantas/	Lista todas as plantas
POST	/plantas/	Cadastra planta
GET	/plantas/{id}/	Detalhe
PUT/PATCH	/plantas/{id}/	Atualizar
DELETE	/plantas/{id}/	Remover
GET	/plantas/{id}/dashboard/	Painel completo com usos, regiões e fontes

• Usos Medicinais 💊

``` http://127.0.0.1:8000/usos/ ``` 

• Regiões e Biomas 🗺

``` http://127.0.0.1:8000/regioes/ ``` 

• Fontes Científicas 📚

``` http://127.0.0.1:8000/fontes-cientificas/ ``` 


# Sistema de Filtros 🔍 

🌿 Planta – filtros disponíveis:

• Por nome científico:

``` http://127.0.0.1:8000/plantas/?nome_cientifico=Hancornia speciosa ``` 

• Por nome popular:

``` http://127.0.0.1:8000/plantas/?nome_popular=Mangaba ``` 

• Por risco de extinção:

``` http://127.0.0.1:8000/plantas/?risco_extincao=True ``` 

• Por bioma:

``` http://127.0.0.1:8000/plantas/?regioes__tipo_bioma=Cerrado ``` 

# Ordenação (ordering) 📌

• Ordenar por nome científico:

``` http://127.0.0.1:8000/plantas/?ordering=nome_cientifico ``` 

• Ordenar por nome popular:

``` http://127.0.0.1:8000/plantas/?ordering=nome_popular ``` 

• Ordenar por data de registro (mais recentes primeiro):

``` http://127.0.0.1:8000/plantas/?ordering=-data_registro ``` 

# Busca (SearchFilter) 🔎

Busca textual em plantas:

``` http://127.0.0.1:8000/plantas/?search=manga ``` 


Campos incluídos na busca:

• nome_cientifico

• nome_popular

• descricao

# Endpoint Especial: Dashboard Completo 📊 

Mostra tudo de uma planta, já organizado.

Exemplo:

``` http://127.0.0.1:8000/plantas/1/dashboard/ ``` 


Retorna:

• dados da planta

• imagem

• usos medicinais

• regiões

• fontes científicas

# Documentação Automática 📘 

Disponível graças ao drf-spectacular:

Swagger UI

``` http://127.0.0.1:8000/api/docs/swagger/ ``` 

Redoc

``` http://127.0.0.1:8000/api/docs/redoc/ ``` 

Schema JSON

``` http://127.0.0.1:8000/api/schema/ ``` 

# Upload de Imagens 🖼

Faça upload via POST no endpoint de plantas:

Content-Type: multipart/form-data

Exemplo de campo:

imagem: arquivo.jpg


As imagens são armazenadas em:

``` http://127.0.0.1:8000/media/plantas/ ``` 

# Acesso ao Admin 🧪


``` http://127.0.0.1:8000/admin/ ```

# Objetivo do Projeto 🎯

Este projeto visa integrar conhecimentos de:

• Modelagem de dados

• Criação de APIs REST

• Serialização

• Filtros e busca

• Documentação automática

• Django Admin avançado

• Com foco no tema: "Catalogação de Plantas Medicinais Brasileiras"

# Licença 📄

• Este projeto é acadêmico e livre para estudo.

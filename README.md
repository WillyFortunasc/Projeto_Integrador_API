# Catálogo de Plantas Medicinais — API REST (Django + DRF) 🌿

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg?logo=python)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-5.2-green.svg?logo=django)](https://www.djangoproject.com/)
[![Django REST](https://img.shields.io/badge/DRF-3.16-red.svg?logo=django)](https://www.django-rest-framework.org/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57.svg?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![JWT](https://img.shields.io/badge/Auth-JWT-orange.svg)](https://jwt.io/)
[![License](https://img.shields.io/badge/License-Acadêmico-yellow.svg)](#)


## Instituições de Fomento e Parceria
[![Website IFB](https://img.shields.io/badge/Website-IFB-%23508C3C.svg?labelColor=%23C8102E)](https://www.ifb.edu.br/) 
[![Website ihwbr](https://img.shields.io/badge/Website-ihwbr-%23DAA520.svg?labelColor=%232E2E2E)](https://hardware.org.br/)

## Orientador (link para o perfil do orientador)

[![LinkedIn Claudio Ulisse](https://img.shields.io/badge/LinkedIn-Claudio_Ulisse-%230077B5.svg?labelColor=%23FFFFFF&logo=linkedin)](https://www.linkedin.com/in/claudioulisse/)
[![GitHub claulis](https://img.shields.io/badge/GitHub-claulis_(Claudio_Ulisse)-%23181717.svg?logo=github&logoColor=white)](https://github.com/claulis)
[![Lattes Claudio Ulisse](https://img.shields.io/badge/Lattes-Claudio_Ulisse-green.svg?logo=cnpq&logoColor=white)](http://lattes.cnpq.br/4607303092740768)


## Sumário

- [Visão Geral](#visão-geral)
- [Funcionalidades Principais](#funcionalidades-principais)
- [Tecnologias Utilizadas](#tecnologias-utilizadas-)
- [Estrutura do Projeto](#estrutura-do-projeto-)
- [Descrição dos Diretórios](#descrição-dos-diretórios)
- [Instalação e Execução](#instalação-e-execução-)
- [Estrutura do Banco de Dados (Modelos)](#estrutura-do-banco-de-dados-modelos-)
- [Endpoints Principais](#endpoints-principais-)
- [Sistema de Filtros](#sistema-de-filtros-)
- [Ordenação (ordering)](#ordenação-ordering-)
- [Busca (SearchFilter)](#busca-searchfilter-)
- [Endpoint Especial: Dashboard Completo](#endpoint-especial-dashboard-completo-)
- [Documentação Automática](#documentação-automática-)
- [Upload de Imagens](#upload-de-imagens-)
- [Acesso ao Admin](#acesso-ao-admin-)
- [Objetivo do Projeto](#objetivo-do-projeto-)
- [Autenticação (JWT)](#autenticação-jwt-)
- [Perfis e Permissões (Grupos)](#perfis-e-permissões-grupos-)
- [Controle de Acesso por Perfil](#controle-de-acesso-por-perfil-)
- [Deploy no Render](#deploy-no-render-)
- [Licença](#licença-)


# Visão Geral

API REST desenvolvida em **Django + Django REST Framework** para catalogação de **plantas medicinais brasileiras**, seus **usos terapêuticos**, **regiões e biomas**, e **fontes científicas**.

Este projeto foi desenvolvido como **Projeto Integrador**, seguindo a **estrutura base proposta pelo professor**, porém **totalmente remodelado** para o tema:

> **Plantas Medicinais do Cerrado e Outros Biomas Brasileiros**

A API é segura, documentada, organizada e utiliza boas práticas de desenvolvimento backend.

---
## Funcionalidades Principais

- Cadastro de plantas medicinais (com upload de imagem)
- Cadastro de usos medicinais
- Cadastro de regiões e biomas
- Cadastro de fontes científicas
- Relacionamentos entre entidades
- Sistema de filtros, busca e ordenação
- Autenticação via JWT
- Controle de acesso por grupos
- Documentação automática (Swagger e Redoc)
- Endpoint especial de dashboard por planta

---

## Tecnologias Utilizadas 📦

| Tecnologia | Versão | Descrição |
|-----------|--------|----------|
| Python | 3.12+ | Linguagem de programação utilizada no desenvolvimento da API. |
| Django | 5.2.8 | Framework web responsável pela estrutura base do projeto. |
| Django REST Framework | 3.16 | Framework para construção de APIs RESTful. |
| Poetry | Latest | Gerenciador de dependências e ambientes virtuais do projeto. |
| SQLite | Padrão | Banco de dados utilizado no ambiente de desenvolvimento. |
| Pillow | Latest | Biblioteca para processamento e upload de imagens. |
| drf-spectacular | Latest | Geração automática de documentação OpenAPI (Swagger e Redoc). |
| django-filter | Latest | Implementação de filtros avançados nas consultas da API. |
| SimpleJWT | Latest | Implementação de autenticação baseada em JSON Web Tokens (JWT). |

---  

## Estrutura do Projeto 📁

```text
Projeto_Integrador_API/
├── manage.py
├── pyproject.toml
├── poetry.lock
├── db.sqlite3
├── README.md
│
├── api_projetos/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── api/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── catalogo_plantas/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── permissions.py
│   └── migrations/
│
├── media/
│   └── plantas/
│       └── *.jpg
│
├── static/
└── .venv/
```


# Descrição dos Diretórios


| Diretório / Arquivo | Descrição |
|---------------------|----------|
| `Projeto_Integrador_API/` | Diretório raiz do projeto, contendo toda a estrutura da API. |
| `manage.py` | Script principal do Django para execução de comandos administrativos. |
| `pyproject.toml` | Arquivo de configuração do Poetry com dependências e metadados do projeto. |
| `poetry.lock` | Controle das versões exatas das dependências instaladas pelo Poetry. |
| `db.sqlite3` | Banco de dados SQLite utilizado no ambiente de desenvolvimento. |
| `README.md` | Documentação principal do projeto. |
| `api_projetos/` | Diretório de configuração central do projeto Django. |
| `api_projetos/settings.py` | Configurações globais (apps, banco de dados, JWT, permissões, Swagger, mídia). |
| `api_projetos/urls.py` | Rotas principais do projeto, incluindo apps, autenticação e documentação. |
| `api_projetos/asgi.py` | Configuração para execução da aplicação em servidores ASGI. |
| `api_projetos/wsgi.py` | Configuração para execução da aplicação em servidores WSGI. |
| `api/` | Aplicação base utilizada como referência estrutural do Projeto Integrador. |
| `api/models.py` | Modelos auxiliares da aplicação base (se aplicável). |
| `api/serializers.py` | Serializadores da aplicação base. |
| `api/views.py` | Views e ViewSets da aplicação base. |
| `api/urls.py` | Rotas específicas da aplicação base. |
| `catalogo_plantas/` | Aplicação principal responsável pelo domínio de plantas medicinais. |
| `catalogo_plantas/models.py` | Definição dos modelos principais do sistema. |
| `catalogo_plantas/serializers.py` | Serialização e validação dos dados da API. |
| `catalogo_plantas/views.py` | ViewSets, filtros, buscas, ordenação e endpoint de dashboard. |
| `catalogo_plantas/permissions.py` | Permissões personalizadas baseadas em grupos de usuários. |
| `catalogo_plantas/urls.py` | Rotas específicas da aplicação de catálogo de plantas. |
| `catalogo_plantas/admin.py` | Configuração do Django Admin para gerenciamento dos dados. |
| `migrations/` | Histórico de migrações do banco de dados. |
| `media/` | Diretório para armazenamento de arquivos enviados pela API. |
| `media/plantas/` | Armazena as imagens das plantas cadastradas. |
| `static/` | Diretório reservado para arquivos estáticos do projeto. |
| `.venv/` | Ambiente virtual criado e gerenciado pelo Poetry. |


# Instalação e Execução 🚀

1. Clonar o repositório: 

``` python

git clone https://github.com/WillyFortunasc/Projeto_Integrador_API.git

cd Projeto_Integrador_API 

```

2. Instalar dependências com Poetry

``` python

poetry install 

```

3. Ativar o ambiente virtual

``` python

poetry shell

```

4. Aplicar migrações

``` python

poetry run python manage.py migrate 

```

5. Criar superusuário (opcional, mas recomendado)

``` python

poetry run python manage.py createsuperuser 

```

6. Rodar servidor

``` python

poetry run python manage.py runserver 

```

7. A API estará disponível em:

``` http://127.0.0.1:8000/api/catalogo/ ```

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

| Método    | Endpoint                 | Descrição                                  |
| --------- | ------------------------ | ------------------------------------------ |
| GET       | /plantas/                | Lista todas as plantas                     |
| POST      | /plantas/                | Cadastra planta                            |
| GET       | /plantas/{id}/           | Detalhe                                    |
| PUT/PATCH | /plantas/{id}/           | Atualizar                                  |
| DELETE    | /plantas/{id}/           | Remover                                    |
| GET       | /plantas/{id}/dashboard/ | Painel completo com usos, regiões e fontes |


• Usos Medicinais 💊

``` http://127.0.0.1:8000/api/catalogo/usos-medicinais/ ``` 

• Regiões e Biomas 🗺

``` http://127.0.0.1:8000/api/catalogo/regioes/ ``` 

• Fontes Científicas 📚

``` http://127.0.0.1:8000/api/catalogo/fontes-cientificas/ ``` 


# Sistema de Filtros 🔍 

🌿 Planta – filtros disponíveis:

• Por nome científico:

``` http://127.0.0.1:8000/api/catalogo/plantas/?nome_cientifico=Hancornia speciosa Gomes ``` 

• Por nome popular:

``` http://127.0.0.1:8000/api/catalogo/plantas/?nome_popular=Mangaba ``` 

• Por risco de extinção:

``` http://127.0.0.1:8000/api/catalogo/plantas/?risco_extincao=True ``` 

• Por bioma:

``` http://127.0.0.1:8000/api/catalogo/plantas/?regioes__tipo_bioma=Cerrado ``` 


# Ordenação (ordering) 📌

• Ordenar por nome científico:

``` http://127.0.0.1:8000/api/catalogo/plantas/?ordering=nome_cientifico ``` 

• Ordenar por nome popular:

``` http://127.0.0.1:8000/api/catalogo/plantas/?ordering=nome_popular ``` 

• Ordenar por data de registro (mais recentes primeiro):

``` http://127.0.0.1:8000/api/catalogo/plantas/?ordering=-data_registro ``` 

# Busca (SearchFilter) 🔎

Busca textual em plantas:

``` http://127.0.0.1:8000/api/catalogo/plantas/?search=mangaba ``` 


Campos incluídos na busca:

• nome_cientifico

• nome_popular

• descricao

# Endpoint Especial: Dashboard Completo 📊 

Mostra tudo de uma planta, já organizado.

Exemplo:

``` http://127.0.0.1:8000/api/catalogo/plantas/1/dashboard/ ``` 


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

``` python

Content-Type: multipart/form-data 

```

Exemplo de campo:

``` python

imagem: arquivo.jpg

```


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

# Autenticação (JWT) 🔐

A API utiliza JSON Web Tokens (JWT) para autenticação.

### Endpoints de autenticação

- Confirmar o token

``` http://127.0.0.1:8000/api/token/ ```

- Obter token (login)

``` POST /api/token/ ```

- Renovar token

``` POST /api/token/refresh/ ```

Exemplo de login (POST /api/token/)

``` python
{
  "username": "seu_usuario",
  "password": "sua_senha"
} 
```

Resposta:

``` python 

{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

- Usar o token no Swagger

Clique em Authorize → cole:

``` Bearer <ACCESS_TOKEN> ```

- Usar em requisições da API

``` Authorization: Bearer <ACCESS_TOKEN> ```

- Perfis e Permissões (Grupos) 🛡

Os grupos devem ser criados no painel ``` admin (/admin/): ```

# Grupos utilizados:

- Admin: acesso total

- Pesquisador: cria e edita usos e fontes

- Usuario: somente leitura

## Controle de Acesso por Perfil 🔐

| Recurso / Permissão | Admin | Pesquisador | Usuário |
|--------------------|:-----:|:-----------:|:-------:|
| **Administração – Log Entry** | | | |
| Can add log entry | ✅ | ❌ | ❌ |
| Can change log entry | ✅ | ❌ | ❌ |
| Can delete log entry | ✅ | ❌ | ❌ |
| Can view log entry | ✅ | ❌ | ❌ |
| **API – Projeto** | | | |
| Can add projeto | ✅ | ❌ | ❌ |
| Can change projeto | ✅ | ❌ | ❌ |
| Can delete projeto | ✅ | ❌ | ❌ |
| Can view projeto | ✅ | ❌ | ❌ |
| **API – Responsável** | | | |
| Can add responsavel | ✅ | ❌ | ❌ |
| Can change responsavel | ✅ | ❌ | ❌ |
| Can delete responsavel | ✅ | ❌ | ❌ |
| Can view responsavel | ✅ | ❌ | ❌ |
| **API – Tarefa** | | | |
| Can add tarefa | ✅ | ❌ | ❌ |
| Can change tarefa | ✅ | ❌ | ❌ |
| Can delete tarefa | ✅ | ❌ | ❌ |
| Can view tarefa | ✅ | ❌ | ❌ |
| **Autenticação – Grupo** | | | |
| Can add group | ✅ | ❌ | ❌ |
| Can change group | ✅ | ❌ | ❌ |
| Can delete group | ✅ | ❌ | ❌ |
| Can view group | ✅ | ❌ | ❌ |
| **Autenticação – Permissão** | | | |
| Can add permission | ✅ | ❌ | ❌ |
| Can change permission | ✅ | ❌ | ❌ |
| Can delete permission | ✅ | ❌ | ❌ |
| Can view permission | ✅ | ❌ | ❌ |
| **Autenticação – Usuário** | | | |
| Can add user | ✅ | ❌ | ❌ |
| Can change user | ✅ | ❌ | ❌ |
| Can delete user | ✅ | ❌ | ❌ |
| Can view user | ✅ | ❌ | ❌ |
| **Token de Autenticação** | | | |
| Can add token | ✅ | ❌ | ❌ |
| Can change token | ✅ | ❌ | ❌ |
| Can delete token | ✅ | ❌ | ❌ |
| Can view token | ✅ | ❌ | ❌ |
| **Catálogo – Fonte Científica** | | | |
| Can add fonte cientifica | ✅ | ✅ | ❌ |
| Can change fonte cientifica | ✅ | ✅ | ❌ |
| Can delete fonte cientifica | ✅ | ❌ | ❌ |
| Can view fonte cientifica | ✅ | ✅ | ✅ |
| **Catálogo – Planta** | | | |
| Can add planta | ✅ | ✅ | ❌ |
| Can change planta | ✅ | ✅ | ❌ |
| Can delete planta | ✅ | ❌ | ❌ |
| Can view planta | ✅ | ✅ | ✅ |
| **Catálogo – Região** | | | |
| Can add regiao | ✅ | ✅ | ❌ |
| Can change regiao | ✅ | ✅ | ❌ |
| Can delete regiao | ✅ | ❌ | ❌ |
| Can view regiao | ✅ | ✅ | ✅ |
| **Catálogo – Uso Medicinal** | | | |
| Can add uso medicinal | ✅ | ✅ | ❌ |
| Can change uso medicinal | ✅ | ✅ | ❌ |
| Can delete uso medicinal | ✅ | ❌ | ❌ |
| Can view uso medicinal | ✅ | ✅ | ✅ |
| **Tipos de Conteúdo** | | | |
| Can add content type | ✅ | ❌ | ❌ |
| Can change content type | ✅ | ❌ | ❌ |
| Can delete content type | ✅ | ❌ | ❌ |
| Can view content type | ✅ | ❌ | ❌ |
| **Sessões** | | | |
| Can add session | ✅ | ❌ | ❌ |
| Can change session | ✅ | ❌ | ❌ |
| Can delete session | ✅ | ❌ | ❌ |
| Can view session | ✅ | ❌ | ❌ |


# Deploy no Render ☁️

A API foi publicada em ambiente de produção utilizando a plataforma Render, permitindo o acesso público aos endpoints e à documentação automática.

**URL da aplicação em produção**

- API online 

https://projeto-integrador-api-oficial.onrender.com/

**Configuração do serviço**

O serviço foi criado como Web Service com as seguintes configurações:

- Runtime: Python

- Build Command:

```python
pip install -r requirements.txt

```


- Start Command:

``` python
gunicorn api_projetos.wsgi:application

```

O módulo api_projetos corresponde ao diretório onde estão localizados os arquivos settings.py e wsgi.py.

**Ajustes para produção**

No arquivo settings.py, foram realizados os seguintes ajustes para execução em produção:

```python

DEBUG = False

ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1']

```

**Rota raiz da aplicação**

Para evitar o retorno padrão Not Found e indicar que a API está ativa, foi criada uma rota raiz (/).
Ao acessar a URL principal da aplicação, é retornado o seguinte JSON informativo:

``` python
{
  "status": "API online",
  "endpoints": {
    "admin": "/admin/",
    "token": "/api/token/",
    "token refresh": "/api/token/refresh/",
    "api base": "/api/",
    "catalogo plantas": "/api/catalogo/",
    "swagger": "/api/docs/swagger/",
    "redoc": "/api/docs/redoc/"
  }
}

```

**Documentação em produção**

A documentação automática da API está disponível em produção através do Swagger UI:

``` python

https://projeto-integrador-api-oficial.onrender.com/api/docs/swagger/

```

**Status do deploy**

``` python

API online e funcional

Endpoints acessíveis em produção

Documentação ativa

Ambiente pronto para uso e avaliação acadêmica

```

# Licença 📄

• Este projeto é acadêmico e livre para estudo.
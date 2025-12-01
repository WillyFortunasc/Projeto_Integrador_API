# API Projetos

> Projeto Django + Django REST Framework para gerenciamento de projetos.

[![Django](https://img.shields.io/badge/Django-5.2.8-092E20?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django%20REST%20Framework-3.16.1-A30000?style=flat-square&logo=django)](https://www.django-rest-framework.org/)
[![Swagger/OpenAPI](https://img.shields.io/badge/Swagger%2FOpenAPI-Enabled-85EA2D?style=flat-square&logo=swagger)](https://swagger.io/)
[![Poetry](https://img.shields.io/badge/Poetry-Latest-60A5FA?style=flat-square&logo=poetry)](https://python-poetry.org/)

---

## Visão Geral

Este repositório contém uma API construída com Django (>=5.2.8) e
Django REST Framework para gerenciar projetos. A API já inclui
integração com `drf-yasg` para documentação (Swagger / ReDoc) e usa
SQLite por padrão para facilitar o desenvolvimento.

As dependências principais (definidas em `pyproject.toml`) são:

- `django (>=5.2.8,<6.0.0)`
- `djangorestframework (>=3.16.1,<4.0.0)`
- `drf-yasg (>=1.21.11,<2.0.0)`

## Pré-requisitos

- Python 3.12 ou superior
- Git (para clonar o repositório)
- **Poetry** (gerenciador de dependências)

### Instalar Poetry

Se ainda não tem Poetry instalado, siga a [documentação oficial](https://python-poetry.org/docs/#installation):

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Após instalação, adicione o Poetry ao `PATH`:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Verifique a instalação:

```bash
poetry --version
```

## Instalação com Poetry

1. Clone o projeto

```bash
git clone <URL_DO_REPOSITORIO>
cd api_projetos
```

2. Instalar dependências e criar ambiente virtual

Poetry cria automaticamente um virtualenv e instala todas as dependências:

```bash
poetry install
```

3. Ativar o ambiente virtual (opcional)

O Poetry gerencia o virtualenv automaticamente. Para executar comandos dentro do ambiente:

```bash
poetry run <comando>
```

Ou, para entrar em um shell interativo:

```bash
poetry shell
```

Dentro do shell, você pode rodar comandos normalmente sem o prefixo `poetry run`.

## Configuração do banco de dados

O projeto já vem configurado para usar SQLite (arquivo `db.sqlite3` na raiz).
Para preparar o banco:

```bash
poetry run python manage.py migrate
```

Opcionalmente, criar um usuário administrador:

```bash
poetry run python manage.py createsuperuser
```

Se desejar usar outro banco (Postgres, MySQL, etc.), edite `api_projetos/settings.py`
na seção `DATABASES` e instale o driver apropriado através do Poetry ou manualmente.

## Rodando o servidor

```bash
poetry run python manage.py runserver
```

A API ficará disponível em `http://127.0.0.1:8000/` e os endpoints do app `api`
estão sob `http://127.0.0.1:8000/api/`.

### Documentação (Swagger / ReDoc)

- Swagger UI: `http://127.0.0.1:8000/swagger/`
- ReDoc: `http://127.0.0.1:8000/redoc/`

Esses endpoints são servidos via `drf-yasg` e expõem a especificação da API.

## Endpoints importantes

- `GET /api/projetos/` — listar projetos
- `GET /api/projetos/{id}/` — detalhes de um projeto
- Outros endpoints registrados pelo `DefaultRouter` do DRF no `api/urls.py`.

Para ver todos os endpoints e testar via UI, abra `/swagger/` após iniciar o servidor.


## Dicas e troubleshooting

### Poetry não encontrado?

Se `poetry` não está no seu `PATH`, reinstale e configure corretamente:

```bash
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"
```

### Problemas ao rodar `poetry install`?

Verifique se a versão do Python está correta (>= 3.12):

```bash
python --version
```

Se precisar usar uma versão específica, configure no `pyproject.toml` ou use:

```bash
poetry env use python3.12
```

### Limpar cache do Poetry

Se enfrentar problemas de dependência, tente:

```bash
poetry cache clear . --all
poetry install
```

### Adicionar novas dependências

Para adicionar uma dependência (ex: `requests`):

```bash
poetry add requests
```

Para remover:

```bash
poetry remove requests
```

## Como contribuir

- Abra uma issue descrevendo o bug ou feature desejada.
- Faça um fork, crie uma branch com o prefixo `feature/` ou `fix/`, implemente e
  envie um pull request apontando para a branch `main` do repositório original.


## Projeto Integrador: Catálogo de Plantas Medicinais do Cerrado 
![download](https://github.com/user-attachments/assets/4a26083f-f9c7-418a-a035-837305778745)


Este projeto é uma extensão do repositório original do professor, adicionando um novo app `catalogo_plantas` para gerenciar informações sobre plantas medicinais, usos, e regiões do cerrado.

### Novos Endpoints:

- `/api/catalogo/plantas/`
- `/api/catalogo/usos/`
- `/api/catalogo/regioes/`

### Como usar:

1. Criar plantas com imagem, nome científico e popular, risco de extinção, etc.  
2. Cadastrar usos medicinais relacionados às plantas.  
3. Associar plantas às regiões do cerrado.

---

*Demais instruções para rodar e configurar continuam válidas conforme o README original.*

## URLs principais da API

- Listagem de Plantas: [http://127.0.0.1:8000/api/catalogo/plantas/](http://127.0.0.1:8000/api/catalogo/plantas/)
- Listagem de Usos Medicinais: [http://127.0.0.1:8000/api/catalogo/usos/](http://127.0.0.1:8000/api/catalogo/usos/)
- Listagem de Regiões: [http://127.0.0.1:8000/api/catalogo/regioes/](http://127.0.0.1:8000/api/catalogo/regioes/)
- Fontes Científicas: http://127.0.0.1:8000/api/catalogo/fontes-cientificas/
- Django Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- Dashboard: http://127.0.0.1:8000/api/catalogo/plantas/id/dashboard/


# Filtros e Ordenação da API - Catálogo de Plantas Medicianais 

# 1. Plantas 🌱

- Filtrar por nome científico	nome_cientifico	http://127.0.0.1:8000/api/catalogo/plantas/?nome_cientifico=Hancornia speciosa
- Filtrar por nome popular	nome_popular	http://127.0.0.1:8000/api/catalogo/plantas/?nome_popular=Mangaba
- Filtrar por risco de extinção	risco_extincao	http://127.0.0.1:8000/api/catalogo/plantas/?risco_extincao=true
- Filtrar por bioma da região	regioes__tipo_bioma	http://127.0.0.1:8000/api/catalogo/plantas/?regioes__tipo_bioma=Cerrado

# Ordenação ↕

- Ordenar por nome científico (A–Z)	ordering=nome_cientifico	http://127.0.0.1:8000/api/catalogo/plantas/?ordering=nome_cientifico
- Ordenar por nome popular (A–Z)	ordering=nome_popular	http://127.0.0.1:8000/api/catalogo/plantas/?ordering=nome_popular
- Ordenar por data de registro (mais recente primeiro)	ordering=-data_registro	http://127.0.0.1:8000/api/catalogo/plantas/?ordering=-data_registro
- Ordenar por data de registro (mais antigo primeiro)	ordering=data_registro	http://127.0.0.1:8000/api/catalogo/plantas/?ordering=data_registro

# 2. Usos Medicianais 🌿

- Filtrar por parte utilizada	parte_utilizada	http://127.0.0.1:8000/api/catalogo/usos-medicinais/?parte_utilizada=Folha
- Filtrar por indicação	indicacao	http://127.0.0.1:8000/api/catalogo/usos-medicinais/?indicacao=Diabetes

# Ordenação ↕

- Ordenar por parte utilizada	ordering=parte_utilizada	http://127.0.0.1:8000/api/catalogo/usos-medicinais/?ordering=parte_utilizada

# 3. Regiões 📍

- Filtrar por nome da região	nome	http://127.0.0.1:8000/api/catalogo/regioes/?nome=Goiás
- Filtrar por bioma	tipo_bioma	http://127.0.0.1:8000/api/catalogo/regioes/?tipo_bioma=Cerrado

# Ordenação ↕

- Ordenar por nome	ordering=nome	http://127.0.0.1:8000/api/catalogo/regioes/?ordering=nome
- Ordenar por bioma	ordering=tipo_bioma	http://127.0.0.1:8000/api/catalogo/regioes/?ordering=tipo_bioma

# 4. Fontes Científicas 📚

- Filtrar por ano	ano	http://127.0.0.1:8000/api/catalogo/fontes-cientificas/?ano=2020
- Filtrar por fonte	fonte	http://127.0.0.1:8000/api/catalogo/fontes-cientificas/?fonte=Reflora

# Ordenação ↕

- Ordenar por ano	ordering=ano	http://127.0.0.1:8000/api/catalogo/fontes-cientificas/?ordering=ano
- Ordenar por ano (do mais recente para o mais antigo)	ordering=-ano	http://127.0.0.1:8000/api/catalogo/fontes-cientificas/?ordering=-ano
- Ordenar por título	ordering=titulo	http://127.0.0.1:8000/api/catalogo/fontes-cientificas/?ordering=titulo

# 5. Dashboard Geral 📊

http://127.0.0.1:8000/api/catalogo/dashboard-geral/


- Totais

- Resumo

- Plantas recentes

- Estatísticas gerais

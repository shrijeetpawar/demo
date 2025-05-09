# demo

# Indian Bank Branch GraphQL API

This project is a Django-based GraphQL API that serves bank branch data from a PostgreSQL database. It fulfills the requirements of the assignment and is built using scalable, production-ready practices with a SaaS-style clean architecture.

## Tech Stack

- Python 3.10+
- Django 5.x
- Graphene-Django (GraphQL)
- PostgreSQL
- Docker-ready (optional for deployment)
- Tested on Windows

## Features

- ✅ GraphQL endpoint at `/gql`
- ✅ Query to get bank branches with nested bank details
- ✅ Uses real RBI data (via `indian_banks.sql`)
- ✅ Clean codebase following Django best practices
- ✅ Basic unit test for GraphQL queries
- ✅ UTF-8 safe PostgreSQL data handling

---

##  Getting Started

###  Prerequisites

- PostgreSQL (configured with a database named `bankdb`)
- Python 3.10+
- Virtualenv (recommended)

### 📥 Install & Run Locally

```bash
git clone https://github.com/shrijeetpawar/demo.git
cd demo

python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)

pip install -r requirements.txt

🛠️ Configure PostgreSQL (if not already)

    Create the database:

CREATE DATABASE bankdb WITH ENCODING='UTF8';

Import cleaned SQL data:

psql -U postgres -d bankdb -f indian_banks.sql

In config/settings.py, set:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'bankdb',
            'USER': 'postgres',
            'PASSWORD': 'yourpassword',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

🚀 Start the Server

python manage.py runserver

Visit: http://localhost:8000/gql
🔍 Sample GraphQL Query

query {
  branches {
    ifsc
    branch
    bank {
      name
    }
  }
}

🧪 Run Tests

python manage.py test

Includes:

    GraphQL test that checks correct branch query resolution

☁️ Deployment Ready

You can deploy this on:

    Heroku

    Render

    Dockerized environments

Includes:

    Procfile

    requirements.txt

    UTF-8 data handling

⏱ Time Taken

    6 hours total:

        2 hours: DB setup and encoding fixes

        2 hours: Django + GraphQL setup

        1 hour: Test cases and validation

        1 hour: Docs, cleanup, and polish

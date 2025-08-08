# newsole2

my_django_app/
├── accounts/ # User authentication app
│ ├── migrations/
│ ├── templates/
│ │ └── registration/
│ ├── **init**.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ └── views.py
├── core/ # Main business logic app
│ ├── migrations/
│ ├── templates/
│ │ └── home.html
│ │ └── about.html
│ │ └── contact.html
│ │ └── base.html
│ ├── filters.py
│ ├── **init**.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── config/ # Django settings package
│ ├── **init**.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── media/ # Uploaded media (Cloudinary in production)
├── staticfiles/ # Collected static files
├── .gitignore
├── manage.py
├── Pipfile
├── Pipfile.lock
├── Procfile
├── README.md
├── requirements.txt
└── runtime.txt

## Uses sqlite as database for local building

## Uses Postgres for production

## Start Postgres locally

Start PostgreSQL locally (macOS)
`brew services start postgresql`

Access PostgrSQL shell in local terminal:
`psql postgres`

Check if PostgreSQL is running
`brew services list`

## Test .env variables

`python manage.py shell`

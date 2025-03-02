import os
from pathlib import Path

DEBUG = True
# Percorso della cartella del progetto
BASE_DIR = Path(__file__).resolve().parent.parent

# Chiave segreta per Django
SECRET_KEY = 'sostituisci_questa_chiave_con_una_sicura'

# Configurazione del database MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'quaderno_campagna',  # Sostituisci con il nome del tuo database
        'USER': 'root',  # Sostituisci con il tuo utente MySQL
        'PASSWORD': '969458',  # Sostituisci con la tua password MySQL
        'HOST': 'localhost',  # Indirizzo del server MySQL
        'PORT': '3306',  # Porta predefinita MySQL
    }
}

# Configurazione ALLOWED_HOSTS
ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Applicazioni installate
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quaderno',  # App per la gestione del quaderno di campagna
    'bottiglia', # App per la gestione dell imbottigliamento
]

# Middleware richiesti per Django Admin
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configurazione dei template
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ROOT_URLCONF = 'qdc.urls'
#ROOT_URLCONF = 'quaderno.urls'  # Sostituisci 'quaderno' con il nome della tua app principale

# Configurazione per i file statici
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "mystaticfiles"
]
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Percorso in cui verranno raccolti i file statici

# -*- coding: utf-8 -*-

import os
import sys
import glob

gettext_noop = lambda s: s


def rel_project(*x):
    return os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), *x))


def REL(*x):
    u"""Django's settings module exports only uppercase object."""
    return rel_project(*x)

rel_public = lambda *x: rel_project('public', *x)


# get local software repositories
sys.path.insert(0, rel_project('..', 'lib'))
gettext_noop = lambda s: s


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS

SECRET_KEY = 'somedefaultsecretkey'

ALLOWED_HOSTS = ('djbook.ru', 'www.djbook.ru')

DATABASES = {
    'default': dict(
        ENGINE='django.db.backends.mysql',
        NAME='djbookru',
        USER='djbookru',
        PASSWORD='q1',
        HOST='localhost',
        PORT='',
        )
}

DEFAULT_FROM_EMAIL = 'support@djbook.ru'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Moscow'
# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-RU'
LANGUAGES = (
    ('ru', gettext_noop('Russian')),
    ('en', gettext_noop('English')),
)
USE_I18N = True
USE_L10N = False
USE_THOUSAND_SEPARATOR = False
LOCALE_PATHS = (
    rel_project('locale'),
    rel_project('main', 'locale'),
)

SITE_ID = 1
SITE_URL = 'http://djbook.ru/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = rel_public('media')
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = rel_public('static')
# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'
# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    rel_project('static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'src.forum.middleware.LastLoginMiddleware',
    'src.forum.middleware.UsersOnline',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'src.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'src.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'social.apps.django_app.context_processors.backends',
    'src.context_processors.custom',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    rel_project('templates'),
)

FIXTURE_DIRS = (
    rel_project('fixtures'),
)

USER_ONLINE_TIMEOUT = 15

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'plain': {
            'format': '%(asctime)s %(message)s',
        },
        'verbose': {
            'format':
                '%(levelname)s %(asctime)s %(name)s %(process)d %(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'main_log': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': rel_project('..', 'logs', 'main.log'),
            'maxBytes': 1024 * 1024 * 1,
            'backupCount': 10,
            'formatter': 'verbose',
        },
        'haystack_log': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': rel_project('..', 'logs', 'haystack.log'),
            'maxBytes': 1024 * 1024 * 1,
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'profile_db_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': rel_project('..', 'logs', 'profile.db.log'),
            'maxBytes': 1024 * 1024 * 1,
            'backupCount': 5,
            'formatter': 'plain',
        }

    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'haystack': dict(
            handlers=['haystack_log'],
            level='ERROR',
            propagate=True,
        ),
        'django.db.backends': dict(
            handlers=['profile_db_log'],
            level='ERROR',
            propagate=True,
        )
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.flatpages',

    'bootstrapform',
    'pagedown',
    'oembed',
    'pagination',
    'sorl.thumbnail',
    'tagging',
    'ordered_model',
    'social.apps.django_app.default',
    'haystack',
    'haystack_static_pages',

    'src.forum',
    'src.accounts',
    'src.claims',
    'src.comments',
    'src.doc_comments',
    'src.examples',
    'src.main',
    'src.news',
    'src.videos',
    'src.links',
    'src.header_messages',
)


### AUTH: BEGIN
#AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = '/auth/login/'
LOGIN_ERROR_URL = LOGIN_URL
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
### AUTH: END


### SOCIAL_AUTH: BEGIN
SOCIAL_AUTH_USER_MODEL = 'accounts.User'
SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'src.accounts.social_auth_pipelines.check_email',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user'
)

SOCIAL_AUTH_GITHUB_APP_ID = ''
SOCIAL_AUTH_GITHUB_API_SECRET = ''
SOCIAL_AUTH_GITHUB_SCOPE = ['user:email']

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

SOCIAL_AUTH_VK_OAUTH2_KEY = ''
SOCIAL_AUTH_VK_OAUTH2_SECRET = ''

AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
    'social.backends.github.GithubOAuth2',
    'social.backends.yandex.YandexOpenId',
    'social.backends.vk.VKOAuth2',
    'src.accounts.backends.CustomUserBackend',
)
### SOCIAL_AUTH: END

### DOCUMENTATION: BEGIN
DJANGO_DOCUMENTATION_VERSION = '1.8'
DJANGO_DOCUMENTATION_HTML = REL('../docs/rel%s/' % DJANGO_DOCUMENTATION_VERSION)
DJANGO_DOCUMENTATION_URL = '/rel%s/' % DJANGO_DOCUMENTATION_VERSION
DJANGO_DOCUMENTATION_SITEMAP_URL = '%ssitemap.xml' % DJANGO_DOCUMENTATION_URL
### DOCUMENTATION: END

### HAYSTACK: BEGIN
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'xapian_backend.XapianEngine',
        'PATH': rel_project('search', 'xapian_index'),
        'HAYSTACK_XAPIAN_LANGUAGE': 'ru',
        # 'INCLUDE_SPELLING': True  # TODO: use this
    },
}


def get_doc_pages():
    for directory, dirnames, filenames in os.walk(DJANGO_DOCUMENTATION_HTML):
        for item in glob.glob('%s/*.html' % directory):
            yield item

HAYSTACK_STATIC_PAGES = tuple(get_doc_pages())
HAYSTACK_STATIC_MAPPING = {
    DJANGO_DOCUMENTATION_HTML: DJANGO_DOCUMENTATION_URL
}
### HAYSTACK: END


### FEEDBACK: BEGIN
EMAIL_SUBJECT_PREFIX = '[Djbook.ru]'
DATETIME_FORMAT = 'j N Y, G:i'
FEEDBACK_SUBJECT = gettext_noop(u'Feedback message from Djbook.ru')
### FEEDBACK: END

RECAPTCHA_PUBLIC = ''
RECAPTCHA_PRIVATE = ''

MIGRATION_MODULES = {
    'auth': 'src.main.migrations_auth',
}

# testing
# TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--nocapture',
    '--with-runnable-test-names',
    '--nologcapture',
    # '--with-coverage',
    # '--cover-html',
    # '--cover-package=src',
    # '--cover-inclusive'
]

NOSE_PLUGINS = [
    'nose_runnable_test_names.RunnableTestNames'
]

try:
    from local_settings import *
except ImportError:
    pass

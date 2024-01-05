"""
Django settings for webProject project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-y*q(!zvfa)k=-doo#0yvi&(sg-_usi6_+a!hthj1l8j&a!28ly"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '.localhost', '127.0.0.1']

CSRF_TRUSTED_ORIGINS = ['https://sandbox-api.iyzipay.com']


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'testwebproject@outlook.com'
EMAIL_HOST_PASSWORD = 'WebProjectAdmin.1234'
EMAIL_FROM_ADDRESS = 'testwebproject@outlook.com'
DEFAULT_FROM_EMAIL = 'testwebproject@outlook.com'

# Iyzico Payment Login: Mail: testwebproject@outlook.com ||| Password: 102938 @ https://sandbox-merchant.iyzipay.com/

# Application definition

INSTALLED_APPS = [
    # 'jet_django',
    # 'django_q',
    "jazzmin",
    "widget_tweaks",
    "nested_admin",
    "import_export",
    "django_filters",
    "django_extensions",
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail',

    'modelcluster',
    'taggit',

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.humanize",
    "django.contrib.postgres",
    "django.contrib.redirects",

    "ckeditor",
    "ckeditor_uploader",
    
    # Our Apps
    "store",
    "schools",
    "members",
    "products",
    "payment",
    "orders",
    "cart",
    "management",
    "discounts",
    "support",
    "warehouse",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "webProject.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'webProject.context_processors.default',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = "webProject.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "tr-tr"

TIME_ZONE = "Europe/Istanbul"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/"


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


JET_PROJECT = 'entegrasyoncloud'
JET_TOKEN = 'f902cf72-0469-4ff4-a7ef-27f1a8dc1050'

JAZZMIN_SETTINGS = {
    'site_title' : "Life Vest",
    'site_brand' : "Life Vest",
    'site_logo' : "images/logo-letter.png",
    "login_logo" : "images/logo-admin-login.png",
    'copyright' : "Life Vest",
    "navigation_expanded": False,
    "order_with_respect_to": ["auth", 
                              "members", 
                              "schools", "schools.schools",
                              "products", "products.products", "products.CombinationProduct", "products.SetProduct", "products.ProductCategory", "products.ProductSubCategory", 
                              "orders", "orders.orders",
                              "cart", "cart.cart",
                              "discounts",
                              "management",
                              "support",
                              "warehouse",
                            ],
    "hide_apps": [ "sites", "flatpages", "redirects", "wagtailredirects", "wagtailforms", "wagtailusers", "wagtailsites", "wagtailsearch", "wagtailimages", "wagtaildocs", "wagtailcore", "taggit", "modelcluster", "wagtailadmin", "wagtail"],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.Group": "fas fa-users",
        "members": "fas fa-users",
        "members.member": "fas fa-user",
        
        "products": "fas fa-bread-slice",
        "products.products": "fas fa-bread-slice",
        "products.CombinationProduct": "fas fa-boxes",
        "products.ProductCategory": "fas fa-columns",
        "products.ProductSubCategory": "fas fa-list-alt",
        "products.SizeBasedStocks": "fas fa-pencil-ruler",
        "products.ProductCategorySizes": "fas fa-ruler",
        "products.ProductPrices": "fas fa-tag",
        "products.SetProduct": "fas fa-book",

        "orders": "fas fa-bars",
        "orders.orders": "fas fa-bars",
        "orders.OrderProducts": "fas fa-grip-horizontal",

        "schools": "fas fa-building",
        "schools.schools": "fas fa-building",
        "schools.SchoolCampus": "far fa-building",

        "cart": "fas fa-shopping-basket",
        "cart.cart": "fas fa-shopping-basket",
        "cart.cartitems": "fas fa-grip-horizontal",

        "discounts": "fas fa-percent",
        "discounts.SpecialDiscount": "fas fa-percent",
        "discounts.DiscountCoupon": "fas fa-tag",
    },
    # "custom_links": {
    #     "management": [{
    #         "name": "Ödeme Ayarları",
    #         "url": "paymentgateways",
    #         "icon": "fas fa-comments",
    #         # "permissions": ["orders.add_orders"]
    #     }]
    # },

    # "show_ui_builder": True,
    # "related_modal_active": True,
}

JAZZMIN_UI_TWEAKS = {
    "body_small_text": True,
    "actions_sticky_top": True,
    "sidebar_nav_legacy_style": True,
    "sidebar_fixed": True,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
}

WAGTAILADMIN_BASE_URL = '/cms/'
WAGTAIL_SITE_NAME = "Life Vest"

SITE_ID = 1

AUTH_USER_MODEL = 'members.Member'

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'codeSnippet_theme': 'monokai',
        'toolbar': 'all',
        'extraPlugins': ','.join(
            [
                'codesnippet',
                'widget',
                'dialog',
            ]
        ),
    }
}

LOGIN_REDIRECT_URL = ''
LOGIN_URL = 'user/login'

django_heroku.settings(locals())
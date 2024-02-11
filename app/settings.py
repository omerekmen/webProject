import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "django-insecure-hz4xi_g24stpz13=38w7io%(pqv$-e6dgmfy9hvj*30bhj8f2="

DEBUG = True

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['*', 'https://sandbox-api.iyzipay.com']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'testwebproject@outlook.com'
EMAIL_HOST_PASSWORD = 'WebProjectAdmin.1234'
EMAIL_FROM_ADDRESS = 'testwebproject@outlook.com'
DEFAULT_FROM_EMAIL = 'testwebproject@outlook.com'

# Iyzico Payment Login: Mail: testwebproject@outlook.com ||| Password: 102938 @ https://sandbox-merchant.iyzipay.com/

INSTALLED_APPS = [

    "jazzmin",
    "import_export",
    "django_filters",
    "django_extensions",

    'modelcluster',
    'taggit',

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.contrib.postgres",

    "ckeditor",
    "ckeditor_uploader",

    "school",
    "members",
    "store",
    "products",
    "orders",
    "cart",
    "payment",
    "coupons",
    "support",
    "warehouse",
    "cargo",
    "reports",
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

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'app.context_processors.default',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = "app.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}



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

LANGUAGE_CODE = "tr-tr"
TIME_ZONE = "Europe/Istanbul"
USE_I18N = True
USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


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
    "hide_apps": [ "sites", "flatpages", "redirects", "taggit", "modelcluster", ],
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

SITE_ID = 1

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
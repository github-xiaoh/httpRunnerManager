"""
Django settings for HttpRunnerManager project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
from __future__ import absolute_import, unicode_literals

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import djcelery
from django.conf.global_settings import SESSION_COOKIE_AGE

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=w+1if4no=o&6!la#5j)3wsu%k@$)6bf+@3=i0h!5)h9h)$*s7'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = ['*',"10.1.111.29",'192.168.44.4']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ApiManager',
    'djcelery', # 定时任务和异步执行
    # 'testTools',
    # 'sc_pay',
    'user_ch',
    'AutoApiTest',
    'corsheaders', # 解决跨域问题App
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # 跨域配置

]

MIDDLEWARE_CLASSES = [
    'dwebsocket.middleware.WebSocketMiddleware'
]

WEBSOCKET_ACCEPT_ALL = True

ROOT_URLCONF = 'HttpRunnerManager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'HttpRunnerManager.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'httprunnermanager',  # 新建数据库名
            'USER': 'root',  # 数据库登录名
            'PASSWORD': 'root123456',  # 数据库登录密码
            'HOST': '127.0.0.1',  # 数据库所在服务器ip地址
            'PORT': '3306',  # 监听端口 默认3306即可
        },
        # 'db1': {
        #     'ENGINE': 'django.db.backends.mysql',
        #     'NAME': 'sc_cms',
        #     'USER': 'java_test',
        #     'PASSWORD': 'xp6oMxo)0$Aji2ui',
        #     'HOST': 'fjnyef-test.cv7bku39ibuj.us-east-1.rds.amazonaws.com',
        #     'PORT': '3306',
        # },
        # 'db2': {
        #     'ENGINE': 'django.db.backends.mysql',
        #     'NAME': 'sc_pay',
        #     'USER': 'java_test',
        #     'PASSWORD': 'xp6oMxo)0$Aji2ui',
        #     'HOST': 'fjnyef-test.cv7bku39ibuj.us-east-1.rds.amazonaws.com',
        #     'PORT': '3306',
        # },
        'sc_cms_ch': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'sc_cms',
            'USER': 'java_test',
            'PASSWORD': 'xp6oMxo)0$Aji2ui',
            'HOST': 'rm-2ze04c849v9m32bzj.mysql.rds.aliyuncs.com',
            'PORT': '3306',
        },
        'auto_api_test': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'cmsplatform',  # 新建数据库名
            'USER': 'root',  # 数据库登录名
            'PASSWORD': 'root123456',  # 数据库登录密码
            'HOST': '127.0.0.1',  # 数据库所在服务器ip地址
            'PORT': '3306',  # 监听端口 默认3306即可
        },
    }
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),  # 静态文件额外目录
    )


else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'httprunnermanager',  # 新建数据库名
            'USER': 'root',  # 数据库登录名
            'PASSWORD': 'root123456',  # 数据库登录密码
            'HOST': '127.0.0.1',  # 数据库所在服务器ip地址
            'PORT': '3306',  # 监听端口 默认3306即可
        }
    }
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')


#配置多数据源使用
# use multi-database in django
# add by WeizhongTu
DATABASE_ROUTERS = ['HttpRunnerManager.database_router.DatabaseAppsRouter']
DATABASE_APPS_MAPPING = {
    # example:
    #'app_name':'database_name',
    # 'testTools': 'db1',
    # 'sc_pay': 'db2',
    'user_ch': 'sc_cms_ch',
    'AutoApiTest':'auto_api_test'
}



STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

SESSION_COOKIE_AGE = 300 * 60


# 可以理解为自动查找我们定义的task
djcelery.setup_loader()

CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = 'Asia/Shanghai'  # celery 时区
BROKER_URL = 'amqp://guest:guest@127.0.0.1:5672//' if DEBUG else 'amqp://guest:guest@127.0.0.1:5672//' # 任务容器地址，rabbitMQ地址
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'  # celey处理器，固定写法
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend' # celery结果返回，可用于跟踪结果
# celery内容等消息的格式设置
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_TASK_RESULT_EXPIRES = 7200  # celery任务执行结果的超时时间，
CELERYD_CONCURRENCY = 1 if DEBUG else 10 # celery worker的并发数 也是命令行-c指定的数目 根据服务器配置实际更改 一般25即可
CELERYD_MAX_TASKS_PER_CHILD = 100  # 每个worker执行了多少任务就会死掉，我建议数量可以大一些，比如200


EMAIL_SEND_USERNAME = '443990096@qq.com'  # 定时任务报告发送邮箱，支持163,qq,sina,企业qq邮箱等，注意需要开通smtp服务
EMAIL_SEND_PASSWORD = 'btsfupcotihybhhj'     # 邮箱密码


# 解决跨越问题
# 配置白名单或者全部允许

# 全部允许配置
CORS_ORIGIN_ALLOW_ALL = True
# 白名单配置
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:8081',
    'http://localhost:8081',
    'http://0.0.0.0:8081',
    'http://192.168.44.4:8081'
)
# 允许cookie
CORS_ALLOW_CREDENTIALS = True  # 指明在跨域访问中，后端是否支持对cookie的操作

# 允许的请求方式
CORS_ALLOW_METHODS = (
 'DELETE',
 'GET',
 'OPTIONS',
 'PATCH',
 'POST',
 'PUT',
 'VIEW',
)
# 允许的请求头
CORS_ALLOW_HEADERS = (
 'XMLHttpRequest',
 'X_FILENAME',
 'accept-encoding',
 'authorization',
 'content-type',
 'dnt',
 'origin',
 'user-agent',
 'x-csrftoken',
 'x-requested-with',
 'Pragma',
)




LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
        # 日志格式
    },
    'filters': {
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/all.log'),
            # 'maxBytes': 1024 * 1024 * 100,
            'backupCount': 5,
            'formatter': 'standard',
            'when': 'midnight',
            'interval': 1,
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/script.log'),
            # 'maxBytes': 1024 * 1024 * 100,
            'backupCount': 5,
            'formatter': 'standard',
            'when': 'midnight',
            'interval': 1,
        },
        'scprits_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/script.log'),
            # 'maxBytes': 1024 * 1024 * 100,
            'backupCount': 5,
            'formatter': 'standard',
            'when': 'midnight',
            'interval': 1,
        },

        'test_tools': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/script.log'),
            # 'maxBytes': 1024 * 1024 * 100,
            'backupCount': 5,
            'formatter': 'standard',
            'when': 'midnight',
            'interval': 1,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': True
        },
        'HttpRunnerManager.app': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': True
        },
        'HttpRunnerManager': {
            'handlers': ['scprits_handler', 'console'],
            'level': 'DEBUG',
            'propagate': True
        },
        'scripts': {
            'handlers': ['scprits_handler', 'console'],
            'level': 'DEBUG',
            'propagate': True
        },

        'testTools': {
            'handlers': ['test_tools', 'console'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}




import os
import sys

MONGO_DATABASE_HOST = os.environ.get("MONGO_HOST")
MONGO_DATABASE_PORT = os.environ.get("MONGO_PORT")
MONGO_DATABASE_USER = os.environ.get("MONGO_INITDB_ROOT_USERNAME")
MONGO_DATABASE_PASSWORD = os.environ.get("MONGO_INITDB_ROOT_PASSWORD")
MONGO_DATABASE_NAME = os.environ.get("MONGO_DB")
MONGO_TEST_DATABASE_NAME = "testing_db"

if "test" in sys.argv:
    MONGO_DATABASE_NAME = MONGO_TEST_DATABASE_NAME

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    }
}

from django.conf import settings
from pymongo import MongoClient


def get_db_handle():
    client = MongoClient(
        host=settings.MONGO_DATABASE_HOST,
        port=int(settings.MONGO_DATABASE_PORT),
        username=settings.MONGO_DATABASE_USER,
        password=settings.MONGO_DATABASE_PASSWORD,
    )
    return client[settings.MONGO_DATABASE_NAME]

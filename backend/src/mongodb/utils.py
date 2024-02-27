from typing import Annotated

from bson import ObjectId
from django.conf import settings
from django.http import Http404
from pydantic import BaseModel, BeforeValidator, ValidationError

from src.mongodb.mongo import get_db_handle, get_mongo_client

# Represents an ObjectId field in the database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]


class MongoTestTearDown:
    """
    APITestCase tearDown mixin, ensures mongodb test database teardown between tests
    Will drop instances created in setUpTestData method!
    """

    def tearDown(self):
        super().tearDown()
        get_mongo_client().drop_database(settings.MONGO_TEST_DATABASE_NAME)


class MongoViewSetMixin:
    def _get_collection(self):
        return self.model.get_collection()

    def get_queryset(self):
        assert (
            isinstance(self.model, BaseModel),
            "queryset has to inherit pydantic BaseModel",
        )
        if self.filter_backends:
            raise NotImplementedError("filter_backend not supported for mongo models")
        return self._get_collection().find()

    def get_object(self):
        instance_data = self.model.get_collection().find_one(
            ObjectId(self.kwargs["pk"])
        )
        if instance_data:
            return self.model(**instance_data)
        raise Http404("Instance not found")


class PyMongoModelMixin:
    """
    Handles pydantic.BaseModel integration with pymongo collections
    """

    @property
    def collection(self):
        return self.get_collection()

    @classmethod
    def get_collection(cls):
        return get_db_handle()[cls.Config.collection_name]

    def save(self):
        data = self.dict()
        if not self.id:
            data.pop("id")

        result = self.collection.insert_one(data)
        self.id = str(result.inserted_id)

    def get_object(self):
        return self.collection.find_one({"_id": ObjectId(self.id)})

    def refresh(self):
        if self.id:
            result = self.get_object()
            for key, value in result.items():
                setattr(self, key, value)

    def update(self, data):
        if not self.id:
            return

        if any(key in data for key in ("id", "_id")):
            raise ValidationError("Can't update _id/id value")

        result = self.collection.update_one({"_id": ObjectId(self.id)}, {"$set": data})

        if result.acknowledged:
            for key, value in data.items():
                setattr(self, key, value)

    def delete(self):
        if self.id:
            self.collection.delete_one({"_id": ObjectId(self.id)})

# coding=utf-8

from .base import Base

class User(BaseModel):

    class Meta:
        db_table = "sp_user"

    username = CharField()
    password = CharField()
    joined_at = DateTime()



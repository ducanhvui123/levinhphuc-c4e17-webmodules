from mongoengine import *

class Customer(Document):
    name = StringField()
    gender = IntField()
    address = StringField()
    email = StringField()
    phone = StringField()
    job = StringField()
    company = StringField()
    contacted = BooleanField()
    measurements = ListField()

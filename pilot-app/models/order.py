from mongoengine import *

class Order(Document):
    customer_name = StringField()
    customer_user = StringField()
    time = DateTimeField()
    is_accepted = BooleanField()
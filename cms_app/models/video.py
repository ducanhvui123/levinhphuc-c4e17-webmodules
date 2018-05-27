from mongoengine import *

class Video(Document):
    title = StringField()
    thumbnail = StringField()
    views =  IntField()
    youtube_id = StringField()
    link = StringField()

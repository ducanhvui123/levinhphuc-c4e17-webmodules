import mongoengine 
# mongodb://<dbuser>:<dbpassword>@ds033996.mlab.com:33996/youtube
host = "ds033996.mlab.com"
port = 33996
db_name = "youtube"
user_name = "admin"
password = "admin"



def connect():
    mongoengine.connect(db_name, host=host, port=port,
                        username=user_name, password=password)


def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
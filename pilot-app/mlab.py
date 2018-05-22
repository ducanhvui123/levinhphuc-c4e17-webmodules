import mongoengine

# mongodb://<dbuser>:< dbpassword >@ds119820.mlab.com:19820/muadongkhonglanhc4e17

host = "ds119820.mlab.com"
port = 19820
db_name = "muadongkhonglanhc4e17"
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
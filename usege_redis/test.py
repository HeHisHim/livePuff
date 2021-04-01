import pymongo


uri = "mongodb://root:Ricemap123@192.168.10.14:27017,192.168.10.15:27017,192.168.10.18:27017/private_fund?replicaSet=replica1&authSource=admin"

class Mongo:
    def __init__(self, uri, db_name, **kwargs):
        self.uri = uri
        self.db_name = db_name
        self.client: pymongo.MongoClient = None
        self.database: pymongo.Database = None
        self.kwargs: dict = kwargs
        self.init_app(self.uri, self.db_name, **kwargs)
    
    def init_app(self, uri, db_name, **kwargs):
        self.client = pymongo.MongoClient(self.uri, **self.kwargs)
        self.database = self.client.get_database(self.db_name, write_concern=pymongo.WriteConcern(w="majority"))

    def get_initialized_collection(self, collection_name):
        return self.database.get_collection(collection_name)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
        self.client = None
        print(self.client)

    
if "__main__" == __name__:
    mongo = Mongo(uri, "private_fund")

    # print(mongo.get_initialized_collection("net_value").find_one())
    with mongo as cursor:
        print(cursor.get_initialized_collection("net_value").find_one())
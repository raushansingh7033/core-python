class Database:

    _instance = None

    def __init__(self):
        if Database._instance is not None:
            raise Exception("Only one object allowed")
        else:
            Database._instance = self


db1 = Database()
db2 = Database()
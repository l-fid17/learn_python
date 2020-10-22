class Database:
    content = {"users": []} # class variable

    @classmethod
    def insert(cls, data):
        Database.content["users"].append(data)

    @classmethod
    def remove(cls, finder): # lambda x: x["username"] != "something"
        cls.content["users"] = [user for user in cls.content["users"] if not finder(user)]

    @classmethod
    def find(cls, finder): # lambda x: x["username"] == "something"
        return [user for user in cls.content["users"] if finder(user)]
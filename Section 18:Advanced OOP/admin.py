from user import User
# from db import Database
from saveable import Saveable

class Admin(User, Saveable):
    def __init__(self, username, password, access):
        super(Admin, self).__init__(username, password)
        self.access = access

    def __repr__(self):
        return f"<Admin {self.username}, access {self.access}>"

    def to_dict(self):
        return {
            "username": self. username,
            "password": self.password,
            "access": self.access
        }

    # def save(self):         # # this method is the same as Admin.save() (admin.py)
    #     Database.insert(self.to_dict())


"""
two ways of solving the above
"""
# 1. move the code in the User class (user.py)
# however Store (store.py) does not inherit from the class User

# 2. have another class. see (saveable.py)
# and we remove the save method plut the db import from this class, as well as from Store
# then import the new class and make Admin extend the new class also


""""""

# self.save() will be searched in Admin
# then in User
# then in Saveable, where it will be found

# self.save() uses self.to_dict()

# self.to_dict() will be searched for in Admin, where it will be found
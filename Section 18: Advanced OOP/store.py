from saveable import Saveable

class Store(Saveable):
    def to_dict(self):
        return {
            "key": "item"
        }

    # def save(self):         # this method is the same as Admin.save() (admin.py)
    #     Database.insert(self.to_dict())


"""
see admin.py
"""
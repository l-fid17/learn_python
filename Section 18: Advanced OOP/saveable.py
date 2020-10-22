from abc import ABCMeta, abstractmethod

from db import Database

class Saveable(metaclass=ABCMeta):
    def save(self):         # # this method is the same as Admin.save() (admin.py)
        Database.insert(self.to_dict())

    @abstractmethod     # forces the class extending this one to implement this method
    def to_dict(self):
        pass


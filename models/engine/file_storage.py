#!/usr/bin/python3
"""Defines a class for file storage"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to JSON and vice-versa"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets the obj with key in __objects"""
        self.__objects["{}.{}".format(obj.__class__.__name__,
            obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        a_dict = {}
        for i,j in self.__objects.items():
            a_dict[i] = j.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(a_dict, f)

    def reload(self):
        """deserializes JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                a_dict = json.load(f)

            for i, j in a_dict.items():
                class_name, obj_id = key.split(",")
                j['__class__'] = class_name
                obj = BaseModel.from_dict(j)
                self.__objects[i] = obj

        except:
            pass

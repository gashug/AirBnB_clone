#!/usr/bin/python3
"""Defines a class BaseModel"""

import uuid
from datetime import datetime


class BaseModel:
    "Represents the base class for all attributes and methods"""

    id: str
    created_at: datetime
    updated_at: datetime

    def __init__(self):
        """Initialize public instance attrubutes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """return string representation of object"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates the current datetime to attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns the dictionary representation of the object"""
        cls_dict = self.__dict__.copy()
        cls_dict['__class__'] = self.__class__.__name__
        cls_dict['created_at'] = self.created_at.isoformat()
        cls_dict['updated_at'] = self.updated_at.isoformat()
        return cls_dict

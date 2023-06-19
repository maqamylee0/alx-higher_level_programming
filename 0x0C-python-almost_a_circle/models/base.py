#!/usr/bin/python3
"""base class"""


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialising instance"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation to a file"""
        list_o = []
        if list_objs is None:
            list_o = []
        else:
            for obj in list_objs:
                list_o.append(obj.to_dictionary())
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            file.write(cls.to_json_string(list_o))

     @staticmethod
     def from_json_string(json_string):
        """changes from json to list"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

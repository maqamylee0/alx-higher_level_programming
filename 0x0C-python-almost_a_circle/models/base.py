#!/usr/bin/python3
"""base class"""


import json



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
    
    @classmethod
    def create(cls, **dictionary):
        """creates a rectangle instance copy"""
        if cls.__name__ == "Rectangle":
            r1 = cls(1, 3, 0, 0, 4)
        else:
            r1 = cls(1, 3, 0, 1)
        r1.update(**dictionary)
        return r1

    def load_from_file(cls):
        """load from file and save instance"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**dictionary) for dic in dictionaries]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save instance to csv file"""
        filename = cls.__name__ + ".csv"
        if list_objs is None:
            list_objs = []
        with open(filename, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            for obj in list_objs:
                csv_writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        """load from csv file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                objs = []
                for row in reader:
                    objx = cls.create_from_csv_row(row)
                    objs.append(objx)
                    return objs
        except FileNotFoundError:
            return []

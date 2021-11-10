import pathlib
import json

class Person:
    def __init__(self, person_map):
        for k,v in person_map.items():
            setattr(k,v)


class Reader:
    def __init__(self, input_file:pathlib.Path):
        self.path = input_file

    def read(self):
        return [Person(i) for i in json.load(self.path.open())]


class Writer:
    def __init__(self, output_file:pathlib.Path):
        self.path = output_file

    def write(self, data):
        json.dump(data, self.path.open(mode = 'w'), indent = 4)
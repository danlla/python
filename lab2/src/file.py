import pathlib
import json
from person import Person


class Reader:
    def __init__(self, input_file: pathlib.Path):
        self.path = input_file

    def read(self):
        return [Person(i) for i in json.load(self.path.open())]


class Writer:
    def __init__(self, output_file: pathlib.Path):
        self.path = output_file

    def write(self, data):
        json.dump([i.__dict__ for i in data], self.path.open(
            mode='w', encoding='windows-1251'), indent=4, ensure_ascii=False)

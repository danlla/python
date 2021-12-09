import pathlib
import json
import pickle
from person import Person


class Reader:
    """
    Класс для чтения файла
    """
    def __init__(self, input_file: pathlib.Path):
        """
        :param:
        input_file: путь к файлу из которого нужно прочитать данные
        """
        self.path = input_file

    def read_j(self) -> list:
        """
        Возращает лист персонов, которые были прочитанны из файла
        """
        return json.load(open(self.path))

    def read_p(self) -> list:
        """
        Возращает лист персонов, которые были прочитанны из файла
        """
        return [Person(i) for i in pickle.load(open(self.path, 'rb'), encoding='windows-1251')]


class Writer:
    """
    Класс для записи в файл
    """
    def __init__(self, output_file: pathlib.Path):
        """
        :param:
        output_file: путь к файлу в который нужно записать данные
        """
        self.path = output_file

    def write_p(self, data):
        """
        Записывает данные в файл
        :param:
        data: данные которые нужно записать
        """
        pickle.dump(data, open(self.path, 'wb'))

import pathlib
import json
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

    def read(self) -> list:
        """
        Возращает лист персонов, которые были прочитанны из файла
        """
        return [Person(i) for i in json.load(self.path.open())]


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

    def write(self, data):
        """
        Записывает данные в файл
        :param:
        data: данные которые нужно записать
        """
        json.dump([i.__dict__ for i in data], self.path.open(
            mode='w', encoding='windows-1251'), indent=4, ensure_ascii=False)

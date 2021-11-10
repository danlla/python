class Person:
    """
    Класс оболочка для записи из файла
    """
    def __init__(self, person_map):
        """
        :param:
        person_map: мапа с данными
        """
        for k, v in person_map.items():
            setattr(self, k, v)

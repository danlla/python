class Person:
    def __init__(self, person_map):
        for k, v in person_map.items():
            setattr(self, k, v)

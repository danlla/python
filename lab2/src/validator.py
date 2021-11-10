from person import Person
import re
import tqdm


class RegexpPerson:
    def __init__(self):
        self.reg = {
            "telephone": r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$',
            "weight": r'^([1-9]|[1-9][0-9]|[1][0-9][0-9]|200)$',
            "inn": r'^[0-9]{12}$',
            "passport_series": r'^[1-9][0-9]\s[0-9][0-9]$',
            "university": r'^[а-яА-Я-\. ]{1,}$',
            "age": r'^([1-9]|[1-9][0-9]|1[0-2][1-9]|130)$',
            "academic_degree": r'^([а-яА-Я]|-| ){3,}$',
            "worldview": r'^([а-яА-Я]|-| ){3,}$',
            "address": r'^([а-я]|\s|[А-Я]|\.)+\s[1-9][0-9]*[а-я]?$'
        }

    def valid(self, k, v):
        return re.match(self.reg[k], str(v)) is not None


class Validator:
    def __init__(self, data):
        self.data = data
        self.count_err = {}

    def validate(self, reg_exp):
        data_v = []
        with tqdm.tqdm(total=len(self.data), desc='validate...') as bar:
            for i in self.data:
                for k, v in i.__dict__.items():
                    if not reg_exp.valid(k, v):
                        if self.count_err.setdefault(k) is None:
                            self.count_err[k] = 1
                        else:
                            self.count_err[k] += 1
                        break
                else:
                    data_v.append(i)
                bar.update(1)
        return data_v

    def get_count_err(self):
        return self.count_err

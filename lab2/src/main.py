from parser_args import *
from file import Reader, Writer
from validator import *


def main():
    pars = ParserArgs()
    args = pars.get_args()
    reader = Reader(args['input'])
    data = reader.read()
    reg_exp = RegexpPerson()
    validator = Validator(data)
    data_v = validator.validate(reg_exp)
    writer = Writer(args['output'])
    writer.write(data_v)

    print("Count valid notes: {}".format(len(data_v)))
    print("Count invalid notes: {}".format(len(data) - len(data_v)))
    for err, value in validator.get_count_err().items():
        print("Error: {} value:{}".format(err, value))


if __name__ == '__main__':
    main()

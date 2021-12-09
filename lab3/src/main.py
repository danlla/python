from sort import heap_sort
from file import Reader, Writer


def main():
    reader = Reader('data.txt')
    data = reader.read_j()

    heap_sort(data)

    writer = Writer('output.txt')
    writer.write_p(data)

    reader = Reader('output.txt')
    data = reader.read_p()

    for i in data:
        print("telephone: {}\n" 
              "weight: {}\n"
              "inn: {}\n"
              "passport_series: {}\n"
              "university: {}\n"
              "age: {}\n"
              "academic_degree: {}\n"
              "worldview: {}\n"
              "address: {}\n".
              format(i.telephone, i.weight, i.inn, i.passport_series, i.university,
                     i.age, i.academic_degree, i.worldview, i.address))


if __name__ == '__main__':
    main()

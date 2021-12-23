from sort import heap_sort
from file import Reader, Writer
from time import time


def main():
    reader = Reader('C:\\python\\labs\\lab3\\data.txt')
    data = reader.read_j()
    t = time()
    heap_sort(data)
    print(f"Time sort: {time()-t}")
    t = time()
    writer = Writer('C:\\python\\labs\\lab3\\output.txt')
    writer.write_p(data)
    print(f"Time write: {time()-t}")

    reader = Reader('C:\\python\\labs\\lab3\\output.txt')
    data = reader.read_p()

    #for i in data:
    #    print("telephone: {}\n"
    #          "weight: {}\n"
    #          "inn: {}\n"
    #          "passport_series: {}\n"
    #          "university: {}\n"
    #          "age: {}\n"
    #          "academic_degree: {}\n"
    #          "worldview: {}\n"
    #          "address: {}\n".
    #          format(i.telephone, i.weight, i.inn, i.passport_series, i.university,
    #                 i.age, i.academic_degree, i.worldview, i.address))


if __name__ == '__main__':
    main()

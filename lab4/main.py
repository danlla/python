import pandas as pd
from time import time
from multiprocessing import Pool
from matplotlib import pyplot as plt


def min_dead(*data):
    _list = list(data)
    return min(_list)


df = pd.read_csv("data.csv", sep=",", encoding='windows-1251')

if __name__ == "__main__":
    print(len(df.columns))
    df.drop(df[df["Умерли"] < 0].index)

    time_1 = time()
    tms = []
    for i in range(1, 5):
        with Pool(i) as p:
            print(p.apply(min_dead, df["Умерли"].tolist()))
        dif_time = time() - time_1
        tms.append(dif_time)
        print(time() - time_1)
    print(tms)

    fig = plt.figure(figsize=(10, 10))
    plt.ylabel('t')
    plt.xlabel('count')
    plt.title('Зависимость t от count')
    plt.scatter(list(range(1, 5)), tms, color='red', marker='.', linewidths=2, facecolors='red')
    plt.show()

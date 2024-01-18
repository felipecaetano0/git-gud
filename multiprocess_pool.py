from multiprocessing import Pool


def f(x):
    for a in range(x*100000000):
        x ** 2
        # FIXME :: Look htop
    return x**2


if __name__ == "__main__":
    p = Pool(5)
    with p:
        ret = p.map(f, [1, 2, 3])
        for i in ret:
            print(i)

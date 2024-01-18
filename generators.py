
def f(x):
    print('git')
    yield x
    print('gud')


def g(x):
    for y in range(x):
        print('try')
        yield y
        print('hard')


def h(x):
    for y in range(x):
        print('try')
        yield y
        print('harder')
        yield y


if __name__ == "__main__":
    for i in f(666):
        print(i)

    for j in g(3):
        print(j)

    k = 0
    for _ in h(3):
        k += 1
        print(k)

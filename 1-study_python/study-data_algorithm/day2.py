from timeit import Timer


def test1():
    lis = []
    for i in range(10000):
        lis.append(i)


def test2():
    lis = []
    for i in range(10000):
        lis += [i]


def test3():
    lis = [i for i in range(10000)]


def test4():
    lis = list(range(10000))


def test5():
    lis = []
    for i in range(10000):
        lis.extend([i])


def test6():
    lis = []
    for i in range(10000):
        lis = lis + [i]


def test7():
    lis = []
    for i in range(10000):
        lis.insert(-1, i)


if __name__ == '__main__':
    time1 = Timer('test1()', 'from __main__ import test1')
    print(time1.timeit(1000))

    time2 = Timer('test2()', 'from __main__ import test2')
    print(time2.timeit(1000))

    time3 = Timer('test3()', 'from __main__ import test3')
    print(time3.timeit(1000))

    time4 = Timer('test4()', 'from __main__ import test4')
    print(time4.timeit(1000))

    time5 = Timer('test5()', 'from __main__ import test5')
    print(time5.timeit(1000))

    time6 = Timer('from __main__ import test6')
    print(time6.timeit(1000))

    time7 = Timer('from __main__ import test7')
    print(time7.timeit(1000))

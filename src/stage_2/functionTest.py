def zip_test():
    s1 = [1, 2, 3, 4]
    s2 = ['a', 'b', 'c', 'd']
    s3 = list(zip(s1, s2))  # zip   压缩
    s4 = list(zip(*s3))  # zip * 解压
    print("s1:", s1, "s2:", s2, '\n',
          "zip:", s3, '\n', "unzip:", s4)


def map_test():
    a = [1, 2, 3, 4, 5]
    b = map(lambda x: x ** 2, a)
    print(list(b))

    def f1(n):
        return n ** 0.5

    c = map(f1, a)
    print(list(c))

    def f2(x, y):
        return x + y

    d = map(f2, [1, 2, 3], [4, 5, 6])
    print(f2([1, 2, 3], [4, 5, 6]))
    print(list(d))


def reduce_test():
    from functools import reduce
    # 与for 循环相比 更简洁但速度慢
    a = list(range(10))
    b = reduce(lambda x, y: x + y, a)
    print(b)


def filter_test():
    # 过滤序列 以函数的布尔值决定是否保留
    a = list(range(10))
    b = filter(lambda x: x % 2 == 0, a)
    print(a, list(b))


def enumerate_test():
    a = ['a', 'b', 'c']
    for i, j in enumerate(a, 1):
        print(i, ":", j)


zip_test()
map_test()
reduce_test()
filter_test()
enumerate_test()

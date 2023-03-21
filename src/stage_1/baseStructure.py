def condition_test():
    # bool()函数 转换为True False
    # 0 以及 空对象都等价于 False
    print(bool(range(8, 5)))  # 特殊的空range对象


def if_test():
    a = 1
    b = 2
    if a > b:
        print(a)
    elif a == b:
        print(a, b)
    else:
        print(b)


def circulation_test():
    for i in range(10):
        print(i, end=' ')
    else:
        print("end")
    j = 0
    while j < 10:
        print(j, end=" ")
        j += 1
    else:
        print("end")


condition_test()
if_test()
circulation_test()

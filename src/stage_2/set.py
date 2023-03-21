def set_test():
    # 创建等同 与 列表 元组
    # update() 添加元组、列表、集合、字典(key)、range对象等各种序列
    a = {1, 2, 3}
    b = range(11, 14)
    a.update(b)
    print(a)
    # discard() 丢弃指定元素
    a.discard(11)
    print(a)

    a = {1, 2, 3, 4, 5}
    b = {1, 3, 5, 7, 9}
    # &交集合 |并集  -差集 ^对称差集
    # 差集的前后顺序会影响结果
    print('&:', a & b, '|:', a | b, '-:', a - b, '反-:', b - a, '^:',
          a ^ b, sep='\n')


set_test()

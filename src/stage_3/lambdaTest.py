def lambda_test():
    f = lambda x, y: x + y  # 此处直接使用def 创建函数即可 无须lambda函数
    a = f(3, 4)
    print(a)

    # 在 map 函数中应用：
    x = map(lambda p, q: p + q, [1, 2, 3], [4, 5, 6])
    print(list(x))


lambda_test()

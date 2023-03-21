def tuple_test():
    # 创建 转换
    t1 = (1, 2, 3)
    t2 = tuple((1, 2, 3))  # 双括号
    l1 = [1, 2, 3]
    t3 = tuple(l1)
    print(t1, t2, t3)

    # 单元素元组
    t_single_wrong = (1)
    t_single = (1,)  # 不加逗号则 t_single 为 int
    print(type(t_single_wrong), type(t_single))

    # 其余等同于列表


tuple_test()

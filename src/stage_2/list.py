def list_test():
    # 创建方式：弱数据类型；list()函数
    list_1 = [1, 2, 3, 4, 5]
    list_2 = list([1, 2, 3, 4, 5])
    print(list_1, list_2)

    # range(begin, end, step)的应用 生成[begin,end) 公差为step 的 序列
    list_3 = list(range(1, 10))
    list_4 = list(range(1, 10, 2))
    list_5 = list(range(10, 0, -1))
    print(list_3, list_4, list_5)

    # 访问方法： 下标法  循环遍历
    print("访问")
    list_6 = list(range(1, 11))
    print(list_6[0], list_6[9])
    for i in range(len(list_6)):
        print(list_6[i])
    index = 0
    while index < len(list_6):
        print(list_6[index])
        index += 1

    # 分片法同字符串

    # 方法
    list_f = list(range(1, 10))
    # .append(new_element) 增添元素 .insert(index, new_element) 增添元素
    print("原来", list_f)
    list_f.append(10)
    print("append后", list_f)
    list_f.insert(0, 0)
    print("在0处插入0后", list_f)

    # .pop(index) 删除元素 count(target) 对指定元素计数
    list_f.pop(0)
    print("删除0处元素后", list_f)
    print("[0, 0, 0, 3, 4, 5]中0的个数:", [0, 0, 0, 3, 4, 5].count(0))

    # .extend(new_list)合并 并且改变操作对象  +运算符生成新列表
    list_m = [1, 2, 3]
    list_n = [4, 5]
    print(list_m + list_n, list_m, "没有改变list_m")
    list_m.extend(list_n)
    print(list_m, "改变list_m")

    # .index(target) 检索第一个目标元素的索引值
    print([1, 2, 3, 4, 5].index(4), "存在")

    # .remove(target) 不存在报错 只删除第一个
    list_f = [1, 2, 3, 2]
    list_f.remove(2)
    print(list_f)

    # .sort()排序 类型不可混   .reverse()翻转
    list_f = [9, 3, 6, 3, 2, 6, 8]
    list_m = ['a', 't', 's', 'p', 'a']
    list_f.sort()
    list_m.sort()
    print(list_f)
    print(list_m)
    list_m.reverse()
    print(list_m)

    # .clear() 清空元素
    list_f.clear()
    print(list_f)

    # .copy() 浅拷贝
    list_m = [1, 2, [3, 4]]
    list_n = list_m.copy()
    print(list_n)
    list_n[2][0] = 4
    print(list_m)

    # in   not in   is   is not
    print(2 in [1, 2, 3])
    print(2 not in [1, 2, 3])
    print([1, 2] is [1, 2])
    list_p = [1, 2]
    list_m = list_p.copy()
    print(list_m is list_p)
    list_m = list_p
    print(list_m is list_p)

    # 迭代器 for in
    list_1 = list(x**2 for x in range(1, 10, 2))
    print(list_1)
    list_2 = list(x.title() for x in ('sam', 'bake'))
    print(list_2)


list_test()

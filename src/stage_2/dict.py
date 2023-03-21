def dict_test():
    # dict()函数接受zip对象
    x = dict(zip([1, 2, 3], [4, 5, 6]))
    print(x)
    # 基本操作：
    dic1 = {"name": "Amy", "age": 30, "trash": '#￥%#@'}
    # 增加元素：
    dic1["gender"] = "female"
    print(dic1)
    # 删除：
    del dic1["trash"]
    print(dic1)
    # keys() 返回全部key 作为列表
    # values() 返回包含有value 的列表
    # items() 返回包含有(key,value) 的列表


dict_test()

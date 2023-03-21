def string_test():
    str1 = "abcdefghijk"
    str2 = "123456789"
    str3 = str(list(range(10)))

    print(str3)
    # 从0开始（反向-1） 截取时留头去尾
    # 用法： str[begin: end: step] 截取[begin,end)的字符串，间隔为step（不写默认为1，方向正）
    # step < 0则反向截取
    print('截取', str1[2:6], str1[2:8:2])
    print('拼接', str1 + ' ' + str2)
    print('重复', (str1[2:6] + ' ') * 3)
    print('[2:6]长度', len(str1[2:6]))
    print('反向截取', str2[-1:-4:-1])

    # src_str.find(target_str)方法 在源字符串查找另一个子串 返回首字符的索引
    # 查找不到返回 -1
    src_str = "0123456789"
    target_str = "456"
    print(src_str.find(target_str))

    # src_str.replace(old_str,new_str) 替换字符串，返回新串
    old_str = "456"
    new_str = "555"
    print(src_str.replace(old_str, new_str))

    # src_str.split(separator) 以给定的separator分割字符串,默认为空格（制表符、换行）
    src_str1 = "1/2/3/4/5"
    print(src_str1.split('/'))

    # len()方法 空格也算长度
    print('len of "89238 98287" =', len("89238 98287"))

    # str.upper() str.lower() str.title()
    print("abcde".upper(), "ABCDE".lower(), "title".title())

    # src_str.strip(target_char) 去除两侧指定字符 （默认空格）
    print(" abcbchjbja ".strip(' ab'))


string_test()

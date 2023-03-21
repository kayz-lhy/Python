def factorfunc():
    facs = []
    n = 23976

    def factors(num):  # 递归函数不使用默认值参数
        for i in range(2, int(num ** 0.5) + 1):  # 只在[2,√2+1)范围内寻找因子以节省时间空间
            # print(i)  # 调试代码
            if num % i == 0:  # 当i是因子时
                facs.append(i)
                # print('x')
                factors(num // i)
                # print('y')
                break  # 防止继续完成之前的循环
        else:
            facs.append(num)
        return facs

    # 先将facs列表中的元素转换为字符串元素，再拼接为要打印的字符串
    result = '*'.join(map(str, factors(n)))
    if n == eval(result):  # 判断结果是否正确
        print(n, '= ' + result)


factorfunc()

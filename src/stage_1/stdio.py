def stdio():
    x = input('please input a string:')
    # 得到的一定是字符串
    # 必要时可以使用int() eval()等函数转换
    y = int(input('please input an int:'))

    fp = open('testOutput.txt', 'a')
    print(1, 2, 3, 4, 5, sep=' ', end=' ', file=fp, flush=True)
    fp.close()
    # 格式化输出
    print("%s is %d" % (x, y))


stdio()

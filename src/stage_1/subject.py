"""
常量与变量:
1.变量名：必须以字母、汉字、下划线开头；不可有空格、标点；大小写敏感；
2.整数、实数、复数：
3.二进制以0b开头，八进制以0o开头，十六进制以0x开头；
"""


def subject_test():
    a = b = 1
    c = 2.5
    d = 3.5
    e = 0b110111
    f = 0o17
    g = 0xaf
    h = 3 + 2j

    # 比较两实数
    print(3.5 == 3.51 - 0.01)
    print(abs(3.5 - (4.5 - 1.0)) < 1e-6)
    from math import isclose
    print(isclose(0.4 - 0.1, 0.3))

    # 复数相关运算
    print('模', abs(h))
    print('虚部', h.imag)
    print('实部', h.real)
    print('共轭复数', h.conjugate())
    print('原数与共轭复数和与积', h + h.conjugate(), h * h.conjugate())
    # 数字可以加下划线 不可连续 不可头尾
    print(1234_343_353_363, 12_123_455.566, 34_555 + 45_666j)
    print('end')


subject_test()

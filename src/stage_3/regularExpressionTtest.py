import re


def main_test():
    import re
    # *[0,inf)
    print(re.match('a*', 'testasdteaaast'))
    print(re.match('a*', 'aaaatestasdteaaast'))
    # +[1,inf)
    print(re.match('a+', 'testasdteaaast'))
    print(re.match('a+', 'aaaaatestasdteaaast'))
    # ? 0 or 1
    print(re.match('a?', 'testasdteaaast'))
    print(re.match('a?', 'atestasdteaaast'))
    print(re.match('a?', 'aaaatestasdteaaast'))
    # {m} m次 {m,} 至少m次 {m,n} [m,n]
    print(re.match('a{2,5}', 'atestasdteaaast'))
    print(re.match('a{2,5}', 'aaatestasdteaaast'))


def phone_num(n):
    if re.match('1[356789]\d{9}', str(n)):
        print('valid!')
    else:
        print('invalid number')


main_test()
phone_num(13455556789)

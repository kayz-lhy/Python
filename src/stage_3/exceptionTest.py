def exception_test(a, b):
    try:
        x = a // b
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except TypeError:
        print('Must be int')
    # finally:
    #    print('The result is:')

    else:
        print(x)

    assert a != b


if __name__ == '__main__':
    exception_test(2, 1)
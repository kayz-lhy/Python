def re(x: int) -> int:
    s = list(str(abs(x)))
    s.reverse()
    y = int(''.join(s))
    if -2 ** 31 < y < 2 ** 31 - 1:
        return -y if x < 0 else y
    else:
        return 0


print(re(239846923))

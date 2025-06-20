#wap to coonvert given decimal ti minary


def binary(n):
    res = 0
    unit = 1
    while n>0:
        rem = n%2
        res += rem * unit
        unit *= 10
        n //= 2
return res
l

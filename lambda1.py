sqr = lambda n: n**2
print(list(map (sqr, range(1,6))))

even = []
odd = []
even_odd = lambda n:even.append(n) if n% 2== 0 else odd.append(n)
list(map(even_odd,range(1,11)))
print(even, odd)


def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print(list(map(factorial, range(1,6))))


def prime(n):
    flag = True
    for i in range(2, n):
        if n% i == 0:
            flag = False
            break
        if flag:
            return n
print(list(filter(prime, range(1,51))))

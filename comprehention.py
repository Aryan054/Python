def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f
l =[ i if i%3 == 0 else fact(i) for i in range(1,7)]
print(l)

l = ['hello', 'racer', 'malayalam', 'python']
vow = [j for s in l for j in s if j  in 'aeiouAEIOU']
print(vow)

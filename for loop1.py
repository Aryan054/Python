# i/ p = s = 'ApPlE'
#o/p = {'A': 'a', 'p': 'P', 'P': 'p', 'l': 'L', 'E': 'e'}
'''s = 'ApPlE'
i = 0
res = {}
while i < len(s):
    if 'A'<=s[i]<='Z':
        res[s[i]] = chr(ord(s[i])+32)
    elif'a'<=s[i]<='z':
         res[s[i]] = chr(ord(s[i])-32)
    i += 1
print(res)

# Multiplication table 
print("Multiplication table of")
a = int(input())
for i in range(1,11):
    print(a,"X",i,"=",a*i)

# Armstrong Number Print
n = int(input("Enetr an integer: "))
i = n
res = 0
while i > 0:
    rem = i % 10
    res += rem ** len(str(n))
    i //= 10
if res == n:
    print('Armstrong')
else:
    print('weakarm')

'''
'''
# To find vowels
l = [1,2.3,2+3j,True,'Program','Python','Yuvraj']
res = ''
for i in l:
    if type(i) == str:
        for j in i:
            if j not in 'AEIOUaeiou':
                res += j
print(res)
'''

# l = [1, 2.3, 'Python', 'Yuvraj', 3+2j]
# out = [ 'program', 'prgrm', 'Yuvraj','Yvrj']

l = [1, 2.3, 'Python', 'Yuvraj', 3+2j]
res = {}
s = ''
for i in l:
    if type(i) == str:
        for j in i:
            if j not in 'AEIOUaeiou':
                s+=j
                res[i] = s
print(res)
                


'''for i in range(5):
    print('*')
    '''
# All Are Known as Solid Patterns

# primary diagonal
'''
for i in range(5):
    for j in range(5):
        print('*', end =' ')
    print()
'''
'''
for i in range(5):
    for j in range (5):
        if i == j:
            print('*', end=' ')
        else:
            print(' ', end =' ')
    print()
'''
'''
for i in range(5):
    for j in range(5):
        if i>j:
            print('*', end =' ')
        else:
            print(' ', end=' ')
    print();
'''
'''
for i in range(5):
    for j in range(5):
        if i < j:
            print('*', end=' ')
        else:
            print(' ', end = ' ')
    print()
'''

# Secondary diagonal
'''
n = 5
for i in range(n+1):
    for j in range(n+1):
        if i+j == n+1:
           print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
        
'''
'''

n = 5
for i in range(n+1):
    for j in range(n+1):
        if i+j > n+1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
print()
'''
'''
n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j < n+1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''
#primary and secondary diagonal Mixture
'''
n = 5
for i in range( 1, n+1):
    for j in range( 1, n+1):
        if i==j :
            print('*', end=' ')
        elif  i+j == n+1:
            print('*', end=' ')
        else:
            print(' ', end = '')
    print()
''

n = 5
for i in range(1, 5+1):
    for j in range(1, 5+1):
        if i==j or i+j == n+1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''
# Hallow Pattern
'''
n =10
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==1 or i==n or j==1 or j==n:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''
'''
n = 10
for i in range(1,n+1):
    for j in range(1, n+1):
        if i==1 or i==n or j==1 or j==n or i==j or i+j == n+1:
            print('*' , end=' ')
        else:
            print(' ', end= ' ')
    print()
'''
'''
n = 9
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==1 or i==n or j==1 or j==n or i==5 or j==5 or i+j==n+1 or i==j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''
# DYnamically Typed Pattern
'''
n = 9
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==1 or i==n or j==1 or j==n or i==n//2+1 or j==n//2+1 or i+j==n+1 or i==j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''
'''
p = 5
s = 9

for i in range(1, p+1):
    for j in range(1, s+1):
        if i==5 or i+j==5+1 or i+4==j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

n = int(input())
c = (n*2)-1
for i in range(1, n+1):
    for j in range(1, c+1):
        if i==5 or i+j==n+1 or j-1==n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''
'''
n = int(input("enter int:"))
k = 0
for i in range(1,n+1):
        for j in range(1, n+1):
            print(k,end=' ')
            k+=1
        print()
'''
'''
n = 5
k = 0
for i in range(1,n+1):
    for j in range(1, n-1):
        print(i,j,end=' ')
    print()
 '''

n = 5  # Height of the letter "D"

for i in range(1, n+1):
    for j in range(1, n+1):
        if j==3 :
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

        
n = 5
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==3 or j==3  or j==5-1  :
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
print()

n = 5
for i in range(1, n+1):
    
    for j in range(1, n-1):
        
        if j==1 or i%j==0 or i==3:
            
            print('*', end=' ')
    
        else:
            print(' ',end=' ')
    
    print()


n= 5
for i in range(1, n+1):
    for j in range(1, n+1):
        if j==1 or j==n or i==j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

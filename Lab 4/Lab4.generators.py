"""N = int(input())
a = (elem**2 for elem in range(1,N))
for i in a:
    print(i)"""



"""n = int(input())
a = (elem for elem in range(n) if elem%2==0)
for i in a:
    print(i, end = ", ")"""



"""def genf():
    for elem in range(1,n):
        if elem%3==0 and elem%4==0:
            yield elem
n = int(input())
for i in genf():
    print(i)"""



"""def squares():
    for elem in range(a,b):
        yield elem**2
a = int(input())
b = int(input())
for i in squares():
    print(i)"""
        


"""def genf():
    for elem in range(n+1):
        yield n-elem
n = int(input())
for i in genf():
    print(i, end = " ")"""


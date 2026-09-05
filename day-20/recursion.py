'''def display(n):
    if n>10:
        return
    print(n)
    display(n+1)

display(1)
'''

'''def display(n):
    if n>10:
        return
    display(n+1)
    print(n)

display(1)
'''
'''def displaysum(n):
    if n==0:
        return 0
    return n+displaysum(n-1)

    
print(displaysum(8))
'''

'''def productofn(n):
    if n==1:
        return 1
    return n*productofn(n-1)

    
print(productofn(5))
'''
'''
def display(ind):
    if ind == len(s):
        return 
    display(ind+1)
    print(s[ind],end='')

s = 'python programming'
display(0)
'''

'''
def display(ind):
    if ind == len(s):
        return 
    display(ind+3)
    print(s[ind],end='')

s = 'python'
display(3)
'''

'''
def display(n):
    if n > len(s):
        return
    print(s[:n])
    display(n+1)

s = 'python programming'
display(1)
'''
'''def display(n):
    if n > len(s):
        return
    print(s[:n])
    display(n+5)

s = 'python'
display(3)
'''

'''
def display(ind,w):
    if ind > len(s)-w:
        return
    print(s[ind:ind+w])
    display(ind+1,w)

s = 'python programming'
display(0,10)
'''

'''
def display(n):
    if n==0:
        return

    display(n//10)
    print(n%10)

n = 987654
display(n)
'''

'''
a = 0
b = 1

n =10
for i in range(n-1):
'''

   


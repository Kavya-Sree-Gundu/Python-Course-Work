Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#int float str list tuple set dict
x=input()
qfcsdgtyrqfue
x
'qfcsdgtyrqfue'
name=input()
kavya
name
'kavya'
name=input('enter your name:")
           
SyntaxError: unterminated string literal (detected at line 1)
name=input("enter your name:")
           
enter your name:panny
name
           
'panny'
age=input("enter thr age:")
           
enter thr age:21
age
           
'21'
age=int(input("enter the age:"))
           
enter the age:21
age
           
21
type(age)
           
<class 'int'>
name=input("enter the names:")
           
enter the names:kavya pavani teju
names
           
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    names
NameError: name 'names' is not defined. Did you mean: 'name'?
names=input("enter the names:")
           
enter the names:kavya pavani teju
names
           
'kavya pavani teju'
names=input("enter the names:").split()
           
enter the names:1 2 3 4 54 5
names
           
['1', '2', '3', '4', '54', '5']
map(int,names)
           
<map object at 0x000001687C2F5F90>
list(map(int,names))
           
[1, 2, 3, 4, 54, 5]
values=list(map(int,input().split()))
           
1 2 34 5 5 6556754
values
           
[1, 2, 34, 5, 5, 6556754]
values=list(map(float,input().split()))
           
1 2 3454 5463.23
values
           
[1.0, 2.0, 3454.0, 5463.23]
names=tuple(input("enter the names:").split()))
SyntaxError: unmatched ')'
names=tuple(input("enter the names:").split())
enter the names:kavya ankitha anvi
names
('kavya', 'ankitha', 'anvi')
values=tuple(map(float,input().split()))
567 5678 567
values
(567.0, 5678.0, 567.0)
names=set(input().split())
ytuio tyui tyu
names
{'ytuio', 'tyui', 'tyu'}
values=set(map(int,input().split()))
1244
values
{1244}
1 2 3 4
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a,b=[1,2]
A
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    A
NameError: name 'A' is not defined. Did you mean: 'a'?
a
1
b
2
a,b=(1,2)
a
1
b
2
email,password=input("enter the emial and passwors:").split()
enter the emial and passwors:kavyasree9023@gmail.com
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    email,password=input("enter the emial and passwors:").split()
ValueError: not enough values to unpack (expected 2, got 1)
email,password=input("enter the emial and password:").split()
enter the emial and password:kavyasree9023@gmail.com
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    email,password=input("enter the emial and password:").split()
ValueError: not enough values to unpack (expected 2, got 1)


email,password=input("enter the emial and password:").split()
enter the emial and password:kavyasree@gmail.com and kavya@123
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    email,password=input("enter the emial and password:").split()
ValueError: too many values to unpack (expected 2)
email,password=input("enter the email and password:").split()
enter the email and password:kavya@123gmail.com kavya123
email,password
('kavya@123gmail.com', 'kavya123')
('kavya@123gmail.com', 'kavya123')
('kavya@123gmail.com', 'kavya123')
a,b,c=list(map(int,input().split()))
1 2 3
q
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    q
NameError: name 'q' is not defined
a
1
b
2
2
2
c
3
name,marks=input().split()
kavya 20
name
'kavya'
marks
'20'
int
<class 'int'>
int(marks)
20
e=eval(input())
1
e
1
e=eval(input())
12.34
e=eval(input())
1234.13
e
1234.13
e=eval(input())
"kavya"
e
'kavya'
e=eval(input())
{1,2,3,4,5}
e=eval(input())
{1:1,2:2,3:3}
e
{1: 1, 2: 2, 3: 3}
e=eval(input())
2+3*4+5*8
e
54
s=''

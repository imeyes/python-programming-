Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=5
>>> y=7
>>> # Python program to swap two variables
>>> temp = x
>>> x=y
>>> y=temp
>>> print('The value of x after swapping: {}'.format(x))
The value of x after swapping: 7
>>> print('The value of y after swapping: {}'.format(y))
The value of y after swapping: 5
>>> # python program without using temp variable
>>> x=5
>>> y=7
>>> x,y =y,x
>>> print("x=",x)
x= 7
>>> print("y=",y)
y= 5
>>> # python program with addition substraction
>>> x=5
>>> y=7
>>> x=x+y
>>> y=x-y
>>> x= x-y
>>> print("x=",x)
x= 7
>>> print("y=",y)
y= 5
>>> x=5
>>> y=7
>>> x=x+y
>>> print("x=",x)
x= 12
>>> y=x-y
>>> print("y=",y)
y= 5
>>> x=x-y
>>> print("x=",x)
x= 7
>>> x=5
>>> y=7
>>> x=x*y
>>> y=x/y
>>> x=x/y
>>> print("x=",x)
x= 7.0
>>> print("y=",y)
y= 5.0
>>> x=5
>>> y=7
>>> x=x*y
>>> print("x=",x)
x= 35
>>> y=x/y
>>> print("y=",y)
y= 5.0
>>> x=x/y
>>> print("y=",y)
y= 5.0
>>> x=5
>>> y=7
>>> x=x^y
>>> y=X^y
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    y=X^y
NameError: name 'X' is not defined
>>> x=5
>>> y=7
>>> x=x^y
>>> y=x^y
>>> x=x^y
>>> print("x=",y)
x= 5
>>> print("y=",y)
y= 5
>>> print("x=",x)
x= 7
>>> x=5
>>> y=7
>>> x=x^y
>>> print("x=",x)
x= 2
>>> y=x^y
>>> print("y=",y)
y= 5
>>> x=x^y
>>> print("x=",x)
x= 7
>>> x=5
>>> y=7
>>> sum=x+y
>>> print("sum=",sum)
sum= 12
>>> x=input("enter first number")
enter first number12
>>> y= input("ener second number")
ener second number13
>>> sum=x+y
>>> print("sum=",sum)
sum= 1213
>>> print('sum=',sum)
sum= 1213
>>> x=input("enter first value:")
enter first value: 12
>>> y=input("enter second value:")
enter second value:13
>>> sum=loat(x)+float(y)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    sum=loat(x)+float(y)
NameError: name 'loat' is not defined
>>> sum=float(x)+float(y)
>>> print("sum=",sum)
sum= 25.0
>>> a=int(x)+int(y)
>>> print("a=",a)
a= 25
>>> a=x+y
>>> print("a=",a)
a=  1213
>>> 
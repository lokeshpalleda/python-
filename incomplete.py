fu(1)
def fu(d,e=5,f=6):
	print(d,e,f)
fu(1,6,7)"""

#1
"""print("add")
def func(a,b):
	return a+b
print(func(5,5))
print("subtraction")
def func(a,b):
	return a-b
print(func(5,5))
print("multiplication")
def func(a,b):
	return a*b
print(func(5,5))
print("division")
def func(a,b):
	return a/b	
print(func(5,5))"""

#2
"""a=int(input("enter number:"))
b=int(input("enter number:"))
def fun(a,b):
	return a+b,a-b,a*b,a/b
print(fun(a,b))
def func():
	print("add,sub,mul,div")
func()"""

#4
"""l=[10,20,30,40]
def fun(l):
	s=l[0]
	m=l[0]
	print("minimum")
	for i in l:
		if i<s:
			s=i
	print(s)
	print("maximum")
	for i in l:
		if i>m:
			m=i
	print(m)
fun(l)"""


#5
"""l=[10,20,30,40]
def fun(l):
	m=l[0]
	n=l[0]
	print("maximum")
	for i in l:
		if i>m:
			m=i
	l.remove(m)
	for j in l:
		if j>n:
			n=j
	print(n)
fun(l)"""


#6
a=input("enter:")
b=("")
def rev(a):
	for i in a:
		b=i+b
	print(b)
rev(a)	

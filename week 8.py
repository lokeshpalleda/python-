#GCD
def gcd(a,b):
	while b!=0:
		a,b=b,a%b
	return a
print(gcd(16,32))

#recursive GCD
def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)
a=int(input("enter number:"))
b=int(input("enter number:"))
n=gcd(a,b)
print(n)

#recursive fact
def fact(i):
	if i==0|i==1:
		return 1
	else:
		return i*fact(i-1)
n=int(input("enter number:"))
num=fact(n)
print(num)

#fabnoci
def fab(a):
	if a<=1:
		return a
	else:
		return (fab(a-1)+fab(a-2))
n=int(input("enter number:"))
if n<=0:
	print("no fab")
else:
	for i in range(n):
		print(fab(i))
		
#add in dict
dic={'a':1,'b':2,'c':3,'d':4}
dic.update({'e':5})
print((dic))

#sum
dic={'a':1,'b':2,'c':3,'d':4}
x=dic.values()
sum=0
for i in dic.values():
	sum+=i
	print(sum)

#check
d={'a':1,'b':2,'c':3,'d':4}
n=input("enter key")
if n in d.keys():
	print("found")
else:
	print("not found")

#string
#wap to reverse a string
c=0
d=0
s=input("enter a word:")
print(s[::-1])

rev=("")
print("without slicing")
for i in s:
	rev=i+rev
	c+=1
print(rev)
if rev==s:
	print("it is palindrome")
else:
	print("not a palindrome")
print("length:",c)
print("length using len",len(rev))
n=s.split()
for j in n:
	if len(j)%2==0:
		print(j)
m=("aeiouAEIOU")
k=input("enter a letter:")
if k in m:
	print("it is a vowel")
else:
	print("not a vowel")
m={'a','e','i','o','u'}
k=input("enter a string:")
for l in k:
	if l in m:
		d+=1
		print(l)
print("number of vowels:",d)
	

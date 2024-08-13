#strings
s1='Frienduu'
s2="bava"
s3='jaan123'
s4='123'
print(s1)
print(s2)
print("accessing each index")
print(s2[0])
print(s2[1])
print(s2[2])
print(s2[3])
print("accessing each index using for")
for i in s1:
	print(i)
print("concatenation")
print(s2+" "+s1)
print("multiply")
print(s2 *3)
print("membership operator")
print('f' in s1)
print("slicing")
print(s1[2:5])
print(s1[2:5:2])
print("alpha related")
print(s2.upper())
print(s1.lower())
print(s1.isupper())
print(s2.capitalize())
print(s2.title())
print(s3.isalnum())
print(s1.isalpha())
print(s3.isdigit())

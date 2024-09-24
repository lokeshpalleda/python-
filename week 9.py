#week 9
#text file

lines=['i am studying in vishnu\n',
'i am a cse student']
f=open('hemanth.txt','w')
f.writelines(lines)
f=open('hemanth.txt','r')
f.seek(10)
pos=f.tell()
print('pos',pos)
f.read(8)
post=f.tell()
print('pos',post)
f.close()


#binary file

f=open('number.bin','wb')
f.write(b'\x00\x01\x02')
f=open('number.bin','rb')
print(f.read())


#comma separated values file
data=[
['s.no','roll','name'],
[1,'g4','hemanth'],
[2,'i6','puneeth'],
[3,'i8','lokesh']
]
import csv
with open('table.csv','w') as file:
	readf=csv.reaedf(file)
for row in readf:
	print(row)

#sets
#split
#join
#map
s1={10,20,30,30}
s2={30,40,50}
#set methods
print("union")
print(s1|s2)
print("intersection")
print(s1&s2)
print("difference")
print(s1-s2)
print("set difference")
print(s1^s2)
#set operators

print("add 60")
s1.add(60)
print(s1)

print("add sets")
s1.add('sets')
print(s1)

print("pop")
s1.pop()
print(s1)

print("remove 30")
s1.remove(30)
print(s1)

print("discard 60")
s1.discard(60)
print(s1)

print("union")
print(s1.union(s2))

print("difference")
print(s1.difference(s2))

print("intersection")
print(s1.intersection(s2))

s1.clear()
print("clear")
print(s1)

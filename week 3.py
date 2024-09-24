

#avg &sum
l=[10,20,30]
print("sum of numbers")
print(sum(l))
len(l)
avg=sum(l)/len(l)
print("avg")
print(avg)



#reverse
l=[10,20,30]
l2=[]
print("enter element")
ele=input()
l.append(ele)
l2=l
l2.reverse()
print("reverse")
print(l2)
print("slicing")
print(l2[::-1])



#interchange
l=[10,20,30,40]
l[0],l[-1]=l[-1],l[0]
print(l)
n=len(l)      
x=l[0]
l[0]=l[n-1]
l[n-1]=x
print(l)




#firstoccurance
l=[10,20,30,30,40]
print("enter an element")
g=int(input())
l.remove(g)
print(l)


#max and min index
l=[10,20,30,40]
n=max(l)
m=min(l)
print("max index",l.index(n))
print("min index",l.index(m))



#even or odd
l=[]
even=[]
odd=[]
n=int(input("enter number of elements:"))
for i in range(n):
    ele=int(input("enter element:"))
    l.append(ele)
print(l)
for i in range(n):
    if l[i]%2==0:
        even.append(l[i])
    else:
        odd.append(l[i])
print("even",even)
print("odd",odd)

        
#concanate
ans=[]
l1=["m","na","i","abhi"]
l2=["y","me","s","ram"]
print(list(zip(l1,l2)))












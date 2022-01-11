l=[]
n=int(input())
for i in range(0,n):
    x=int(input())
    l.append(x)
for i in range(len(l)):
    for j in range(len(l)-1):
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
print(l)

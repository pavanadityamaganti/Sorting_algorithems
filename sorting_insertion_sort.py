n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
for i in range(1,len(l)):
    while l[i-1]>l[i] and i>0:
        l[i-1],l[i]=l[i],l[i-1]
        i-=1
print(l)

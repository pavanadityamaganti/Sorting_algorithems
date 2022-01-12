"""SELECTION SORTING:
PROCESS:
--------
step 1 :- we consider the given array in to two parts one is sorted and one is unsorted firstly list of index '0' is
          considered as sorted list and the other is unsorted list.
step 2 :- now we take the minimum value in list and place it in index '0' of list.
step 3 :- now we find the minimum value of unsorted list and swap it with 1st position of unsorted list and later it
          will combine with the sorted list.
step 4 :- now the step 3 will be continued until all the unsorted list is converted in to the sorted list."""
n=int(input())
l=[]
a=0
for i in range(n):
    x=int(input())
    l.append(x)
for i in range(n):
    for j in range(i+1,n):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l)

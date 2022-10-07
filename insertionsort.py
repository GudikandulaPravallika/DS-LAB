def insertionsort(lt):
    for i in range(1,len(lt)):
        j=i-1
        next_element=lt[i]
        while lt[j]>next_element and j>=0:
            lt[j+1]==lt[j]
            j=j-1
        lt[j+1]=next_element
l=[]
n=int(input("enter the size of list"))
for i in range(n):
    x=int(input("enter the elements"))
    l.append(x)
print(l)
print(insertionsort(l))


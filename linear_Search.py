def linearSearch(lt,key):
    for i in range(len(lt)):
        if lt[i]==key:
            return i
    return -1
l=[]
n=int(input("enter the size of list"))
for i in range(n):
    x=int(input("enter the elements"))
    l.append(x)
print(l)
key=int(input("enter the element to be found"))
s=linearSearch(l,key)
if s==-1:
    print("element is not found")
else:
    print("element is found at index:",s)
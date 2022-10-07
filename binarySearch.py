def binarysearch(lt,l,h,key):
    if l<=h:
        mid = (l+h)//2
        if lt[mid]==key:
            return mid
        elif lt[mid]<key:
            return binarysearch(lt,mid+1,h,key)
        else:
            return binarysearch(lt,l,mid-1,key)
    return -1

l=[]
n=int(input("enter the size of list"))
for i in range(n):
    x=int(input("enter the elements"))
    l.append(x)
print(l)
key=int(input("enter the element to be found"))
s=binarysearch(l,0,n-1,key)
if s==-1:
    print("element is not found")
else:
    print("element is found at index:",s)



def merge(lt,l,mid,h):
    n1=mid-l+1
    n2=h-mid
    L=[0]*n1
    R=[0]*n2
    for i in range(0,n1):
        L[i]=lt[l+i]
    for j in range(0,n2):
        R[j]=lt[mid+1+j]
    i=0
    j=0
    k=l
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            lt[k]=L[i]
            i+=1
        else:
            lt[k]=R[j]
            j+=1
        k+=1
    while i<n1:
        lt[k]=L[i]
        i+=1
        k+=1
    while j<n2:
        lt[k]=R[j]
        j+=1
        k+=1
    return lt
def mergesort(lt,l,h):
    if l<h:
        m=l+(h-l)//2
        mergesort(lt,l,m)
        mergesort(lt,m+1,h)
        merge(lt,l,m,h)
lt=[12,35,25,50,24,2,4,1,87]
mergesort(lt,0,len(lt)-1)
print(lt)
        
        
        
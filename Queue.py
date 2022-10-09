import sys
from array import *
queue=array("i",[])
def enqueue():
        ele=int(input("enter element"))
        queue.append(ele)
        print("Inserted")
def dequeue():
        if len(a)==0:
            print("Stack is empty")
        else:
            print("Deleted element is:",queue.pop())
def display():
            print("The element in stack are:")
            for i in a:
                print(i)
while True:
    print("1.add 2.remove 3.show 4.quit")
    ch=int(input("enter your choice"))
    if ch==1:
        enqueue()
    elif ch==2:
        dequeue()
    elif ch==3:
        display()
    elif ch==4:
        break
    else:
        print("Invalid choice")
    
    
        

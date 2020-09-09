"""
Python assignment
Exception handling
Compute 5/0 and use try/except
"""
try:
    n=int(input("Enter the number of elements in the list1\t"))
except:
    print("Wrong input")
lst=[]
while True:
    for i in range(0,n):  
        try:
            element=int(input())
            lst.append(element)
        except:
            print("The input value is not an integer")
            break
    break
if n==len(lst):
    print("The given number is",lst)
else:
    lst.clear()
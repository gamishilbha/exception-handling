"""
Python assignment
Exception handling
combining the subject, verb and object
"""
subject=["Americans", "Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
disp=[]
def Perm(subject, verbs, objects):
    for i in subject:
        disp.append(i)
        for j in verbs:
            disp.append(j)
            for x in objects:
                disp.append(x)
                print(*disp, end='.\n')
                disp.remove(x)
            disp.remove(j)
        disp.remove(i)
Perm(subject, verbs, objects)     
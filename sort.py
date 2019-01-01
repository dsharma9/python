#!/usr/bin/env python3.7

print("Shorting the entered list")
A=[]
for i in range(5):
    print(f"Kindly enter the position {i} value to the list")
    A.append(i)
    A[i]=input()

A.sort()
print(A)

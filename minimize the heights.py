"""
Given an array arr[] denoting heights of N towers and a positive integer K.

For each tower, you must perform exactly one of the following operations exactly once.

Increase the height of the tower by K
Decrease the height of the tower by K
Find out the minimum possible difference between
the height of the shortest and tallest towers after you have modified each tower
"""

arr=list(map(int,input().split()))
k=int(input("enter the value of k :"))
n=len(arr)
mini=0
maxi=0
answer=arr[-1]-arr[0]
for i in range(1,n):
    if arr[i]-k<0:
        continue
    maxi=max(arr[i-1]+k,arr[n-1]-k)
    mini=min(arr[0]+k,arr[i]-k)
    answer=min(answer,maxi-mini)
print("minimum difference in heights: ",answer)

"""
input:
1 5 8 10
enter the value of k :2
output:
minimum difference in heights:  5
"""
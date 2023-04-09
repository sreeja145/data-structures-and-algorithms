n=int(input())
arr=list(map(int,input().split()))
find_element=int(input())
if_found=0
for i in arr:
    if find_element==i:
        print("element found")
        if_found=1
        break
if if_found==0:
    print("element not found")
"""
Input
4
2 4 5 1
3
Output
element not found
"""
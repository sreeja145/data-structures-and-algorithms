"""
rotate the array cyclically by one
"""
arr=list(map(int,input().split()))
arr[:]=arr[-1:]+arr[0:-1]
print("after rotating: ",*arr)
"""
Input:
1 2 3 4 5
after rotating:  5 1 2 3 4
"""
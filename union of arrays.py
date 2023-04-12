"""
find out the union of two arrays
"""
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
final_arr=set()
for i in arr1:
    if i not in final_arr:
        final_arr.add(i)
for j in arr2:
    if j not in final_arr:
        final_arr.add(j)
print("union of two arrays: ",*final_arr)
"""
input:
0 1 2 3 4 5 6 7
1 2 3
output:
union of two arrays:  0 1 2 3 4 5 6 7
"""
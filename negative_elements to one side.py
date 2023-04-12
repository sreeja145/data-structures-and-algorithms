
"""
move all negative elements to one side
"""
arr=list(map(int,input().split()))
pos_ele=[]
neg_ele=[]
for i in arr:
    if i>0:
        pos_ele.append(i)
    else:
        neg_ele.append(i)
pos_ele.extend(neg_ele)
arr.clear()
arr.extend(pos_ele)
print("final array: ",*arr)
"""
Input:
0 -1 -2 -3 45 67 89
final array:  45 67 89 0 -1 -2 -3
"""

arr=list(map(int,input().split()))
min_element=arr[0]
max_element=arr[0]
for i in arr[1:]:
    if i<min_element:
        min_element=i
    if i>max_element:
        max_element=i
print("minimum element :",min_element,"maximum element : ",max_element)
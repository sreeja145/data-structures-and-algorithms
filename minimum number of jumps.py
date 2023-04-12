"""
minumum number of jumps required to reach from one end to other end by taking step values as jumps
"""


def min_jumps(builds):
    n = len(builds)
    if n == 0 or builds[0] == 0:
        return -1

    maxReach = builds[0]  # 1
    step = builds[0]  # 1
    jump = 1

    for i in range(1, n):  # i=1 2 3 4 5 6 7 8 9 10
        if i == n - 1:  # n-1=10 # i==n-1 jumps=3
            return jump

        maxReach = max(maxReach, i + builds[i])
        # {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9} max=max(1,4)=4 max=max(4,7)=7 max=max(7,11)=11 #
        # max=max(11,13)=13 max=max(13,7)=13 # max=max(13,12)=13 max=max(13,14)=14 max=max(14,14)=14 max=max(14,17)=17
        step -= 1  # steps=0 steps=3-1=2 steps=steps-1 =1 0 step=9 8 7 6 5

        if step == 0:
            jump += 1  # 2 3

            if i >= maxReach:  #
                return -1

            step = maxReach - i  # 4-1=3 # 13-4=9

    return -1


arr = list(map(int, input().split()))
print(min_jumps(arr))

"""
input:
1 3 5 8 9 2 6 7 8 9
output:
3
"""

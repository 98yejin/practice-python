def twosum(nums, target):
    nmap = {}
    for i, num in enumerate(nums):
        nmap[num] = i
    for i, num in enumerate(nums):
        temp = target - num
        if temp in nmap and i != nmap[temp]:
            return i, nmap[temp]


print(twosum([2, 7, 11, 15], 9))

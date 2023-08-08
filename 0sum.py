'''
brute force
time complexity O(n^3)
'''
def printAll0sum1(nums):
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total == 0:
                print("Sublist:", (i, j))


'''
multimap method
'''
def insert(d, key, value):
    d.setdefault(key, []).append(value)

def printAll0sum2(nums):
    d = {}
    insert(d, 0, -1)
    total = 0

    for i in range(len(nums)):
        total += nums[i]
        if total in d:
            list = d.get(total)
            for val in list:
                print("Sublist:", (val+1, i))
            
        insert(d, total, i)


'''
set method
time complexity O(n)
space complexity O(n)
'''
def check0sum(nums):
    s = set()
    s.add(0)
    total = 0

    for i in nums:
        total += i
        if total in s:
            return "Found Sublist"
        
    return "Not Found Sublist"


if __name__ == "__main__":
    nums = list(map(int, input("Enter space seperated numbers: ").split()))

    print("Checking for Zero Sum:", check0sum(nums))
    print("Printing All Zero Sum (BruteForce):")
    printAll0sum1(nums)
    print("Printing All Zero Sum (Mutlimap):")
    printAll0sum2(nums)
    
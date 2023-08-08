'''
hashtable/dictionary
time complexity O(n)
space complexity O(n)
'''
def find2sum3(nums, total):
    out = {}
    
    for i, val in enumerate(nums):
        if total - val in out:
            return "Pair Found:", nums[out.get(total-val)], nums[i]
        
        out[val] = i

    return "Pair Not Found"


'''
sorting method
time complexity O(n.log(n))
does not require extra space 
'''
def find2sum2(nums, total):
    nums.sort()
    (low, high) = (0, len(nums)-1)

    while low < high:
        if nums[low] + nums[high] == total:
            return "Pair Found:", (nums[low], nums[high])

        if nums[low] + nums[high] < total:
            low += 1
        else:
            high -= 1
        
    return "Pair Not Found"


'''
brute force
time complexity O(n^2)
does not require extra space 
'''
def find2sum1(nums, total):
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == total:
                return "Pair Found:", (nums[i], nums[j])
            
    return "Pair Not Found"

if __name__ == "__main__":
    nums = list(map(int, input("Enter space seperated numbers: ").split()))
    total = int(input("Enter the total number: "))

    print("Using Brute Force:", find2sum1(nums, total))
    print("Using Sorting:", find2sum2(nums, total))
    print("Using Hashtable:", find2sum3(nums, total))
    
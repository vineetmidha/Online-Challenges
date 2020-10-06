https://leetcode.com/problems/number-of-good-pairs/description/

TC: O(n^2)

def numIdenticalPairs_brute_force(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
    
    return count

TC: O(nlogn + n)

def numIdenticalPairs_2(nums): 
    count = 0

    nums.sort()

    j = 0
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            count += i-j
        else:
            j = i
    return count

nums = [1,2,3,1,1,3]

# [1,1,1,2,3,3]

TC: O(max + O(max_num) + n)

    def numIdenticalPairs3(self, nums: List[int]) -> int:
        max_num = max(nums)
        
        freq = [0 for x in range(max_num+1)]
        
        count = 0
        for x in nums:
            count += freq[x]
            freq[x] += 1
        
        return count

TC: O(n)

    def numIdenticalPairs3(self, nums: List[int]) -> int:
        freq = {}
        count = 0
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
            count += freq[x] - 1
        
        return count


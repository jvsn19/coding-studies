from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:       
        nums.sort()
        
        l, r = 0, len(nums) - 1
        ans = []
        
        for l in range(len(nums)):
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            
            appeared = {}
            
            for r in range(l + 1, len(nums)):
                if not (r < len(nums) - 1 and nums[r] == nums[r + 1]):
                    target = 0 - nums[l] - nums[r]

                    if target in appeared:
                        ans.append([nums[l], nums[appeared[target]], nums[r]])
                    
                appeared[nums[r]] = r

                          
                
        return ans
            
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = nums[-1]+2*k - nums[0]
        
        j = 1
        while j < len(nums):
            cur_max = max(nums[len(nums)-1] - k , nums[j-1] + k)
            cur_min = min(nums[0] + k , nums[j] - k)
            result = min(result,cur_max - cur_min)
            j+=1
        return result

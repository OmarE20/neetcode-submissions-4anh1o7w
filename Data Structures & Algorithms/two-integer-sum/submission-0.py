class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create Hashmap
        seen = {}

        # Loop through the list and look for j in hashmap. If not there, add to the hashmap and move on
        for i in range(len(nums)):
            j = target - nums[i]
            if j in seen:
                return [seen[j],i]
            seen[nums[i]] = i          
            
            



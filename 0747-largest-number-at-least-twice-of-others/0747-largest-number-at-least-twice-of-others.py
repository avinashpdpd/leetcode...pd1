class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m=max(nums)
        i=nums.index(m)
        nums.remove(m)
        
        if 2 *max(nums)<=m:
            return i
        else:
            return -1
        
        
        
        
        #  m=max(nums)
        # i=nums.index(m)
        # nums.remove(m)
        # if 2*max(nums)<=m:
        #     return i
        # else:
        #     return -1
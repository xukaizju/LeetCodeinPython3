class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index=0
        count=0
        while index<len(nums):
            if nums[index]!=val:
                nums[count]=nums[index]
                count+=1
            index+=1
        return  count
        
        """
        a=[x for x in nums if x!=val]
        return  len(a)
        
        Note:
        This is my first code, the result In spyder3 is correct, but LeetCode's IDE reminder me it's wrong,
        I don't know why, so I left this note to record this.
        """

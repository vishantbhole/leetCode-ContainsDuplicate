class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash = {}
 
        for i in range(len(nums)):
            if nums[i] in hash:
                return True
            else:
                hash[nums[i]] = i
        return False

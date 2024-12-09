class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = set()
        for num in nums:
            if num in map:
                return True
            map.add(num)
        return False
        

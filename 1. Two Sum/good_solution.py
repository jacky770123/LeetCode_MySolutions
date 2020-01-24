class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        https://medium.com/@havbgbg68/leetcode-1-two-sum-python-8d77c223abd3
        """
        hash_table = {}
        for i, num in enumerate(nums):
            if target - num in hash_table:
                return([hash_table[target - num], i])
                break
            hash_table[num] = i
        return([])
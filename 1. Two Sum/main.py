from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(0, len(nums)):
            value = target - nums[i]
            if (value in nums[ i + 1 : ]):
                ans.append(i)
                ans.append(nums.index(value, i + 1))
                return ans

if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([3, 2, 4], 6))
    print(solution.twoSum([0, 4, 3, 0], 0))
    print(solution.twoSum([-1,-2,-3,-4,-5], -8))
from typing import List

class Solution:
    # Brute Force
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
          for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
              return [i, j]
        return []

    # Hash Table
    def twoSumHashTable(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        # {2: 0, 7: 1, 11: 2, 15: 3}
        print(numMap)

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []  # No solution found
        



solution = Solution()
result1 = solution.twoSum([2,7,11,15], 9)
result2 = solution.twoSumHashTable([2,7,11,15], 9)
print(result1)
print(result2)
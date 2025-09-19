class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
        

if __name__ == '__main__':
    s = Solution()

    nums, target = [2, 7, 11, 15], 9
    print(s.twoSum(nums, target))
    nums, target = [3, 2, 4], 6
    print(s.twoSum(nums, target))
    nums, target = [3, 3], 6
    print(s.twoSum(nums, target))

class Solution:
    #     def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(nums, target):
        for i in nums:
            for j in nums:
                if i + j == target:
                    if i == j:
                        continue
                    if i == j:
                        return nums.index(i)
                    else:
                        return nums.index(i), nums.index(j)


s = Solution
print(s.twoSum([9, 9], 18))
lis = [1, 2, 3, 5, 6]
print(lis[0], '=========')


# print(lis.index(5))
# print(dir(lis))


class Solution:
    #     def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return i, j


s = Solution
print(s.twoSum([9, 9], 18))


class Solution:
    #     def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self,nums, target):
        for i in range(len(nums)):
            j = target - nums[i]
            if j in nums:

                if nums.index(j) == i:
                    pass
                else:
                    return i, nums.index(j)


s = Solution
print(s.twoSum([9, 9], 18))

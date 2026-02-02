# 35. Search Insert Position

class Solution:

    # Linear Search Approach – O(n)
    def searchInsertLinear(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

    # Binary Search Approach – O(log n)
    def searchInsertBinary(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


# Test Run
if __name__ == "__main__":
    obj = Solution()
    nums = [1, 3, 5, 6]

    print("Linear Search:")
    print(obj.searchInsertLinear(nums, 5))  # 2
    print(obj.searchInsertLinear(nums, 2))  # 1
    print(obj.searchInsertLinear(nums, 7))  # 4

    print("\nBinary Search:")
    print(obj.searchInsertBinary(nums, 5))  # 2
    print(obj.searchInsertBinary(nums, 2))  # 1
    print(obj.searchInsertBinary(nums, 7))  # 4



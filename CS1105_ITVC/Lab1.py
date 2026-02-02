# Q. 217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


# Driver code : LeetCode auto-calls the function, but in VS Code we need driver code to execute it.
if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    sol = Solution()
    print(sol.containsDuplicate(nums))
    """Output: Enter numbers: 1 2 3 2
    True"""



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, postfix = [1] * n, [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]
        return [prefix[i] * postfix[i] for i in range(n)]

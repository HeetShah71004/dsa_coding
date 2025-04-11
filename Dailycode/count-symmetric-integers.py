class Solution(object):
    def countSymmetricIntegers(self, low, high):
        count = 0
        for i in range(low, high + 1):
            s = str(i)
            if len(s) % 2 == 0 and sum(int(s[j]) for j in range(len(s) // 2)) == sum(int(s[j]) for j in range(len(s) // 2, len(s))):
                count += 1
        return count

# Test cases

low = 1
high = 100
solution = Solution()
result = solution.countSymmetricIntegers(low, high)
print(result)  # Output: 9
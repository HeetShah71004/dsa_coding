# 50. POW(x, n)
# implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

# Constraints:

# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# n is an integer.
# Either x is not zero or n > 0.
# -10^4 <= xn <= 10^4
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if x == 0:
            return 0.0
        if x == 1:
            return 1.0
        if x == -1:
            return 1.0 if n % 2 == 0 else -1.0

        exponent = n
        if n < 0:
            x = 1 / x
            exponent = -exponent

        ans = 1.0
        while exponent > 0:
            if exponent % 2 == 1:
                ans *= x
            x *= x
            exponent //= 2
        return ans

# Create an instance of the Solution class
solution = Solution()

# Example 1
x1, n1 = 2.00000, 10
print(f"Input: x = {x1}, n = {n1}\nOutput: {solution.myPow(x1, n1):.5f}\n")

# Example 2
x2, n2 = 2.10000, 3
print(f"Input: x = {x2}, n = {n2}\nOutput: {solution.myPow(x2, n2):.5f}\n")

# Example 3
x3, n3 = 2.00000, -2
print(f"Input: x = {x3}, n = {n3}\nOutput: {solution.myPow(x3, n3):.5f}\n")

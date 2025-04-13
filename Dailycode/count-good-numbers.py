class Solution:
    MOD = 10**9 + 7

    def modExp(self, base, exp):
        result = 1
        base %= self.MOD
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % self.MOD
            base = (base * base) % self.MOD
            exp //= 2
        return result

    def countGoodNumbers(self, n: int) -> int:
        evens = (n + 1) // 2
        odds = n // 2
        evenPart = self.modExp(5, evens)
        oddPart = self.modExp(4, odds)
        return (evenPart * oddPart) % self.MOD

# Test cases

n = 1
solution = Solution()
print(solution.countGoodNumbers(n))  # Output: 5
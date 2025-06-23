class Solution:
    def createPalindrome(self, num: int, odd: bool) -> int:
        x = num
        if odd:
            x //= 10
        while x > 0:
            num = num * 10 + x % 10
            x //= 10
        return num

    def isPalindrome(self, num: int, base: int) -> bool:
        digits = []
        while num > 0:
            digits.append(num % base)
            num //= base
        return digits == digits[::-1]

    def kMirror(self, k: int, n: int) -> int:
        total = 0
        length = 1
        while n > 0:
            for i in range(length, length * 10):
                if n <= 0:
                    break
                p = self.createPalindrome(i, True)
                if self.isPalindrome(p, k):
                    total += p
                    n -= 1
            for i in range(length, length * 10):
                if n <= 0:
                    break
                p = self.createPalindrome(i, False)
                if self.isPalindrome(p, k):
                    total += p
                    n -= 1
            length *= 10
        return total
# Example test cases
sol = Solution()

# Example 1
k = 2
n = 5
print(f"Input: k = {k}, n = {n}")
print("Output:", sol.kMirror(k, n))
# Expected: 25

# Example 2
k = 3
n = 7
print(f"\nInput: k = {k}, n = {n}")
print("Output:", sol.kMirror(k, n))
# Expected: 499

# Example 3
k = 7
n = 17
print(f"\nInput: k = {k}, n = {n}")
print("Output:", sol.kMirror(k, n))
# Expected: 20379000
from collections import Counter

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        if n == 1:
            total = 0
            for i in range(1, 10):
                if i % k == 0:
                    total += 1
            return total

        fact = [1]
        for i in range(1, n + 1):
            fact.append(fact[-1] * i)
        
        seen = set()
        ans = 0

        # Loop through half of the palindromes
        for left in range(10 ** ((n - 1) // 2), 10 ** ((n + 1) // 2)):
            l = str(left)
            r = l[::-1]
            if n % 2 == 1:
                r = r[1:]  # Remove middle digit if odd length
            t = l + r    # Form full palindrome

            if int(t) % k != 0:
                continue

            # Check for repeated permutations
            s = "".join(sorted(t))
            if s in seen:
                continue
            seen.add(s)

            count = Counter(t)

            # Calculate total permutations
            total = fact[n]
            for key in count:
                total //= fact[count[key]]

            ans += total

            # Subtract permutations starting with '0'
            if count["0"] > 0:
                total_non_zero = fact[n - 1]
                count["0"] -= 1
                for key in count:
                    total_non_zero //= fact[count[key]]
                ans -= total_non_zero

        return ans

# Test case
n = 3
k = 5
solution = Solution()
print(solution.countGoodIntegers(n, k))  # Expected output: 27

class Solution(object):
    def countValidNumbers(self, idx, tight, numStr, suffix, limit, numLength, dp):
        if idx == numLength:
            return 1
        if dp[idx][tight] != -1:
            return dp[idx][tight]
        lowerBound = 0
        count = 0
        upperBound = min(limit, int(numStr[idx])) if tight else limit
        suffixStartIdx = numLength - len(suffix)
        if suffixStartIdx <= idx:
            lowerBound = int(suffix[idx - suffixStartIdx])
            upperBound = min(upperBound, int(suffix[idx - suffixStartIdx]))
        for i in range(lowerBound, upperBound + 1):
            count += self.countValidNumbers(idx + 1, tight and (i == int(numStr[idx])), numStr, suffix, limit, numLength, dp)
        dp[idx][tight] = count
        return count

    def numberOfPowerfulInt(self, start, finish, limit, s):
        upperLimit = str(finish)
        lowerLimit = str(start - 1)
        upperLength = len(upperLimit)
        lowerLength = len(lowerLimit)
        upperCount = 0
        lowerCount = 0
        if len(s) <= upperLength:
            dp = [[-1 for _ in range(2)] for _ in range(upperLength)]
            upperCount = self.countValidNumbers(0, 1, upperLimit, s, limit, upperLength, dp)
        if len(s) <= lowerLength:
            dp = [[-1 for _ in range(2)] for _ in range(lowerLength)]
            lowerCount = self.countValidNumbers(0, 1, lowerLimit, s, limit, lowerLength, dp)
        return upperCount - lowerCount

# Test cases

start = 1
finish = 6000
limit = 4
s = "124"
solution = Solution()
result = solution.numberOfPowerfulInt(start, finish, limit, s)
print(result)  # Expected output: 5
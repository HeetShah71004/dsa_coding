from collections import deque

class Solution:
    def isKRepeatedSubsequence(self, s: str, pattern: str, k: int) -> bool:
        pos = matched = 0
        m = len(pattern)
        for ch in s:
            if ch == pattern[pos]:
                pos += 1
                if pos == m:
                    pos = 0
                    matched += 1
                    if matched == k:
                        return True
        return False

    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = [0]*26
        for ch in s:
            freq[ord(ch)-97] += 1
        candidates = [chr(i+97) for i in range(25, -1, -1) if freq[i] >= k]

        q = deque(candidates)
        ans = ""

        while q:
            curr = q.popleft()
            if len(curr) > len(ans) or (len(curr) == len(ans) and curr > ans):
                if self.isKRepeatedSubsequence(s, curr, k):
                    ans = curr
            if len(curr) == 7:
                continue
            for ch in candidates:
                nxt = curr + ch
                if self.isKRepeatedSubsequence(s, nxt, k):
                    q.append(nxt)
        return ans

# Test examples
def main():
    sol = Solution()

    # Example 1
    s1 = "letsleetcode"
    k1 = 2
    print("Example 1:")
    print("Input: s =", s1, ", k =", k1)
    print("Output:", sol.longestSubsequenceRepeatedK(s1, k1))
    print("Expected: let")
    print()

    # Example 2
    s2 = "bb"
    k2 = 2
    print("Example 2:")
    print("Input: s =", s2, ", k =", k2)
    print("Output:", sol.longestSubsequenceRepeatedK(s2, k2))
    print("Expected: b")
    print()

    # Example 3
    s3 = "ab"
    k3 = 2
    print("Example 3:")
    print("Input: s =", s3, ", k =", k3)
    print("Output:", sol.longestSubsequenceRepeatedK(s3, k3))
    print("Expected: \"\"")
    print()

if __name__ == "__main__":
    main()

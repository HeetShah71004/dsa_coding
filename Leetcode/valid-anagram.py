class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in t:
            if i in dic and dic[i] != 0:
                dic[i] -= 1
            else:
                return False
        for i in dic:
            if dic[i] != 0:
                return False
        return True


# Test Examples
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    s1 = "anagram"
    t1 = "nagaram"
    print("Example 1 Output:", sol.isAnagram(s1, t1))  # Expected: True

    # Example 2
    s2 = "rat"
    t2 = "car"
    print("Example 2 Output:", sol.isAnagram(s2, t2))  # Expected: False

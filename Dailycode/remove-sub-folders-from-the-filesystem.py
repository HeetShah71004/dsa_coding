from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        for f in folder:
            if not res:
                res.append(f)
            else:
                prev = res[-1]
                if f.startswith(prev) and len(f) > len(prev) and f[len(prev)] == '/':
                    continue
                else:
                    res.append(f)
        return res

# Test cases
sol = Solution()

# Example 1
folder1 = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
print("Input:", folder1)
print("Output:", sol.removeSubfolders(folder1))
# Expected: ["/a", "/c/d", "/c/f"]

# Example 2
folder2 = ["/a", "/a/b/c", "/a/b/d"]
print("\nInput:", folder2)
print("Output:", sol.removeSubfolders(folder2))
# Expected: ["/a"]

# Example 3
folder3 = ["/a/b/c", "/a/b/ca", "/a/b/d"]
print("\nInput:", folder3)
print("Output:", sol.removeSubfolders(folder3))
# Expected: ["/a/b/c", "/a/b/ca", "/a/b/d"]

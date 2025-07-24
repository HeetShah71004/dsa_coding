import collections

class Solution:
    def minimumScore(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # subtree_xor[i] = XOR sum of the subtree rooted at i
        # descendants[i] = set of all nodes in the subtree of i
        subtree_xor = [0] * n
        descendants = [set() for _ in range(n)]

        # Perform a post-order DFS from root 0 to populate our data structures
        def dfs(node, parent):
            subtree_xor[node] = nums[node]
            descendants[node].add(node)
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
                    subtree_xor[node] ^= subtree_xor[neighbor]
                    descendants[node].update(descendants[neighbor])

        dfs(0, -1)
        total_xor = subtree_xor[0]
        min_score = float('inf')

        # Try every pair of nodes as cut points
        for i in range(1, n):
            for j in range(i + 1, n):
                xor_i = subtree_xor[i]
                xor_j = subtree_xor[j]

                if j in descendants[i]:
                    val1 = xor_j
                    val2 = xor_i ^ xor_j
                    val3 = total_xor ^ xor_i
                elif i in descendants[j]:
                    val1 = xor_i
                    val2 = xor_j ^ xor_i
                    val3 = total_xor ^ xor_j
                else:
                    val1 = xor_i
                    val2 = xor_j
                    val3 = total_xor ^ xor_i ^ xor_j

                score = max(val1, val2, val3) - min(val1, val2, val3)
                min_score = min(min_score, score)

        return min_score


# Test cases
def main():
    sol = Solution()

    # Example 1
    nums1 = [1, 5, 5, 4, 11]
    edges1 = [[0, 1], [1, 2], [1, 3], [3, 4]]
    print("Example 1 Output:", sol.minimumScore(nums1, edges1))  # Expected: 9

    # Example 2
    nums2 = [5, 5, 2, 4, 4, 2]
    edges2 = [[0, 1], [1, 2], [5, 2], [4, 3], [1, 3]]
    print("Example 2 Output:", sol.minimumScore(nums2, edges2))  # Expected: 0

if __name__ == "__main__":
    main()

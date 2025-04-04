class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return (0, None)
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)
            if left_depth > right_depth:
                return (left_depth + 1, left_lca)
            elif right_depth > left_depth:
                return (right_depth + 1, right_lca)
            else:
                return (left_depth + 1, node)
        return dfs(root)[1]

    def findDeepestLeaves(self, root: TreeNode):
        from collections import deque
        if not root:
            return []
        
        queue = deque([(root, 0)])
        max_depth = 0
        leaves_at_depth = []

        while queue:
            node, depth = queue.popleft()
            if depth > max_depth:
                max_depth = depth
                leaves_at_depth = [node.val]
            elif depth == max_depth:
                leaves_at_depth.append(node.val)

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return leaves_at_depth

# --- Helper: Build Tree from Level-Order List ---
def build_tree(values):
    from collections import deque
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

# --- Test Case ---

values = [3,5,1,6,2,0,8,None,None,7,4]
root = build_tree(values)

sol = Solution()
deepest_leaves = sol.findDeepestLeaves(root)
lca_node = sol.lcaDeepestLeaves(root)

# --- Output ---
print("Deepest Leaves:", deepest_leaves)
print("Lowest Common Ancestor of Deepest Leaves:", lca_node.val if lca_node else None)

# Expected Output:
# Deepest Leaves: [7, 4]
# Lowest Common Ancestor of Deepest Leaves: 2

# [2,7,4]

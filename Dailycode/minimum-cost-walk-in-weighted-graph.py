class Solution:
    def minimumCost(self, n: int, edges: list[list[int]], query: list[list[int]]) -> list[int]:
        parent = list(range(n))
        
        min_path_cost = [-1] * n
        
        def find_root(node: int) -> int:
            if parent[node] != node:
                parent[node] = find_root(parent[node])
            return parent[node]
        
        for source, target, weight in edges:
            source_root = find_root(source)
            target_root = find_root(target)
            
            min_path_cost[target_root] &= weight
            
            if source_root != target_root:
                min_path_cost[target_root] &= min_path_cost[source_root]
                parent[source_root] = target_root
        
        result = []
        for start, end in query:
            if start == end:
                result.append(0)
            elif find_root(start) != find_root(end):
                result.append(-1)
            else:
                result.append(min_path_cost[find_root(start)])
                
        return result
    
# Test cases
n = 5
edges = [[0,1,7],[1,3,7],[1,2,1]]
query = [[0,3],[3,4]]
solution = Solution()
print(solution.minimumCost(n, edges, query)) # [1, -1]
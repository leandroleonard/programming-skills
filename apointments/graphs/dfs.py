class Solution:

    def dfs(self, adj):
        visited = [False] * len(adj)
        result = []

        self.dfsRecursivly(adj, 0, visited, result)
        return result
    
    def dfsRecursivly(self, node, val, visited, result):
        result.append(val)
        visited[val] = True

        for i in node[val]:
            if not visited[i]:
                self.dfsRecursivly(node, i, visited, result)


s = Solution()

print(s.dfs([[2,3,1], [0], [0, 4], [0], [2]]))
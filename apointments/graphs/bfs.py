from collections import deque

class Solution:
    def bfs(self, adj):
        n = len(adj)
        visited = [False] * n
        res = []    

        visited[0] = True
        q = deque()
        q.append(0)

        while q:
            current = q.popleft()
            res.append(current)

            for i in adj[current]:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)

        return res

    

s = Solution()

print(s.bfs([[2, 3, 1], [0], [0, 4], [0], [2]]))
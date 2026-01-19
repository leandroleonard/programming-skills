from collections import deque

class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
        
        visited = {}
        q = deque([node])
        visited[node] = Node(node.val)

        while q:
            current = q.popleft()

            for neighbor in current.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    q.append(neighbor)

                visited[current].neigbors.append(visited[neighbor])


        return visited[node]
    

s = Solution()
print(s.cloneGraph([[2,4],[1,3],[2,4],[1,3]]))

        
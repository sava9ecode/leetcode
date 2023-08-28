class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(start):
            visited.add(start)
            for end in range(len(isConnected)):
                if isConnected[start][end] and end not in visited:
                    dfs(end)

        number_of_provinces = 0
        visited = set()
        for start in range(len(isConnected)):
            if start not in visited:
                number_of_provinces += 1
                dfs(start)

        return number_of_provinces

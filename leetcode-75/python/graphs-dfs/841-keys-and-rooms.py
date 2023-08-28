class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        visited = set(stack)

        while stack:
            key = stack.pop()
            for sub_key in rooms[key]:
                if sub_key not in visited:
                    visited.add(sub_key)
                    stack.append(sub_key)

        return len(visited) == len(rooms)

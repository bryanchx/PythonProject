from collections import deque
from typing import (
    List,
)


class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """

    def has_path(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        qu = deque()
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        x1 = start[0]
        y1 = start[1]
        x2 = destination[0]
        y2 = destination[1]
        qu.append((x1, y1, 0))
        maze[x1][y1] = 2
        while len(qu) > 0:
            cur = qu.popleft()
            if cur[0] == x2 and cur[1] == y2:
                return True
            for dx, dy in dirs:
                x = cur[0] + dx
                y = cur[1] + dy
                while x >= 0 and y >= 0 and x < len(maze) and y < len(maze[0]) and maze[x][y] != 1:
                    x += dx
                    y += dy
                x -= dx
                y -= dy
                if maze[x][y] == 0:
                    qu.append((x, y, cur[2] + 1))
                    maze[x][y] = 2
        else:
            return False


if __name__ == "__main__":
    maze = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    start = [1,1]
    destination = [8,8]
    has_path = Solution().has_path(maze, start, destination)
    print(has_path)

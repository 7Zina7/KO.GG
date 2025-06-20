import sys
import random

class Maze:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.maze = [[1 for _ in range(width)] for _ in range(height)]
        self.generate_maze()

    def generate_maze(self):
        stack = [(0, 0)]
        self.maze[0][0] = 0
        while stack:
            x, y = stack[-1]
            neighbors = []
            for dx, dy in [(-2,0),(2,0),(0,-2),(0,2)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < self.width and 0 <= ny < self.height and self.maze[ny][nx] == 1:
                    neighbors.append((nx, ny))
            if neighbors:
                nx, ny = random.choice(neighbors)
                self.maze[(y+ny)//2][(x+nx)//2] = 0
                self.maze[ny][nx] = 0
                stack.append((nx, ny))
            else:
                stack.pop()

    def display(self, path=None):
        for y in range(self.height):
            row = ''
            for x in range(self.width):
                if path and (x, y) in path:
                    row += '*'
                elif self.maze[y][x] == 1:
                    row += '#'
                else:
                    row += ' '
            print(row)

    def solve(self):
        from collections import deque
        queue = deque([((0,0), [(0,0)])])
        visited = set([(0,0)])
        while queue:
            (x, y), path = queue.popleft()
            if (x, y) == (self.width-1, self.height-1):
                return path
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < self.width and 0 <= ny < self.height and self.maze[ny][nx] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path+[(nx, ny)]))
        return None

def main():
    width = 15
    height = 15
    maze = Maze(width, height)
    print('Maze:')
    maze.display()
    input('Press Enter to solve the maze...')
    path = maze.solve()
    if path:
        print('Solution:')
        maze.display(path)
    else:
        print('No solution found.')

if __name__ == '__main__':
    main()

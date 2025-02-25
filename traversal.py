import random

class Node:
    def __init__(self, a, b, z):
        self.x = a
        self.y = b
        self.depth = z

class DFS:
    def __init__(self):
        self.directions = 4
        self.x_move = [1, -1, 0, 0]
        self.y_move = [0, 0, 1, -1]
        self.found = False
        self.N = 0
        self.source = None
        self.goal = None
        self.goal_level = 999999
        self.path = []
        self.topological_order = []

    def gengrid(self):
        self.N = random.randint(4, 7)
        grid = [[random.choice([0, 1]) for _ in range(self.N)] for _ in range(self.N)]
        return grid

    def obs_pos(self, grid):
        while True:
            x = random.randint(0, self.N - 1)
            y = random.randint(0, self.N - 1)
            if grid[x][y] == 1:
                return x, y

    def init(self):
        graph = self.gengrid()
        source_x, source_y = self.obs_pos(graph)
        goal_x, goal_y = self.obs_pos(graph)
        
        # Ensure source and goal are not the same
        while goal_x == source_x and goal_y == source_y:
            goal_x, goal_y = self.obs_pos(graph)
        
        self.source = Node(source_x, source_y, 0)
        self.goal = Node(goal_x, goal_y, self.goal_level)
        
        print("Generated Grid:")
        for row in graph:
            print(row)
        
        print("Source: ({}, {})".format(self.source.x, self.source.y))
        print("Goal: ({}, {})".format(self.goal.x, self.goal.y))
        
        self.st_dfs(graph, self.source)
        
        if self.found:
            print("Goal found")
            print("Number of moves required =", self.goal.depth)
            print("DFS Path:", self.path)
        else:
            print("Goal cannot be reached from the starting node")
        
        print("Topological Order of Traversal:", self.topological_order)

    def print_direction(self, m, x, y):
        directions = ["Down", "Up", "Right", "Left"]
        print(f"Moving {directions[m]} to ({x}, {y})")

    def st_dfs(self, graph, u):
        if self.found:
            return
        
        graph[u.x][u.y] = 0
        self.path.append((u.x, u.y))
        self.topological_order.append((u.x, u.y))
        
        for j in range(self.directions):
            v_x = u.x + self.x_move[j]
            v_y = u.y + self.y_move[j]
            
            if 0 <= v_x < self.N and 0 <= v_y < self.N and graph[v_x][v_y] == 1:
                v_depth = u.depth + 1
                self.print_direction(j, v_x, v_y)
                
                if v_x == self.goal.x and v_y == self.goal.y:
                    self.found = True
                    self.goal.depth = v_depth
                    self.path.append((v_x, v_y))
                    return
                
                child = Node(v_x, v_y, v_depth)
                self.st_dfs(graph, child)
                
                if self.found:
                    return
        
        graph[u.x][u.y] = 1
        self.path.pop()


def main():
    d = DFS()
    d.init()


if __name__ == "__main__":
    main()
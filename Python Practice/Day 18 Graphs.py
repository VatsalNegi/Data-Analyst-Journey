"""
Day 18: Graphs (BFS & DFS)

Topics Covered:
18. BFS Traversal (Graph)
19. DFS Traversal (Iterative)
20. Number of Connected Components
21. Flood Fill Algorithm

Author: Vatsal Negi
Purpose: DSA + Interview Preparation
"""

from collections import deque

# ---------------------------------------------------
# Graph Representation (Adjacency List)
# ---------------------------------------------------

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1],
    4: [5],
    5: [4]
}

# ---------------------------------------------------
# 18. BFS Traversal (Graph)
# ---------------------------------------------------

def bfs(graph, start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# ---------------------------------------------------
# 19. DFS Traversal (Iterative)
# ---------------------------------------------------

def dfs_iterative(graph, start):
    visited = set()
    stack = []

    stack.append(start)

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(neighbour)


# ---------------------------------------------------
# 20. Number of Connected Components
# ---------------------------------------------------

def connected_components(graph):
    visited = set()
    count = 0

    def dfs(node):
        stack = [node]
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.add(curr)
                for neighbour in graph[curr]:
                    if neighbour not in visited:
                        stack.append(neighbour)

    for node in graph:
        if node not in visited:
            dfs(node)
            count += 1

    return count


# ---------------------------------------------------
# 21. Flood Fill Algorithm
# ---------------------------------------------------

def flood_fill(image, sr, sc, new_color):
    rows = len(image)
    cols = len(image[0])
    original_color = image[sr][sc]

    if original_color == new_color:
        return image

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if image[r][c] != original_color:
            return

        image[r][c] = new_color

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return image


# ---------------------------------------------------
# Driver Code (Testing)
# ---------------------------------------------------

if __name__ == "__main__":

    print("BFS Traversal from node 0:")
    bfs(graph, 0)

    print("\nDFS Traversal from node 0:")
    dfs_iterative(graph, 0)

    print("\nNumber of Connected Components:")
    print(connected_components(graph))

    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]

    print("\nFlood Fill Result:")
    result = flood_fill(image, 1, 1, 2)
    for row in result:
        print(row)
      

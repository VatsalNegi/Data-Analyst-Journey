"""
Day 16: Trees (DSA)

Topics Covered:
1. Binary Tree Basics
2. Inorder Traversal
3. Preorder Traversal
4. Postorder Traversal
5. Level Order Traversal (BFS)
6. Height of Binary Tree
7. Count Nodes in Binary Tree

Author: Vatsal Negi
Purpose: DSA + Interview Preparation
"""

# ---------------------------------------------------
# 1. Binary Tree Node Structure
# ---------------------------------------------------
# A Binary Tree is a non-linear data structure
# Each node has at most two children (left & right)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# ---------------------------------------------------
# Sample Tree Creation
#        1
#       / \
#      2   3
#     / \
#    4   5
# ---------------------------------------------------

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


# ---------------------------------------------------
# 2. Inorder Traversal (Left → Root → Right)
# ---------------------------------------------------

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


# ---------------------------------------------------
# 3. Preorder Traversal (Root → Left → Right)
# ---------------------------------------------------

def preorder(root):
    if root is None:
        return

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


# ---------------------------------------------------
# 4. Postorder Traversal (Left → Right → Root)
# ---------------------------------------------------

def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


# ---------------------------------------------------
# 5. Level Order Traversal (BFS on Tree)
# ---------------------------------------------------

from collections import deque

def level_order(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# ---------------------------------------------------
# 6. Height of Binary Tree
# ---------------------------------------------------

def height(root):
    if root is None:
        return 0

    return max(height(root.left), height(root.right)) + 1


# ---------------------------------------------------
# 7. Count Nodes in Binary Tree
# ---------------------------------------------------

def count_nodes(root):
    if root is None:
        return 0

    return 1 + count_nodes(root.left) + count_nodes(root.right)


# ---------------------------------------------------
# Driver Code (Testing)
# ---------------------------------------------------

if __name__ == "__main__":
    print("Inorder Traversal:")
    inorder(root)

    print("\nPreorder Traversal:")
    preorder(root)

    print("\nPostorder Traversal:")
    postorder(root)

    print("\nLevel Order Traversal:")
    level_order(root)

    print("\nHeight of Tree:", height(root))
    print("Total Nodes:", count_nodes(root))
  

"""
Day 17: Binary Search Tree (BST)

Topics Covered:
15. Insert into BST
16. Search in BST
17. Validate Binary Search Tree

Author: Vatsal Negi
Purpose: DSA + Interview Preparation
"""

# ---------------------------------------------------
# Binary Search Tree Node
# ---------------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# ---------------------------------------------------
# 15. Insert into BST
# ---------------------------------------------------

def insert_bst(root, key):
    if root is None:
        return Node(key)

    if key < root.data:
        root.left = insert_bst(root.left, key)
    elif key > root.data:
        root.right = insert_bst(root.right, key)

    return root


# ---------------------------------------------------
# 16. Search in BST
# ---------------------------------------------------

def search_bst(root, key):
    if root is None:
        return False

    if root.data == key:
        return True
    elif key < root.data:
        return search_bst(root.left, key)
    else:
        return search_bst(root.right, key)


# ---------------------------------------------------
# 17. Validate Binary Search Tree
# ---------------------------------------------------

def validate_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True

    if not (min_val < root.data < max_val):
        return False

    return (
        validate_bst(root.left, min_val, root.data) and
        validate_bst(root.right, root.data, max_val)
    )


# ---------------------------------------------------
# Driver Code (Testing)
# ---------------------------------------------------

if __name__ == "__main__":

    root = None
    values = [8, 3, 10, 1, 6, 14]

    # Insert nodes
    for val in values:
        root = insert_bst(root, val)

    # Search in BST
    print("Search 6:", search_bst(root, 6))    # True
    print("Search 7:", search_bst(root, 7))    # False

    # Validate BST
    print("Is Valid BST:", validate_bst(root)) # True

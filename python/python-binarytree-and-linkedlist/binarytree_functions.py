"""
Write each of the following functions on a binary tree with a given root of the type BTree.

1. Return the in-order traversal of a tree as a list.
2. Test if a binary tree is symmetric (a binary tree is symmetric if rotating it about the vertical bar through the root for 180 degrees gives the same tree).
3. Return the maximum path sum (the sum of the path from the root to a leaf is the sum of values in the nodes on the path).
4. Test if a binary tree is a search tree.
5. Test if a given value occurs in a binary search tree.
6. Insert a value into a binary search tree such that the resulting tree remains a search tree.
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right


# 1. In‐order traversal
def inorder(root):
    """
    Return a list of node values in in-order (Left, Root, Right).
    """
    # Base case
    if not root:
        return []
    
    return inorder(root.left) + [root.val] + inorder(root.right)


# 2. Test if a tree is symmetric
def is_symmetric(root):
    def dfs(left, right):
        # Base cases
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        
        return dfs(left.left, right.right) and dfs(left.right, right.left)

    return dfs(root.left, root.right)


# 3. Maximum root‐to‐leaf path sum
def max_path_sum(root):
    # Base cases
    if root is None:
        return 0
    # If leaf node, its path‐sum is just its own value
    if not root.left and not root.right:
        return root.val
    # Otherwise, pick the larger sum among children
    left_sum  = max_path_sum(root.left) if root.left else float('-inf')
    right_sum = max_path_sum(root.right) if root.right else float('-inf')
    return root.val + max(left_sum, right_sum)


# 4. Test if a tree is a valid binary search tree
def is_search_tree(root):
    # Helper function
    def traverse_bst(current_node, previous_value, next_value):
        # Base case
        if current_node is None:
            return True

        if not (previous_value < current_node.val < next_value):
            return False

        # Recursive Call for the Left Subtree:
        left_is_valid = traverse_bst(current_node.left, previous_value, current_node.val)
        # Recursive Call for the Right Subtree:
        right_is_valid = traverse_bst(current_node.right, current_node.val, next_value)

        return left_is_valid and right_is_valid
    
    if root is None:
        return True
    previous_value = float("-inf")
    next_value = float("inf")
    # run the helper function
    return traverse_bst(root, previous_value, next_value)


# 5. Search for a value in a BST
def occurs(root, target):
    while root:
        if target == root.val:
            return True
        elif target < root.val:
            root = root.left
        else:
            root = root.right
    return False


# 6. Insert into a BST (mutating)
def insert(root, target):
    if root is None:
        return TreeNode(target)
    if target < root.val:
        root.left = insert(root.left, target)
    elif target > root.val:
        root.right = insert(root.right, target)
    # if target == root.val, do nothing (no duplicates)
    return root


# Example usage

print("1. In-order traversal")
# Build a sample tree: 
#        5
#       / \
#      3   7
#     /   / \
#    2   6   9
t = TreeNode(5, TreeNode(3, TreeNode(2), None), TreeNode(7, TreeNode(6), TreeNode(9)))
print(inorder(t))  # [2, 3, 5, 6, 7, 9]

print("\n2. Symmetry")
# Build a symmetric tree:
#        1
#       / \
#      2   2
#     /     \
#    3       3
s = TreeNode(1, TreeNode(2, TreeNode(3), None), TreeNode(2, None, TreeNode(3)))
print(is_symmetric(s))  # True
print(is_symmetric(t))  # False

print("\n3. Max root-to-leaf path sum")
print(max_path_sum(t))  # 21
# Build a tree with only one branch
#        1
#       /
#     -10
tree_with_one_branch = TreeNode(1, TreeNode(-10))
print(max_path_sum(tree_with_one_branch))  # -9

print("\n4. Validate BST")
print(is_search_tree(t))  # True
# Break BST property:
bad = TreeNode(5, TreeNode(8), None)
print(is_search_tree(bad))  # False

print("\n5. Occurrence in BST")
print(occurs(t, 6))   # True
print(occurs(t, 4))   # False

print("\n6. Insert into BST")
u = insert(t, 4)
print("After insert 4, in-order:", inorder(u))

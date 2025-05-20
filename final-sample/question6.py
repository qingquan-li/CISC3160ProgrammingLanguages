"""
Design a data structure for binary trees, and write the following functions on binary trees in Python.

1. leaves(tree): This function returns a list of leave values in tree from left to right.
2. deepest(tree): This function returns the value in a deepest node in tree. If there are multiple such values, then the function returns the left-most one.
3. min_max(tree): This function returns a pair (min, max), where min is the minimum element, and max is the maximum element in tree. Note that the tree may not be a binary search tree.
"""

class TreeNode:
    """
    A node in a binary tree.
    Attributes:
      - val: the node’s value
      - left: left child (TreeNode or None)
      - right: right child (TreeNode or None)
    """
    def __init__(self, val, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

# 1) leaves(tree): collect all leaf‐node values left to right
def leaves(root):
    """
    Return a list of values at the leaves of the tree, in left-to-right order.
    A leaf is a node with no children.
    """
    if root is None:
        return []
    # If no children, this node is a leaf
    if root.left is None and root.right is None:
        return [root.val]
    # Otherwise, gather leaves from both subtrees
    return leaves(root.left) + leaves(root.right)

# 2) deepest(tree): find the leftmost value at maximum depth
def deepest(root):
    """
    Return the value of the deepest leaf in the tree.
    If multiple leaves share the max depth, returns the left-most one.
    """
    # Track the best so far
    max_depth = -1
    result = None

    def dfs(node, depth):
        nonlocal max_depth, result
        if node is None:
            return
        # If this is a leaf, check depth
        if node.left is None and node.right is None:
            if depth > max_depth:
                max_depth = depth
                result = node.val
        # Recurse left first to ensure leftmost preference
        dfs(node.left,  depth + 1)
        dfs(node.right, depth + 1)

    dfs(root, 0)
    return result

# 3) min_max(tree): find the minimum and maximum values in the tree
def min_max(root):
    """
    Return a tuple (min_value, max_value) over all nodes in the tree.
    Raises ValueError if the tree is empty.
    """
    if root is None:
        raise ValueError("Tree is empty")

    def helper(node):
        # For an empty subtree, return infinities so as not to affect min/max
        if node is None:
            return (float('inf'), float('-inf'))
        # Get min/max from left and right
        lmin, lmax = helper(node.left)
        rmin, rmax = helper(node.right)
        # Include this node’s value
        current_min = min(node.val, lmin, rmin)
        current_max = max(node.val, lmax, rmax)
        return (current_min, current_max)

    return helper(root)

# === Example Usage ===
if __name__ == "__main__":
    # Build this tree:
    #         10
    #        /  \
    #       5    15
    #      / \     \
    #     2   7     20
    root = TreeNode(10, TreeNode(5, TreeNode(2), TreeNode(7)), TreeNode(15, None, TreeNode(20)))

    print("Leaves:", leaves(root))
    # Leaves: [2, 7, 20]

    print("Deepest leaf value:", deepest(root))
    # Deepest leaf value: 2
    # Explain: Paths: 10→5→2(depth2), 10→5→7(depth2), 10→15→20(depth2)

    print("Min and Max:", min_max(root))
    # Min and Max: (2, 20)

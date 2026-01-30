class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minServiceCenters(root):
    centers = 0

    print("Program started")
    def dfs(node):
        nonlocal centers
        # Null node means it is already covered
        if not node:
            return 2

        left = dfs(node.left)
        right = dfs(node.right)

        # If any child needs service then we place center here
        if left == 0 or right == 0:
            centers += 1
            return 1

        # If any child has a center then that means this node is covered
        if left == 1 or right == 1:
            return 2

        # Otherwise this node needs service
        return 0

    # If root still needs service, add one center
    if dfs(root) == 0:
        centers += 1

    return centers






# Input = {0, 0, null, 0, null, 0, null, null, 0}

root = TreeNode(0)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.left.left.left = TreeNode(0)
root.left.left.left.right = TreeNode(0)

print(minServiceCenters(root))






# Here instead of deciding where to place centers, we decide the state of each node.

# Each node can be in one of 3 states:

# State	Meaning
# 0	This node needs service
# 1	This node has a service center
# 2	This node is already covered





# Strategy Implemented(Greedy + DFS)

# We traverse the tree from bottom to top (postorder):

# If any child needs service (0)
#   place a service center at the current node

# If any child has a service center (1)
#   current node is covered

# Otherwise
#   current node needs service

# At the end:
# If the root still needs service, place one more center.

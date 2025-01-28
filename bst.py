class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert_bst(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root


def build_bst(arr):
    root = None
    for num in arr:
        root = insert_bst(root, num)
    return root


def calculate_height(node):
    if not node:
        return -1  # Return -1 because height is the number of edges
    left_height = calculate_height(node.left)
    right_height = calculate_height(node.right)
    return 1 + max(left_height, right_height)


def tree_to_string(root, level=0, prefix="Root: "):
    if not root:
        return ""
    result = f"{'  ' * level}{prefix}{root.val}\n"
    if root.left or root.right:
        if root.left:
            result += tree_to_string(root.left, level + 1, "L--- ")
        else:
            result += f"{'  ' * (level + 1)}L--- None\n"
        if root.right:
            result += tree_to_string(root.right, level + 1, "R--- ")
        else:
            result += f"{'  ' * (level + 1)}R--- None\n"
    return result


def bst_heights(input_lists):
    result = []
    for bst_list in input_lists:
        root = build_bst(bst_list)
        height = calculate_height(root)
        tree_representation = tree_to_string(root)
        result.append((bst_list, height, tree_representation))
    return result

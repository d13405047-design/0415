class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def dfs_search(node, target):
    if node is None:
        return False
    if node.value == target:
        return True
    return dfs_search(node.left, target) or dfs_search(node.right, target)


if __name__ == '__main__':
    # Construct the tree:
    #         5
    #        / \
    #       3   8
    #      / \     \
    #     2   4   7
    root = TreeNode(5,
                    TreeNode(3,
                             TreeNode(2),
                             TreeNode(4)),
                    TreeNode(8,
                             None,
                             TreeNode(7)))

    if dfs_search(root, 7):
        print('Found')
    else:
        print('Not Found')

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if root in (p, q, None):
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    else:
        return left or right


def tree_create(tree_array):
    root = TreeNode(tree_array[0])
    queue = deque([root])
    i = 1

    while queue is not None and i < len(tree_array):
        current = queue.popleft()

        # 构造左子树
        if i < len(tree_array) and tree_array[i] is not None:
            current.left = TreeNode(tree_array[i])
            queue.append(current.left)
        i += 1

        # 构造右子树
        if i < len(tree_array) and tree_array[i] is not None:
            current.right = TreeNode(tree_array[i])
            queue.append(current.right)
        i += 1

    return root


def preorder_print(root):
    if root is None:
        return
    print(root.val)
    preorder_print(root.left)
    preorder_print(root.right)


def find_node(root, val):
    if root is None:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)



if __name__ == "__main__":
    tree_array = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]

    root = tree_create(tree_array)

    # 找出节点 p 和 q（如 p=5，q=1）
    p = find_node(root, 5)
    q = find_node(root, 1)

    ancestor = lowestCommonAncestor(root, p, q)
    print("最近公共祖先是:", ancestor.val)
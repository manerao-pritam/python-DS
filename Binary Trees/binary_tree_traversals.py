import unittest


class Node:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    # create tree from values
    # values follow this sequence: root, left, right, root.left.left, root.left.right, root.right.left, root.right.right and so on
    def create_tree(self, values) -> Node():
        nodes = [None if v is None else Node(v) for v in values]

        for idx in range(1, len(nodes)):
            node = nodes[idx]
            if not node is None:
                parent_idx = (idx - 1) // 2
                parent = nodes[parent_idx]
                if parent is None:
                    raise f'Parent missing at {parent}'
                setattr(parent, 'left' if idx % 2 else 'right', node)

        self.root = nodes[0] if nodes else None
        return self.root

    # core traversals: Recursive
    def inorder(self, root, result=None) -> list:
        if result is None:
            result = []

        if root:
            self.inorder(root.left, result)
            result += [root.val]
            self.inorder(root.right, result)

        return result

    def preorder(self, root, result=None) -> list:
        if result is None:
            result = []

        if root:
            result += [root.val]
            self.preorder(root.left, result)
            self.preorder(root.right, result)

        return result

    def postorder(self, root, result=None) -> list:
        if result is None:
            result = []

        if root:
            self.postorder(root.left, result)
            self.postorder(root.right, result)
            result += [root.val]

        return result

    # core traversals: Iterative
    def inorder_iter(self, root) -> list:
        if not root:
            return []

        stk, result = [], []

        while root or stk:
            if root:
                stk += [root]
                root = root.left

            else:
                root = stk.pop()
                result += [root.val]
                root = root.right

        return result

    def preorder_iter(self, root) -> list:
        pass

    def postorder_iter(self, root) -> list:
        pass


class TestBinaryTree(unittest.TestCase):
    def test_create_tree(self):
        tree = BinaryTree()

        # valid tree
        root = tree.create_tree([1, 2, 3])
        self.assertEqual(tree.inorder(root), [2, 1, 3])
        self.assertEqual(tree.preorder(root), [1, 2, 3])
        self.assertEqual(tree.postorder(root), [2, 3, 1])

        # valid tree with one child
        root = tree.create_tree([2, 1, 1, 10, 5, None, 4])
        self.assertEqual(tree.inorder(root), [10, 1, 5, 2, 1, 4])
        self.assertEqual(tree.preorder(root), [2, 1, 10, 5, 1, 4])
        self.assertEqual(tree.postorder(root), [10, 5, 1, 4, 1, 2])

        # empty tree
        root = tree.create_tree([])
        self.assertTrue(not tree.inorder(root))
        self.assertTrue(not tree.preorder(root))
        self.assertTrue(not tree.postorder(root))

    def test_inorder_iter(self):
        tree = BinaryTree()
        root = tree.create_tree([2, 1, 1, 10, 5, None, 4])
        self.assertEqual(tree.inorder_iter(root), [10, 1, 5, 2, 1, 4])

        # empty tree
        root = tree.create_tree([])
        self.assertTrue(not tree.inorder_iter(root))


# def main():
#     tree = BinaryTree()
#     root = tree.create_tree([1, 2, 3])
#     print('inorder: ', tree.inorder_iter(root))
#     print('preorder: ', tree.preorder_iter(root))
#     print('postorder: ', tree.postorder_iter(root))
#     print('inorder: ', tree.inorder(root))
#     print('preorder: ', tree.preorder(root))
#     print('postorder: ', tree.postorder(root))
#     root = tree.create_tree([2, 1, 1, 10, 5, None, 4])
#     print('inorder: ', tree.inorder(root))
#     print('preorder: ', tree.preorder(root))
#     print('postorder: ', tree.postorder(root))


if __name__ == '__main__':
    unittest.main()
    # main()

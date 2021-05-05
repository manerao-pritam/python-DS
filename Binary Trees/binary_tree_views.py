from binary_tree_traversals import BinaryTree
from collections import deque, defaultdict, namedtuple
import unittest


class BinaryTreeViews:

    def vertical_traversal(self, root) -> list:
        NodeStatus = namedtuple('NodeStatus', ('key', 'node'))
        nodes_to_visit = deque([NodeStatus(0, root)])
        level_map = defaultdict(list)
        level_map[0] += [root.val]

        while nodes_to_visit:
            level_size = len(nodes_to_visit)

            for _ in range(level_size):
                key, root = nodes_to_visit.popleft()

                if root.left:
                    nodes_to_visit += [NodeStatus(key - 1, root.left)]
                    level_map[key-1] += [root.left.val]

                if root.right:
                    nodes_to_visit += [NodeStatus(key + 1, root.right)]
                    level_map[key+1] += [root.right.val]

        return [level_map[key] for key in sorted(level_map.keys())]

    def left_view(self, root) -> list:
        # its just level order traversal's first node of each layer
        if not root:
            return []

        result, nodes_to_visit = [], deque([root])
        first = root

        while nodes_to_visit:
            level_size = len(nodes_to_visit)

            for i in range(level_size):
                root = nodes_to_visit.popleft()

                # first node in current level
                if not i:
                    first = root

                # children of root
                if root.left:
                    nodes_to_visit += [root.left]

                if root.right:
                    nodes_to_visit += [root.right]

            # add first node to result
            result += [first.val]

        return result

    def right_view(self, root) -> list:
        # its just level order traversal's last node of each layer
        if not root:
            return []

        result, nodes_to_visit = [], deque([root])
        last = root

        while nodes_to_visit:
            level_size = len(nodes_to_visit)

            for i in range(level_size):
                root = nodes_to_visit.popleft()

                if i == level_size - 1:
                    last = root

                if root.left:
                    nodes_to_visit += [root.left]

                if root.right:
                    nodes_to_visit += [root.right]

            result += [last.val]

        return result

    def top_view(self, root) -> list:
        # first node value from each level
        return [] if not root else [level[0] for level in self.vertical_traversal(root)]

    def bottom_view(self, root) -> list:
        # last node value from each level
        return [] if not root else [level[-1] for level in self.vertical_traversal(root)]

    def boundary_view(self, root) -> list:
        def get_left_boundary(root, result):
            # add root and traverse to left node
            if root:
                if root.left:
                    result += [root.val]
                    get_left_boundary(root.left, result)

                elif root.right:
                    result += [root.val]
                    get_left_boundary(root.right, result)

        def get_leaves(root, result):
            if root:
                get_leaves(root.left, result)

                if not root.left and not root.right:
                    result += [root.val]

                get_leaves(root.right, result)

        def get_right_boundary(root, result):
            # traverse to the right node and then add root
            if root:
                if root.right:
                    get_right_boundary(root.right, result)
                    result += [root.val]

                elif root.left:
                    get_right_boundary(root.left, result)
                    result += [root.val]

        result = []
        if root:
            result += [root.val]
            get_left_boundary(root.left, result)

            # this is required for a tree with a single node
            get_leaves(root.left, result)
            get_leaves(root.right, result)

            get_right_boundary(root.right, result)
        return result


class TestBinaryTreeViews(unittest.TestCase):
    def test_left_view(self):
        tree = BinaryTree()
        treeview = BinaryTreeViews()

        # empty tree
        root = tree.create_tree([])
        self.assertTrue(not treeview.left_view(root))

        # single node
        root = tree.create_tree([1])
        self.assertEqual(treeview.left_view(root), [1])

        '''
        valid trees
        '''
        root = tree.create_tree([1, 3, 2])
        self.assertEqual(treeview.left_view(root), [1, 3])

        root = tree.create_tree([1, 2, 3, 4, 6, 9])
        self.assertEqual(treeview.left_view(root), [1, 2, 4])

        root = tree.create_tree(
            [20, 8, 22, 4, 12, None, 25, None, None, 10, 14])
        self.assertEqual(treeview.left_view(root), [20, 8, 4, 10])

    def test_right_view(self):
        tree = BinaryTree()
        treeview = BinaryTreeViews()

        # empty tree
        root = tree.create_tree([])
        self.assertTrue(not treeview.right_view(root))

        # single node
        root = tree.create_tree([1])
        self.assertEqual(treeview.right_view(root), [1])

        '''
        valid trees
        '''
        root = tree.create_tree([1, 3, 2])
        self.assertEqual(treeview.right_view(root), [1, 2])

        root = tree.create_tree([1, 2, 3, 4, 6, 9])
        self.assertEqual(treeview.right_view(root), [1, 3, 9])

        root = tree.create_tree(
            [20, 8, 22, 4, 12, None, 25, None, None, 10, 14])
        self.assertEqual(treeview.right_view(root), [20, 22, 25, 14])

    def test_top_view(self):
        tree = BinaryTree()
        treeview = BinaryTreeViews()

        # empty tree
        root = tree.create_tree([])
        self.assertTrue(not treeview.top_view(root))

        # single node
        root = tree.create_tree([1])
        self.assertEqual(treeview.top_view(root), [1])

        '''
        valid trees
        '''
        root = tree.create_tree([1, 3, 2])
        self.assertEqual(treeview.top_view(root), [3, 1, 2])

        root = tree.create_tree([1, 2, 3, 4, 6, 9])
        self.assertEqual(treeview.top_view(root), [4, 2, 1, 3])

        root = tree.create_tree(
            [20, 8, 22, 4, 12, None, 25, None, None, 10, 14])
        self.assertEqual(treeview.top_view(root), [4, 8, 20, 22, 25])

    def test_bottom_view(self):
        tree = BinaryTree()
        treeview = BinaryTreeViews()

        # empty tree
        root = tree.create_tree([])
        self.assertTrue(not treeview.bottom_view(root))

        # single node
        root = tree.create_tree([1])
        self.assertEqual(treeview.bottom_view(root), [1])

        '''
        valid trees
        '''
        root = tree.create_tree([1, 3, 2])
        self.assertEqual(treeview.bottom_view(root), [3, 1, 2])

        root = tree.create_tree([1, 2, 3, 4, 6, 9])
        self.assertEqual(treeview.bottom_view(root), [4, 2, 9, 3])

        root = tree.create_tree(
            [20, 8, 22, 4, 12, None, 25, None, None, 10, 14])
        self.assertEqual(treeview.bottom_view(root), [4, 10, 12, 14, 25])

    def test_boundary_view(self):
        tree = BinaryTree()
        treeview = BinaryTreeViews()

        # empty tree
        root = tree.create_tree([])
        self.assertTrue(not treeview.boundary_view(root))

        # single node
        root = tree.create_tree([1])
        self.assertEqual(treeview.boundary_view(root), [1])

        '''
        valid trees
        '''
        root = tree.create_tree([1, 3, 2])
        self.assertEqual(treeview.boundary_view(root), [1, 3, 2])

        root = tree.create_tree([1, 2, 3, 4, 6, 9])
        self.assertEqual(treeview.boundary_view(root), [1, 2, 4, 6, 9, 3])

        root = tree.create_tree(
            [20, 8, 22, 4, 12, None, 25, None, None, 10, 14])
        self.assertEqual(treeview.boundary_view(
            root), [20, 8, 4, 10, 14, 25, 22])


# def main():
#     tree = BinaryTree()
#     root = tree.create_tree([1])
#     root = tree.create_tree([1, 3, 2])
#     root = tree.create_tree([1, 2, 3, 4, 6, 9])
#     root = tree.create_tree(
#         [20, 8, 22, 4, 12, None, 25, None, None, 10, 14])
#     treeview = BinaryTreeViews()

#     print(treeview.left_view(root))
#     print(treeview.right_view(root))
#     print(treeview.top_view(root))
#     print(treeview.bottom_view(root))
#     print(treeview.boundary_view(root))


if __name__ == '__main__':
    unittest.main()
    # main()

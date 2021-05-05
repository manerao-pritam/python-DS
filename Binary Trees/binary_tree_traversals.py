from collections import namedtuple, deque, defaultdict
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

    # iterative preorder is simply a level order traversal
    # right child will be pushed first and then the left child
    def preorder_iter(self, root) -> list:
        stk, result = [root], []

        while stk:
            curr = stk.pop()

            if curr:
                result += [curr.val]
                stk += [curr.right, curr.left]

        return result

    # iterative postorder is simply an extended level order traversal with node visited status
    # right child will be pushed first and then the left child
    def postorder_iter(self, root) -> list:

        RootStatus = namedtuple('RootStatus', ('node', 'visited'))
        stk, result = [RootStatus(root, False)], []

        while stk:
            root, visited = stk.pop()

            if visited:
                result += [root.val]
            else:
                if root:
                    stk += [RootStatus(root, True)]
                    stk += [RootStatus(root.right, False)]
                    stk += [RootStatus(root.left, False)]

        return result

    def levelorder(self, root) -> list:
        result, nodes_to_visit = [], deque([root])

        while nodes_to_visit:
            root = nodes_to_visit.popleft()

            if root:
                result += [root.val]
                nodes_to_visit += [root.left, root.right]

        return result

    def reverse_levelorder(self, root) -> list:
        nodes_to_visit, result = deque([root]), deque()

        while nodes_to_visit:
            root = nodes_to_visit.popleft()

            if root:
                result.appendleft(root.val)
                nodes_to_visit += [root.right, root.left]

        return list(result)

    def zig_zag_traversal(self, root) -> list:
        nodes_to_visit, result = deque([root]), []
        level = 0

        # BFS
        while nodes_to_visit:
            size = len(nodes_to_visit)
            level += 1
            children = []

            for _ in range(size):
                root = nodes_to_visit.popleft()

                if root:
                    children += [root.val]
                    nodes_to_visit += [root.left, root.right]

            # reverse children list for even no. level
            result += children[::-1] if not level % 2 else children

        return result

    def diagonal_traversal(self, root) -> list:
        result, left_nodes = [], deque()

        while root:
            result += [root.val]

            if root.left:
                left_nodes.appendleft(root.left)

            if root.right:
                root = root.right
            else:
                root = left_nodes.pop() if left_nodes else None

        return result

        '''
        alternative approach
        '''
        # For each level, add -1 to left node and 0 to right node

        # def update_level_map(key, root):
        #     if key not in level_map:
        #         level_map[key] = [root.val]
        #     else:
        #         level_map[key] += [root.val]

        # if not root:
        #     return []

        # NodeStatus = namedtuple('NodeStatus', ('key', 'node'))
        # nodes_to_visit = deque([NodeStatus(0, root)])
        # level_map = {0: [root.val]}

        # while nodes_to_visit:
        #     level_size = len(nodes_to_visit)

        #     for _ in range(level_size):
        #         key, root = nodes_to_visit.popleft()

        #         if root.left:
        #             nodes_to_visit += [NodeStatus(key - 1, root.left)]
        #             update_level_map(key - 1, root.left)

        #         if root.right:
        #             nodes_to_visit += [NodeStatus(key, root.right)]
        #             update_level_map(key, root.right)

        # result = []
        # for key in sorted(level_map.keys())[::-1]:
        #     result += level_map[key]

        # return result

    def vertical_traversal(self, root) -> list:
        result, positions = [], defaultdict(list)

        def assignPositions(root, x, y):
            if not root:
                return
            assignPositions(root.left, x-1, y+1)
            positions[x] += [(y, root.val)]
            assignPositions(root.right, x+1, y+1)

        assignPositions(root, 0, 0)
        for x in sorted(positions.keys()):
            result += [i[1] for i in sorted(positions[x])]
        return result

        '''
        alternative approach -- need to fix the order of levels
        '''
        # For each level, add -1 to left node and +1 to right node

        # def update_level_map(key, root):
        #     if key not in level_map:
        #         level_map[key] = [root.val]
        #     else:
        #         level_map[key] += [root.val]

        # if not root:
        #     return []

        # NodeStatus = namedtuple('NodeStatus', ('key', 'node'))
        # nodes_to_visit = deque([NodeStatus(0, root)])
        # level_map = {0: [root.val]}

        # # For each level, add -1 to left node and +1 to right node
        # while nodes_to_visit:
        #     level_size = len(nodes_to_visit)

        #     for _ in range(level_size):
        #         key, root = nodes_to_visit.popleft()

        #         if root.left:
        #             nodes_to_visit += [NodeStatus(key - 1, root.left)]
        #             update_level_map(key - 1, root.left)

        #         if root.right:
        #             nodes_to_visit += [NodeStatus(key + 1, root.right)]
        #             update_level_map(key + 1, root.right)

        # return [level_map[key] for key in sorted(level_map.keys())]


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

    def test_preorder_iter(self):
        tree = BinaryTree()
        root = tree.create_tree([2, 1, 1, 10, 5, None, 4])
        self.assertEqual(tree.preorder_iter(root), [2, 1, 10, 5, 1, 4])

        # empty tree
        root = tree.create_tree([])
        self.assertTrue(not tree.preorder_iter(root))

    def test_postorder_iter(self):
        tree = BinaryTree()
        root = tree.create_tree([2, 1, 1, 10, 5, None, 4])
        self.assertEqual(tree.postorder_iter(root), [10, 5, 1, 4, 1, 2])

        # empty tree
        root = tree.create_tree([])
        self.assertTrue(not tree.postorder_iter(root))

    def test_levelorder(self):
        tree = BinaryTree()
        root = tree.create_tree([2, 1, 1, 10, 5, None, 4])
        self.assertEqual(tree.levelorder(root), [2, 1, 1, 10, 5, 4])

        # single node
        root = tree.create_tree([1])
        self.assertEqual(tree.levelorder(root), [1])

        # empty tree
        root = tree.create_tree([])
        self.assertTrue(not tree.levelorder(root))

    def test_reverse_levelorder(self):
        tree = BinaryTree()
        root = tree.create_tree([2, 1, 1, 10, 5, None, 4])
        self.assertEqual(tree.reverse_levelorder(root), [10, 5, 4, 1, 1, 2])

        # single node
        root = tree.create_tree([1])
        self.assertEqual(tree.reverse_levelorder(root), [1])

        # empty tree
        root = tree.create_tree([])
        self.assertTrue(not tree.reverse_levelorder(root))

    def test_zig_zag_traversal(self):
        tree = BinaryTree()
        root = tree.create_tree([2, 1, 1, 10, 5, None, 4])
        self.assertEqual(tree.zig_zag_traversal(root), [2, 1, 1, 10, 5, 4])

        root = tree.create_tree([7, 9, 7, 8, 8, 6, None, 10, 9])
        self.assertEqual(tree.zig_zag_traversal(
            root), [7, 7, 9, 8, 8, 6, 9, 10])

        # single node
        root = tree.create_tree([1])
        self.assertEqual(tree.zig_zag_traversal(root), [1])

        # empty tree
        root = tree.create_tree([])
        self.assertTrue(not tree.zig_zag_traversal(root))

    def test_diagonal_traversal(self):
        tree = BinaryTree()
        root = tree.create_tree([2, 1, 1, 10, 5, None, 4])
        self.assertEqual(tree.diagonal_traversal(root), [2, 1, 4, 1, 5, 10])

        root = tree.create_tree([7, 9, 7, 8, 8, 6, None, 10, 9])
        self.assertEqual(tree.diagonal_traversal(
            root), [7, 7, 9, 8, 6, 8, 9, 10])

        root = tree.create_tree(
            [8, 3, 10, 1, None, 6, 14, None, None, None, None, 4, 7, 13])
        self.assertEqual(tree.diagonal_traversal(
            root), [8, 10, 14, 3, 6, 7, 13, 1, 4])

        # single node
        root = tree.create_tree([1])
        self.assertEqual(tree.diagonal_traversal(root), [1])

        # empty tree
        root = tree.create_tree([])
        self.assertTrue(not tree.diagonal_traversal(root))
        tree = BinaryTree()
        root = tree.create_tree([2, 1, 1, 10, 5, None, 4])
        self.assertEqual(tree.zig_zag_traversal(root), [2, 1, 1, 10, 5, 4])

        root = tree.create_tree([7, 9, 7, 8, 8, 6, None, 10, 9])
        self.assertEqual(tree.zig_zag_traversal(
            root), [7, 7, 9, 8, 8, 6, 9, 10])

        # single node
        root = tree.create_tree([1])
        self.assertEqual(tree.zig_zag_traversal(root), [1])

        # empty tree
        root = tree.create_tree([])
        self.assertTrue(not tree.zig_zag_traversal(root))

    def test_vertical_traversal(self):
        tree = BinaryTree()
        root = tree.create_tree([3, 1, 4, 0, 2, 2])
        self.assertEqual(tree.vertical_traversal(root), [0, 1, 3, 2, 2, 4])

        root = tree.create_tree([7, 9, 7, 8, 8, 6, None, 10, 9])
        self.assertEqual(tree.vertical_traversal(
            root), [10, 8, 9, 9, 7, 6, 8, 7])

        root = tree.create_tree(
            [8, 3, 10, 1, None, 6, 14, None, None, None, None, 4, 7, 13])
        self.assertEqual(tree.vertical_traversal(
            root), [1, 3, 4, 8, 6, 10, 7, 13, 14])

        # single node
        root = tree.create_tree([1])
        self.assertEqual(tree.vertical_traversal(root), [1])

        # empty tree
        root = tree.create_tree([])
        self.assertTrue(not tree.vertical_traversal(root))


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
#     print('preorder: ', tree.preorder_iter(root))
#     print('postorder: ', tree.postorder_iter(root))
#     root = tree.create_tree([7, 9, 7, 8, 8, 6, None, 10, 9])
#     print(tree.zig_zag_traversal(root))
#     root = tree.create_tree([3, 1, 4, 0, 2, 2])
#     root = tree.create_tree([1, 2, 3, 4, 5, 6, 7])
#     print(tree.vertical_traversal(root))
#     root = tree.create_tree(
#         [8, 3, 10, 1, None, 6, 14, None, None, None, None, 4, 7, 13])
#     print(tree.vertical_traversal(root))
#     root = tree.create_tree([])
#     print(tree.diagonal_traversal(root))


if __name__ == '__main__':
    unittest.main()
    # main()

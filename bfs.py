class Node:
    def __init__(self, value, adjs):
        self.adjs = adjs
        self.value = value
        self.isVisited = False

class FinderInGraphDFS:
    isFound = False
    def __init__(self, root):
        self.root = root

    def search(self, goalNode):
        self.isFound = False
        self.searchDFS(self.root, goalNode)

    def searchDFS(self, node, goalNode):
        for adj in node.adjs:
            if adj.value == goalNode.value:
                self.isFound = True
                break
            self.searchDFS(adj, goalNode)

g = Node('g', [])
e = Node('e', [])
f = Node('f', [g])
b = Node('b', [e, f])
c = Node('c', [])
d = Node('d', [f])
a = Node('a', [b, c, d])

s = Node('s', [])

finderInGraphDFS = FinderInGraphDFS(a)
finderInGraphDFS.search(g)
print(finderInGraphDFS.isFound)

finderInGraphDFS.search(f)
print(finderInGraphDFS.isFound)


import Queue

def BFS(node, goalNode):
    queu = Queue.Queue()
    queu.put(node)

    while not queu.empty():
        ele = queu.get()        
        if ele.isVisited == True:
            return
        if ele.value == goalNode.value:
            print('found ->' + ele.value)
        for adj in ele.adjs:
            print('adding ', adj.value)
            queu.put(adj)
        ele.isVisited = True
        print(ele.value)


print('-------bfs------')

BFS(a, g)


#From cake BFS
import unittest

def is_balanced(tree_root):
    queu = []
    minLeafDepth = None
    tree_root.depth = 0
    queu.append(tree_root)

    # Determine if the tree is superbalanced
    while len(queu):
        ele = queu.pop(0)
        if ele.left == None and ele.right == None:
            if minLeafDepth == None:
                minLeafDepth = ele.depth
            minLeafDepth = minLeafDepth if ele.depth > minLeafDepth else ele.depth
            if ele.depth - minLeafDepth > 1:
                return False
        if ele.left is not None:
            ele.left.depth = ele.depth + 1
            queu.append(ele.left)
        if ele.right is not None:
            ele.right.depth = ele.depth + 1
            queu.append(ele.right)
            
    return True

import unittest

#From cake DFS
def is_balanced(tree_root):
    if tree_root is None:
        return True
    stack = []
    minLeafDepth = float('inf')
    tree_root.depth = 0
    stack.append(tree_root)

    # Determine if the tree is superbalanced
    while len(stack):
        ele = stack.pop()
        if ele.left == None and ele.right == None:
            minLeafDepth = minLeafDepth if ele.depth > minLeafDepth else ele.depth
            if ele.depth - minLeafDepth > 1:
                return False
        if ele.right is not None:
            ele.right.depth = ele.depth + 1
            stack.append(ele.right)
        if ele.left is not None:
            ele.left.depth = ele.depth + 1
            stack.append(ele.left)
            
    return True
# Tests

class Test(unittest.TestCase):

    class BinaryTreeNode(object):

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.depth = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right

    def test_full_tree(self):
        tree = Test.BinaryTreeNode(5)
        left = tree.insert_left(8)
        right = tree.insert_right(6)
        left.insert_left(1)
        left.insert_right(2)
        right.insert_left(3)
        right.insert_right(4)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_both_leaves_at_the_same_depth(self):
        tree = Test.BinaryTreeNode(3)
        left = tree.insert_left(4)
        right = tree.insert_right(2)
        left.insert_left(1)
        right.insert_right(9)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_leaf_heights_differ_by_one(self):
        tree = Test.BinaryTreeNode(6)
        left = tree.insert_left(1)
        right = tree.insert_right(0)
        right.insert_right(7)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_leaf_heights_differ_by_two(self):
        tree = Test.BinaryTreeNode(6)
        left = tree.insert_left(1)
        right = tree.insert_right(0)
        right_right = right.insert_right(7)
        right_right.insert_right(8)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_three_leaves_total(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(5)
        right = tree.insert_right(9)
        right.insert_left(8)
        right.insert_right(5)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_both_subtrees_superbalanced(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(5)
        right = tree.insert_right(9)
        right_left = right.insert_left(8)
        right.insert_right(5)
        right_left.insert_left(7)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_both_subtrees_superbalanced_two(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(2)
        right = tree.insert_right(4)
        left.insert_left(3)
        left_right = left.insert_right(7)
        left_right.insert_right(8)
        right_right = right.insert_right(5)
        right_right_right = right_right.insert_right(6)
        right_right_right.insert_right(9)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_only_one_node(self):
        tree = Test.BinaryTreeNode(1)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_linked_list_tree(self):
        tree = Test.BinaryTreeNode(1)
        right = tree.insert_right(2)
        right_right = right.insert_right(3)
        right_right.insert_right(4)
        result = is_balanced(tree)
        self.assertTrue(result)


unittest.main(verbosity=2)


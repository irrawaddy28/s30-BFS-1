'''
102 Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/description/

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Solution:
1. Iterative: Since the tree structure allows us to access nodes starting from the root and moving downward, this process naturally follows a First-In-First-Out (FIFO) order. So we can use queue data structure to perform level order traversal.
First, we insert the root into the queue and iterate over the queue until the queue is empty. In every iteration, we pop from the top of the queue and print the value at the top of the queue. Then, add its left and right nodes to the end of the queue.
https://www.youtube.com/watch?v=AIdppB34TEQ

Time: O(N), Space: O(N) (more specifically, it is O(D), D = diameter of tree)

2. Recursive:
Time: O(N), Space: O(H), H = height of tree
'''
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_level_order(values):
    N = len(values)
    if N == 0:
        return None
    q = deque()
    tree = TreeNode(values[0])
    q.append(tree)
    i=0
    while i < N and q:
        node = q.popleft()
        left_index = 2*i+1
        right_index = left_index + 1
        if left_index < N and values[left_index] is not None:
            node.left = TreeNode(values[left_index])
            q.append(node.left)
        if right_index < N and values[right_index] is not None:
            node.right = TreeNode(values[right_index])
            q.append(node.right)
        i += 1
    return tree

def level_order(root):
    ''' Time: O(N), Space: O(N) '''
    if not root:
        return []

    q = deque()
    q.append(root)
    result = []
    while q:
        level_nodes = []
        K = len(q)
        for _ in range(K):
            root = q.popleft()
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
            level_nodes.append(root.val)
        result.append(level_nodes)
    return result

def level_order_recursive(root):
    ''' Time: O(N), Space: O(H) '''
    def recurse(root, level):
        if not root:
            return
        try:
            result[level].append(root.val)
        except:
            result.append([])
            result[level].append(root.val)
        recurse(root.left, level+1)
        recurse(root.right, level+1)

    if not root:
        return []
    result = []
    recurse(root, 0)
    return result

def run_level_order():
    tests = [([3,9,20,None,None,15,7], [[3],[9,20],[15,7]]),([1],[[1]]),([],[])]
    for test in tests:
        root, ans = test[0], test[1]
        print(f"\nroot = {root}")
        root=build_tree_level_order(root)
        for method in ['iter','recur']:
            if method == 'iter':
                result = level_order(root)
            elif method == 'recur':
                result = level_order_recursive(root)
            print(f"Method {method}: Level order traversal = {result}")
            print(f"Pass: {ans == result}")

run_level_order()
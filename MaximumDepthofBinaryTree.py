
'''
    maxDepth()
    1. If tree is empty then return 0
    2. Else
    (a) Get the max depth of left subtree recursively  i.e.,
    call maxDepth( tree->left-subtree)
    (a) Get the max depth of right subtree recursively  i.e.,
    call maxDepth( tree->right-subtree)
    (c) Get the max of max depths of left and right
    subtrees and add 1 to it for the current node.
    max_depth = max(max dept of left subtree,
    max depth of right subtree)
    + 1
    (d) Return max_depth

'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""



# recursive method

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """ 
    def maxDepth(self, root):

        if root == None:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
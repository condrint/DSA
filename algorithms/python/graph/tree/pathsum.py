# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 18:14:26 2018

@author: Trenton
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: #bases cases and check sum
            return False
        if not (root.left or root.right): #leaf
            if root.val == sum: return True
            return False
        
        left, right = False, False #recurse down tree with boolean values, update sum
        if root.left:
            left = self.hasPathSum(root.left, sum - root.val)
        if root.right:
            right = self.hasPathSum(root.right, sum - root.val)
        return left or right #use or, we only need one True for the tree contain a path = sum
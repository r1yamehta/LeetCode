# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode],sum=0) -> int:
        def combo(root,sum):
            if root==None:
                return 0
            sum=(2*sum)+root.val
            if root.left==None and root.right==None:
                return sum

            return combo(root.left,sum)+combo(root.right,sum)
        return combo(root,0)



        
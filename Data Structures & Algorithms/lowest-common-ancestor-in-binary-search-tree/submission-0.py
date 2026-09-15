# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        LCA = None
        def dfs(current):
            nonlocal LCA
            if current is None or LCA is not None:
                return set()
            
            seen = dfs(current.left) | dfs(current.right)
            seen.add(current.val)
            
            if q.val in seen and p.val in seen and LCA is None:
                LCA = current

            return seen

        dfs(root)
        return LCA

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        s = set(to_delete)
        res = []
        def dfs(root, flag):
            if not root: return None
            toDelete = (root.val in s)
            root.left = dfs(root.left, toDelete)
            root.right = dfs(root.right, toDelete)
            if not toDelete and flag: res.append(root)
            return None if toDelete else root
        dfs(root, True)
        return res
            
# Example 1:

# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]

# Example 2:

# Input: root = [1,2,4,null,3], to_delete = [3]
# Output: [[1,2,4]]

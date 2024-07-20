# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find(n, val, path):
            if n.val == val:
                return True
            if n.left and find(n.left, val, path):
                path += "L"
            elif n.right and find(n.right, val, path):
                path += "R"
            return path
        
        s, d = [], []
        find(root, startValue, s)
        find(root, destValue, d)
        print(s,d)
        while len(s) and len(d) and s[-1] == d[-1]:
            s.pop()
            d.pop()
        print(s,d)
        return "".join("U" * len(s)) + "".join(reversed(d))
    



# Example 1:

# Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
# Output: "UURL"
# Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.

# Example 2:

# Input: root = [2,1], startValue = 2, destValue = 1
# Output: "L"
# Explanation: The shortest path is: 2 → 1.

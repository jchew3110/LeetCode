'''
Given the root of a Binary Search Tree and a target number k, 
return true if there exist two elements in the BST such that their sum is equal to the given target.

https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/616/week-4-august-22nd-august-28th/3908/

'''

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
#         num = []
#         if len(TreeNode) == 0:
#             return False
#         for i in TreeNode:
#             if type(i) != int and type(i) != float:
#                 continue
#             if i is None:
#                 continue
#             else:
#                 if len(num) == 0:
#                     num.append(i)
#                     continue
#                 else:
#                     for n in num:
#                         if n + i == k:
#                             return True
#                     num.append(i)
#         return False                




def findTarget(TreeNode: list, k: int) -> bool:
'''
Non-binary search approach
'''
    num = []
    if len(TreeNode) == 0:
        return False
    for i in TreeNode:
        if type(i) != int and type(i) != float:
            continue
        if i is None:
            continue
        else:
            if len(num) == 0:
                num.append(i)
                continue
            else:
                for n in num:
                    if n + i == k:
                        return True
                num.append(i)
    return False

def test_findTarget():
    assert findTarget([2,1,3], 3) == True
    assert findTarget([2,1,3], 1) == False
    assert findTarget([2,1,3], 4) == True
    assert findTarget([5,3,6,2,4,None,7], 9) == True
    assert findTarget([5,3,6,2,4,None,7], 28) == False
    assert findTarget([1, 2, 3], 6) == False

if __name__ == "__main__":
    test_findTarget()
    print("Everything passed")


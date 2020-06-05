'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。


'''
import tree

class Solution:
    def isValidBST(self, root) -> bool:
        
        def isvalid(root,low,up):
            if root == None:
                return True
            if root.left :
                if root.left.val>=root.val:
                    return False
                if root.left.val <=low or root.left.val>=up:
                    return False
            if root.right:
                if  root.right.val<=root.val:
                    return False
                if root.right.val <=low or root.right.val>=up:
                    return False
            if root.left and not isvalid(root.left,low,root.val):
                return False
            if root.right and not isvalid(root.right,root.val,up):
                return False
            return True
        return isvalid(root,float('-inf'),float('inf'))
s = Solution()
t = tree.Codec()
root = t.deserializeBFS("[3,1,5,0,2,4,6]")
print(s.isValidBST(root))
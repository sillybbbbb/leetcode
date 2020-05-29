import tree

class Solution:
    def isSymmetric(self, root) -> bool:
        Q = []
        Q.append(root)

        while len(Q):
            size = len(Q)
            stack = []
            for i in range(size):
                t = Q.pop(0)
                stack.append(t.val if t else None)
                if t:
                    Q.append(t.left)
                    Q.append(t.right)
            n = len(stack)
            for i in range(n//2):
                if stack[i] != stack[n-i-1]:
                    return False
            
               
        return True 

T = tree.Codec()
tn = T.deserializeBFS(data = "[9,-42,-42,null,76,76,null,null,13,null,13]")
s = Solution()
print(s.isSymmetric(tn))
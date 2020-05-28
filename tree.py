class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import queue
class Codec:

    def serialize(self, root:TreeNode):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        letters = []
        def dfs(node:TreeNode):
            
            if not node:
                letters.append('null')
                return
            else:
                letters.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        i = len(letters)-1
        while letters[i] == 'null':
            letters.pop()
            i-=1
        return letters          
#dfs----------------------------------------------------
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(data):
            if  len(data) == 0:
                return None
            if data[0] == 'null':
                data.pop(0)
                return None
            root = TreeNode(data[0])
            data.pop(0)
            root.left = dfs(data)
            root.right = dfs(data)

            return root 
        if not data:
            return None
        data = data[1:-1].split(',')
        res = dfs(data)
        return res
#bfs----------------------------------------------------
    def serializeBFS(self,root:TreeNode):
        
        Q = queue.Queue()
        Q.put(root)
        s = []
        while not Q.empty():
            root = Q.get()
            if root:
                s.append(root.val)
                Q.put(root.left)
                Q.put(root.right)
            else:
                s.append('null')
        

    def deserializeBFS(self, data):
        if data[0] == "null":
            return None
        
        
        



f = Codec()
dk = f.deserialize("[1,2,3,null,null,4,5,6,null,7]")
ek = f.serialize(dk)
print(ek)
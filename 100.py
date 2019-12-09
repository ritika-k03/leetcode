def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if(p==None and q==None):
            return True
        elif(p==None or q==None):
            return False
        elif q.val!=p.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

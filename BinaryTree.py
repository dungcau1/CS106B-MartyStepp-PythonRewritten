class TreeNode:
    def __init__(self,d=0,l=None,r=None):
        self.data=d
        self.left=l
        self.right=r
    def isLeaf(self):
        return self.leaf==None and self.right==None
class BinaryTree:
    def __init__(self,treenode):
        self.__root=treenode
    def __toStringHelper(self,node):
        if node!=None:
            self.__toStringHelper(node.left)
            print(node.data)
            self.__toStringHelper(node.right)
    def toString(self):
        self.__toStringHelper(self.__root)
    def __containHelper(self,node,val):
        if node==None:
            return False
        elif node.data==val:
            return True
        else:
            return (self.__containHelper(node.left,val) or self.__containHelper(node.right,val))
    def contains(self,val):
        return self.__containHelper(self.__root,val)
    def __toStringSideHelper(self,node,i):
        if node!=None:
            self.__toStringSideHelper(node.right,i+'   ')
            print(i+'%s' %node.data)
            self.__toStringSideHelper(node.left,i+'   ')
    def toStringSide(self):
        self.__toStringSideHelper(self.__root,i='')        

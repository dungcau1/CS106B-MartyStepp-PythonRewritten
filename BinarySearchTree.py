class TreeNode:
    def __init__(self,d=0,l=None,r=None):
        self.data=d
        self.left=l
        self.right=r
    def isLeaf(self):
        return self.left==None and self.right==None
class BinarySet:
    def __init__(self):
        self.__root=None
    """
    Print Sideway
    """
    def toStringSide(self):
        self.__toStringSide(self.__root,i='')
    def __toStringSide(self,node,i):
        if node!=None:
            self.__toStringSide(node.right,i+'   ')
            print(i+'%s' %node.data)
            self.__toStringSide(node.left,i+'   ')
    """
    Get Minimum value
    """
    def getMin(self):
        if self.__root==None:
            raise Exception('You know Python!')
        else:
            return self.__getMin(self.__root)
    def __getMin(self,node):
        if node.left == None:
            return node.data
        else:
            return self.__getMin(node.left)
    """
    Get Maximum value
    """
    def getMax(self):
        if self.__root==None:
            raise Exception('You know Python!')
        else:
            return self.__getMax(self.__root)
    def __getMax(self,node):
        if node.right == None:
            return node.data
        else:
            return self.__getMax(node.right)
    """
    Check Contain
    """
    def __contains(self,node,val):
        if node==None:
            return False
        elif node.data==val:
            return True
        else:
            return (self.__contains(node.left,val) or self.__contains(node.right,val))
    def contains(self,val):
        return self.__contains(self.__root,val)
    """
    IMPORTANT: pass None as parameter mean pointing to nothing, lose address of input
    SOLUTION: 1. pass address of node variable 2. check None before call 3. call its parent node also
    """
    def add(self,val):
        if self.__root==None:
            self.__root=TreeNode(val)
        else:
            self.__add(self.__root,val)   
    def __add(self,node,val):
        if node.data>val:
            if node.left==None:
                node.left=TreeNode(val)
            else:
                self.__add(node.left,val)
        elif node.data<val:
            if node.right==None:
                node.right=TreeNode(val)
            else:
                self.__add(node.right,val)
    """
    Remove
    """
    def remove(self,val):
        self.__remove(self.__root,self.__root,val)
    def __remove(self,parentnode,node,val):
        if node==None:
            pass
        elif node.data>val:
            self.__remove(node,node.left,val)
        elif node.data<val:
            self.__remove(node,node.right,val)
        elif node.data==val:
            if (node.left==None and node.right==None):
                if parentnode.data<val:
                    parentnode.right=None
                else:
                    parentnode.left=None
            elif node.left==None:
                if parentnode.data<val:
                    parentnode.right=node.right
                else:
                    parentnode.left=node.right
            elif node.right==None:
                if parentnode.data<val:
                    parentnode.right=node.left
                else:
                    parentnode.left=node.left
            else:
                mini=self.__getMin(node.right)
                node.data=mini
                self.__remove(node,node.right,mini)        

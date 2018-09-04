class LinkedNode:
    def __init__(self,d=0,n=None):
        self.data=d
        self.next=n
class LinkedList(LinkedNode):
    def __init__(self):
        self.front=None
    def get(self,ind):
        i=0
        cur=self.front
        while i<ind:
            cur=cur.next
            i=i+1
        return cur.data
    def set(self,ind,value):
        i=0
        cur=self.front
        while i<ind:
            cur=cur.next
            i=i+1
        cur.data=value
    def __str__(self):
        list1=[]
        current=self.front
        while current!=None:
            list1.append(current.data)
            current=current.next
        return 'Your linkedlist: [%s]' % ', '.join(map(str, list1))
    def add(self,value):
        if self.front == None:
            self.front=LinkedNode(value)
        else:
            current=self.front
            while current.next!=None:
                current=current.next
            current.next= LinkedNode(value)
    def insert(self,ind,value):
        if ind==0:
            self.front=LinkedNode(value,self.front)
        else:
            cur=self.front
            for i in range(0,ind-1):
                cur=cur.next
            cur.next=LinkedNode(value,cur.next)
    def removeind(self,ind):
        if ind==0:
            self.front=self.front.next
        else:
            cur=self.front
            for i in range(0,ind-1):
                cur=cur.next
            cur.next=cur.next.next

class HashNode:
    def __init__(self,d=0,n=None):
        self.data=d
        self.next=n
class HashSet:
    def __init__(self):
        self.ele=[None]*10
        self.capacity=10
        self.mysize=0
    def HashCode(self,val):
        return abs(val)%self.capacity
    def add(self,val):
        if self.contains(val)==False:
            bucket=self.HashCode(val)
            self.ele[bucket]=HashNode(val,self.ele[bucket])
            self.mysize+=1
    def contains(self,val):
        bucket=self.HashCode(val)
        cur=self.ele[bucket]
        while cur!=None:
            if cur.data==val:
                return True
            cur=cur.next
        return False
    def remove(self,val):
        if self.contains(val)==False:
            return
        bucket=self.HashCode(val)
        if self.ele[bucket].data==val:
            self.ele[bucket]=self.ele[bucket].next
        else:
            cur=self.ele[bucket]
            while cur.next!=None:
                if cur.next.data==val:
                    cur.next=cur.next.next
                    self.mysize-=1
                    return
                if cur.next==None:
                    break
                else:
                    cur=cur.next
    def toString(self):
        for i in range(0,len(self.ele)):
            if self.ele[i]==None:
                print('//')
            else:
                cur=self.ele[i]
                while cur!=None:
                    print(cur.data,end='->')
                    cur=cur.next
                print()       

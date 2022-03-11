class ListNode:
    def __init__(self,val=None,nxt=None):
        self.val = val
        self.next = nxt
class MyLinkedList:
    def __init__(self):
        self.head= None

    def get(self, index: int) -> int:
        temp = self.head
        while index and temp:
            temp =  temp.next
            index-=1
        return temp.val if temp else -1

    def addAtHead(self, val: int) -> None:
        if not self.head: self.head = ListNode(val)
        else:
            keep =self.head
            self.head= ListNode(val)
            self.head.next= keep  
        
        
    def addAtTail(self, val: int) -> None:
        if not self.head: self.head = ListNode(val)
        else:
            temp= self.head
            while temp.next:
                temp = temp.next
            temp.next = ListNode(val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        if not self.head:
            if index==0: self.head = ListNode(val)
        elif not index:
            keep = self.head
            self.head = ListNode(val,keep)
        else:
            temp = self.head
            while index-1 and temp:
                temp = temp.next
                index-=1
            if temp:
                keep = temp.next
                temp.next= ListNode(val)
                temp.next.next = keep
        self.display(self.head)
        

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            keep= self.head
            self.head = self.head.next
            keep.next = None
        else:
            temp = self.head
            while index-1 and temp:
                temp= temp.next
                index-=1
            if temp and temp.next:
                temp.next = temp.next.next       
        
        
        
    def display(self,node):
        print('here')
        temp = node
        while temp:
            print(temp.val)
            temp = temp.next
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
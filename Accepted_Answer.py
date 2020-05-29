from linked_list import ListNode

class Solution:
    def deleteDuplicates(self, head):
        if not head :
            return None
        tracer = head
        outputList = Linked_List()
        while(tracer.next != None):
            if (tracer.val != tracer.next.val):
                outputList.AddTail(tracer.val)
            tracer = tracer.next
        outputList.AddTail(tracer.val)
        return outputList.head
    
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def AddTail(self, value):
        node = ListNode(value)
        if self.head == None:
            self.head = node
            return

        if self.tail == None:
            self.tail = node
            self.head.next = self.tail
            return

        self.tail.next = node
        self.tail = self.tail.next
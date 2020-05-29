class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

    def AddHead(self, value):
        node = ListNode(value)
        if self.head == None:
            self.head = node
            return

        if self.tail == None:
            self.tail = self.head
            self.head = node
            self.head.next = self.tail
            return

        node.next = self.head
        self.head = node

    def printList(self):
        tracer = self.head
        while tracer.next != None:
            print(tracer.val)
            tracer = tracer.next
        print(tracer.val)

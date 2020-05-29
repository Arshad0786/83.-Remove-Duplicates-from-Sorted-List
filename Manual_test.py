from RemoveDuplicatesfromSortedList import Solution
from linked_list import ListNode, Linked_List

a = Linked_List()
a.AddTail(1)
a.AddTail(1)
a.AddTail(1)
a.AddTail(1)
a.AddTail(1)
a.AddTail(1)
a.AddTail(1)
a.AddTail(1)
a.AddTail(2)
a.AddTail(3)
a.AddTail(3)

temp = Solution()
tracer = temp.deleteDuplicates(a.head)
while tracer.next != None:
    print(tracer.val)
    tracer = tracer.next
print(tracer.val)

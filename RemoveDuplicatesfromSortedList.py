from linked_list import ListNode, Linked_List

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

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def find_middle_node(node):
    # count = 0
    faster_node = node
    while(faster_node != None and node != None):
        if(faster_node.next == None):
            faster_node = faster_node.next
        else:
            faster_node = faster_node.next.next

        if faster_node == None:
            break
        node = node.next
    return node


node = ListNode(1)
node.next = ListNode(2)
head = node
node = node.next
node.next = ListNode(3)
node = node.next
node.next = ListNode(4)
node = node.next
# node.next = ListNode(5)
# node = node.next

# print(find_middle_node(head).val)

# def reverse_list(node):
#     pre = None
#     while node != None:

#         temp = node.next
#         temp.next = node.next
#         node.next = pre
#         node = temp
#     return pre


def reverseOrder(head):
    curr = head
    prev = None
    while curr.next is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    curr.next = prev
    return curr.value

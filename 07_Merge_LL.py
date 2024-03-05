class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergetwoLL(l1, l2):
    temp = Node(-1)
    current = temp

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    if l2:
        current.next = l2

    return temp.next


if __name__ == "__main__":
    l1 = Node(1)
    l1.next = Node(3)
    l1.next.next = Node(5)

    l2 = Node(2)
    l2.next = Node(4)
    l2.next.next = Node(6)

    final_list=mergetwoLL(l1,l2)

    while final_list:
        print(final_list.val,end=" ")
        final_list=final_list.next


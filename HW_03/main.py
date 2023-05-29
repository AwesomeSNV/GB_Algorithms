class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def printList(head):
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
    print('None')

def reverse(head):
    previous = None
    current = head

    while current:
        next = current.next
        current.next = previous

        previous = current
        current = next

    return previous

if __name__ == '__main__':

    head = None
    for i in reversed(range(6)):
        head = Node(i + 1, head)

    printList(head)
    head = reverse(head)
    printList(head)
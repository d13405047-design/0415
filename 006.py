class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


if __name__ == '__main__':
    # Create linked list 1 -> 2 -> 3 -> 4
    head = ListNode(1,
                    ListNode(2,
                             ListNode(3,
                                      ListNode(4))))

    # Traverse and print values
    cur = head
    values = []
    while cur is not None:
        values.append(str(cur.value))
        cur = cur.next

    print(' '.join(values))

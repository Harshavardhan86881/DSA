"""Runnable example: a singly linked list with common operations."""


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return f"Node({self.value})"


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def delete_value(self, value):
        if self.head is None:
            return False
        if self.head.value == value:
            self.head = self.head.next
            return True
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next
        if current.next is None:
            return False
        current.next = current.next.next
        return True

    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    def __repr__(self):
        return " -> ".join(str(v) for v in self.to_list()) + " -> None"


if __name__ == "__main__":
    ll = SinglyLinkedList()
    for v in [1, 2, 3]:
        ll.append(v)
    ll.prepend(0)
    print("list:", ll)
    print("delete 2:", ll.delete_value(2))
    print("list:", ll)
    print("to_list:", ll.to_list())

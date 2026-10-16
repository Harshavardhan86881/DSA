"""Runnable example: FIFO queue using collections.deque."""


from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.items:
            raise IndexError("dequeue from empty queue")
        return self.items.popleft()

    def peek(self):
        if not self.items:
            raise IndexError("peek from empty queue")
        return self.items[0]

    def is_empty(self):
        return not self.items


if __name__ == "__main__":
    q = Queue()
    for v in [1, 2, 3]:
        q.enqueue(v)
    print("peek:", q.peek())
    print("dequeue:", q.dequeue())
    print("remaining:", list(q.items))

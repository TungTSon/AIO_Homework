class MyQueue:
    def __init__(self, capacity):
        self._capacity = capacity
        self._queue_list = []

    def is_empty(self):  # check if stack is Empty (the list have no value => Empty)
        return len(self._queue_list) == 0

    def is_full(self):  # check if stack is Full (len of stack == specified capacity => Full)
        return len(self._queue_list) == self._capacity

    def enqueue(self, value):
        if self.is_full():
            # if the queue is full => no place to enqueue => raise exception
            raise ValueError("Queue is full, cannot enqueue anymore")
        self._queue_list.append(value)

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self._queue_list.pop(0)

    def front(self):
        if self.is_empty():
            # if the queue is already empty => raise exception because there is no value to get
            raise ExceValueError("Queue is empty")
        return self._queue_list[0]


if __name__ == "__main__":
    queue1 = MyQueue(capacity=5)    # create a queue of size 5
    print(f"queue.is_tempty() >> {queue1.is_empty()}")
    print("queue.is_full()) >>", queue1.is_full())
    print("------------------------------------------------------------")

    queue1.enqueue(1)
    queue1.enqueue(2)
    print(f">> My queue: {vars(queue1)}")
    print(f"queue.is_tempty() >> {queue1.is_empty()}")
    print("queue.is_full()) >>", queue1.is_full())
    print("------------------------------------------------------------")

    # get current 1st element of the queue
    print(f">> Current 1st element of queue: {queue1.front()}")
    # remove 1st element of the queue
    print(f">> Remove 1st element, value = {queue1.dequeue()}")
    print(f">> My queue: {vars(queue1)}")
    # get current 1st element of the queue
    print(f">> Current 1st element of queue: {queue1.front()}")
    print("------------------------------------------------------------")

    # remove 1st element of the queue
    print(f">> Remove 1st element, value = {queue1.dequeue()}")
    print(f">> My queue: {vars(queue1)}")
    print(f"queue.is_tempty() >> {queue1.is_empty()}")
    print("------------------------------------------------------------")

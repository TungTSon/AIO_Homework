class MyStack:
    def __init__(self, capacity):
        self._capacity = capacity
        self._stack_list = []

    def is_empty(self):  # check if stack is Empty (the list have no value => Empty)
        return len(self._stack_list) == 0

    def is_full(self):  # check if stack is Full (len of stack == specified capacity => Full)
        return len(self._stack_list) == self._capacity

    def pop(self):
        return self._stack_list.pop()

    def push(self, value):
        return self._stack_list.append(value)

    def top(self):
        return self._stack_list[-1]


if __name__ == "__main__":
    stack1 = MyStack(capacity=5)
    print(f"stack1.is_empty() >> {stack1.is_empty()}")

    # push values into stack
    stack1.push(1)
    stack1.push(2)
    stack1.push(-5)

    # check if the stack is Empty. Output should be False
    print(f"stack1.is_empty() >> {stack1.is_empty()}")
    # check if the stack is Full yet. Output should be False
    print(f"stack1.is_full() >> {stack1.is_full()}")

    # get the top value of stack
    print(">> Top value:", stack1.top())
    print("Stack =", vars(stack1)['_stack_list'])

    # pop (remove) the remove the top value
    print("Remove top value of stack----------------------")
    print(">> Top value to be removed:", stack1.pop())
    print("Stack =", vars(stack1)['_stack_list'])   # print out the stack list after popping

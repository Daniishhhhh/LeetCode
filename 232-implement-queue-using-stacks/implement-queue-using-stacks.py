class MyQueue:

    def __init__(self):
        # Two stacks to simulate queue
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        # Always push onto in_stack
        self.in_stack.append(x)

    def pop(self) -> int:
        # Ensure out_stack has elements
        self.peek()
        return self.out_stack.pop()

    def peek(self) -> int:
        # If out_stack is empty, transfer from in_stack
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        # Queue is empty if both stacks are empty
        return not self.in_stack and not self.out_stack

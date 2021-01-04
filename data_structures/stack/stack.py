class Stack(object):
    def __init__(self, limit=10):
        """
        :param limit: 栈大小
        """
        self.stack = []
        self.limit = limit

    def __str__(self):
        return ' '.join([str(i) for i in self.stack])

    def push(self, data):
        """
        入栈，要是栈为满，返回-1
        """
        if len(self.stack) >= self.limit:
            # indicates stack overflow
            return -1
        else:
            self.stack.append(data)

    def pop(self):
        """
        出栈，要是栈空返回-1
        """
        if len(self.stack) <= 0:
            # indicates stack underflow
            return -1
        else:
            return self.stack.pop()

    def peek(self):
        """
        returns the topmost element of the stack
        returns -1 if the stack is empty
        """
        if len(self.stack) <= 0:
            # stack underflow
            return -1
        else:
            return self.stack[len(self.stack) - 1]

    # 判空
    def is_empty(self):
        return self.size() == 0

    # 栈大小
    def size(self):
        return len(self.stack)

    @staticmethod
    def get_code():
        """
        返回目前类代码
        """
        return inspect.getsource(Stack)

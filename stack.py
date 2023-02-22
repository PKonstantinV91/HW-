
class Stack:

    def __init__(self):
        self.list_ = []

    def is_empty(self):
        return self.list_ == []

    def push(self, new_element):
        self.list_.append(new_element)

    def pop(self):
        return self.list_.pop()

    def peek(self):
        if self.is_empty() == False:
            return self.list_[-1]
        else:
            return ''

    def size(self):
        return len(self.list_)
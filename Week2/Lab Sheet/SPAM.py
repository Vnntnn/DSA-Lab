class ArrayStack:
    def __init__(self, data = []):
        self._size = 0
        self._data = data

    def push(self, data):
        self._data = self._data + [data]
        self._size += 1

    def pop(self):
        if not self._size:
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            last_item = self._data[-1]
            del self._data[-1]
            self._size -= 1
            return last_item

    def is_empty(self):
        if not self._size:
            return True
        return False

    def get_stack_top(self):
        if not self._size:
            print("Underflow: Cannot get stack top from an empty list")
            return None
        return self._data[-1]

    def get_size(self):
        return self._size

    def print_stack(self):
        return print(self._data)

SPAM = ArrayStack()

def spamChecking(spamkuy):

    for i in spamkuy:

        if i in "[{(":
            SPAM.push("1")
        if i in "]})":
            SPAM.pop()

    if not SPAM.is_empty():
        print("True")
    else:
        print("False")

spamChecking(input())

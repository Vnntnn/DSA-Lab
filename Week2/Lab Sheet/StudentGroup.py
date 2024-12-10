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

STUDENT_NAME = ArrayStack()
STUDENT_NAME.push("ฉงน")
STUDENT_NAME.push("ละอองดาว")
STUDENT_NAME.push("สกาวเดือน")
STUDENT_NAME.push("เต้")

STUDENT_GROUP1 = []
STUDENT_GROUP2 = []

while STUDENT_NAME.get_size():
    items1 = STUDENT_NAME.pop()
    items2 = STUDENT_NAME.pop()
    STUDENT_GROUP1.append(items1)
    STUDENT_GROUP2.append(items2)

print(f"{STUDENT_GROUP1}\n{STUDENT_GROUP2}")

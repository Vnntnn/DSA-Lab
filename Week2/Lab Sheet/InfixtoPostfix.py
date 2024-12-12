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

def priority(op):
    """Priority operators"""
    if op in ("+", "-"):
        return 1
    if op in ("*", "/"):
        return 2
    return 0

def infixtoPostfix(expression):
    """Convert infix expression to postfix."""
    operators = ArrayStack()
    postfix = []

    for i in expression:
        if i.isalnum():  # Operand
            postfix.append(i)

        elif i == "(":
            operators.push(i)

        elif i == ")":
            while not operators.is_empty() and operators.get_stack_top() != "(":
                postfix.append(operators.pop())
            operators.pop()  # Remove '('
            
        elif i in "+-*/":
            while (not operators.is_empty() and 
                   priority(i) <= priority(operators.get_stack_top())):
                postfix.append(operators.pop())
            operators.push(i)

    while not operators.is_empty():
        postfix.append(operators.pop())

    return "".join(postfix)

expression = input()
postfix_expression = infixtoPostfix(expression)
print(postfix_expression)

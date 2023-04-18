class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

def read_expression(file_path):
    with open(file_path, 'r') as f:
        expression = f.readline().strip()
    return expression.split(" ")

def evaluate_rpn(expression):
    stack = Stack()
    for token in expression:
        if token in '+-*/':
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b
            stack.push(result)
        else:
            stack.push(int(token))
    return stack.pop()

if __name__ == '__main__':
    expression = read_expression('input.txt')
    result = evaluate_rpn(expression)
    print(result)
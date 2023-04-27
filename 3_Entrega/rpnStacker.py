import re

class Regex:
    NUM = re.compile(r'\d+')
    PLUS = re.compile(r'\+')
    MINUS = re.compile(r'-')
    TIMES = re.compile(r'\*')
    DIVIDE = re.compile(r'/')

class RPNCalculator:
    def __init__(self):
        self.stack = []

    def run(self, tokens):
        for token in tokens:
            if token.type == "NUM":
                self.stack.append(int(token.lexeme))
            else:
                b = self.stack.pop()
                a = self.stack.pop()
                if token.type == "PLUS":
                    self.stack.append(a + b)
                elif token.type == "MINUS":
                    self.stack.append(a - b)
                elif token.type == "TIMES":
                    self.stack.append(a * b)
                elif token.type == "DIVIDE":
                    self.stack.append(a / b)
        return self.stack[0]

    def scan(self, expression):
        tokens = []
        for lexeme in expression:
            if Regex.NUM.match(lexeme):
                tokens.append(Token("NUM", lexeme))
            elif Regex.PLUS.match(lexeme):
                tokens.append(Token("PLUS", lexeme))
            elif Regex.MINUS.match(lexeme):
                tokens.append(Token("MINUS", lexeme))
            elif Regex.TIMES.match(lexeme):
                tokens.append(Token("TIMES", lexeme))
            elif Regex.DIVIDE.match(lexeme):
                tokens.append(Token("DIVIDE", lexeme))
            else:
                raise Exception("Unexpected character: " + lexeme)
        return tokens

class Token:
    def __init__(self, token_type, lexeme):
        self.type = token_type
        self.lexeme = lexeme

expression = ['10', 's', '/']

calculator = RPNCalculator()
try:
    tokens = calculator.scan(expression)
    print("Tokens recognized:")
    for token in tokens:
        print("Token " + "[type=" + token.type + ", lexeme= " + token.lexeme+ "]")
    result = calculator.run(tokens)
    print("Saída:", result)
except Exception as e:
    print("Error:", e)
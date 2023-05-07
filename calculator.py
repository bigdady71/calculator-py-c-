class MyClass:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.letter = ''
    
    def set_num(self, n, m, a):
        self.num1 = n
        self.num2 = m
        self.letter = a
    
    def calculate(self):
        if self.letter == '-':
            print(self.num1 - self.num2)
        elif self.letter == '+':
            print(self.num1 + self.num2)
        elif self.letter == '*':
            print(self.num1 * self.num2)
        elif self.letter == '/':
            print(self.num1 / self.num2)
        else:
            print('Incorrect syntax')

obj = MyClass()
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
a = input('Enter operator: ')
obj.set_num(x, y, a)
obj.calculate()

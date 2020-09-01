import re
import math


class Function:
    def __init__(self):
        super(Function, self).__init__()
        self.sin()
        self.cos()
        self.tan()
        # self.operations()
        self.find()

    @staticmethod
    def sin(expr=''):
        get = re.search(r'[0-9]+', expr)
        start0 = re.search('sin', expr)
        start1 = expr.startswith('sin(')
        end1 = expr.endswith(')')
        start2 = re.search(r'cos', expr)
        start3 = re.search(r'tan', expr)
        try:
            if start1 and end1 and re.search(r'[0-9]+', expr):
                if start2 and not start3:
                    return math.sin(math.cos(float(get.group())))
                elif start3 and not start2:
                    return math.sin(math.tan(float(get.group())))
                elif start2 and start3:
                    if expr.find('cos') < expr.find('tan'):
                        return math.sin(math.cos(math.tan(float(get.group()))))
                    else:
                        return math.sin(math.tan(math.cos(float(get.group()))))
                else:
                    return math.sin(float(get.group()))
            elif start0:
                
        except NotImplementedError:
            print('Not a sin function')

    '''@staticmethod
    def operations(expr=''):
        op = ['+', '-', '*', '/']
        get = re.search('[+]+', expr)
        expr1 = re.search('.+\+', expr)
        expr2 = re.search('\+.+', expr)
        print(get)
        for ope in op:
            if ope in expr:
                if ope == '+':
                    return float(expr1.group()[:-1]).__add__(float(expr2.group()[1:]))
                elif ope == '-':
                    return float(expr1.group()[:-1]).__sub__(float(expr2.group()[1:]))
                elif ope == '/':
                    return float(expr1.group()[:-1]).__divmod__(float(expr2.group()[1:]))
                else:
                    return float(expr1.group()[:-1]).__mul__(float(expr2.group()[1:]))'''

    @staticmethod
    def find(expr=''):
        give = False
        op = ['sin', 'cos', 'tan', 'log', 'ln', '√', 'e^', 'sin^-1', 'cos^-1', 'tan^-1', '10^']
        # i = 0
        for ope in op:
            if re.search(ope, expr):
                give = True
                break
        return give

    @staticmethod
    def cos(expr=''):
        get = re.search(r'[0-9]+', expr)
        start1 = expr.startswith('cos(')
        end1 = expr.endswith(')')
        start2 = re.search(r'sin', expr)
        start3 = re.search(r'tan', expr)
        try:
            if start1 and end1 and re.search(r'[0-9]+', expr):
                if start2 and not start3:
                    return math.cos(math.sin(float(get.group())))
                elif start3 and not start2:
                    return math.cos(math.tan(float(get.group())))
                elif start2 and start3:
                    if expr.find('sin') < expr.find('tan'):
                        return math.cos(math.sin(math.tan(float(get.group()))))
                    else:
                        return math.cos(math.tan(math.sin(float(get.group()))))
                else:
                    return math.cos(float(get.group()))
        except SyntaxError:
            print('Not a sin function')

    @staticmethod
    def tan(expr=''):
        get = re.search(r'[0-9]+', expr)
        start1 = expr.startswith('tan(')
        end1 = expr.endswith(')')
        start2 = re.search(r'sin', expr)
        start3 = re.search(r'cos', expr)
        try:
            if start1 and end1 and re.search(r'[0-9]+', expr):
                if start2 and not start3:
                    return math.tan(math.sin(float(get.group())))
                elif start3 and not start2:
                    return math.tan(math.cos(float(get.group())))
                elif start2 and start3:
                    if expr.find('sin') < expr.find('cos'):
                        return math.tan(math.sin(math.cos(float(get.group()))))
                    else:
                        return math.tan(math.cos(math.sin(float(get.group()))))
                else:
                    return math.cos(float(get.group()))
        except SyntaxError:
            print('Not a sin function')


print(Function.find('15+cos(45)'))

def simple_calc(operator, operand1, operand2):
    return eval("{operand1} {operator} {operand2}".format(operand1=operand1, operator=operator, operand2=operand2))

op = str(input())
x = float(input())
y = float(input())

print(simple_calc(op, x, y))

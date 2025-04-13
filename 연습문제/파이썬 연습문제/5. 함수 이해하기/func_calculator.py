def calculator(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        return a/b
    else:
        return;

print(calculator(5, 10, '+'))
print(calculator(5, 10, '-'))
print(calculator(5, 10, '*'))
print(calculator(5, 10, '/'))
print(calculator(5, 10, '='))
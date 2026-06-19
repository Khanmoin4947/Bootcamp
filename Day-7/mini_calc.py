def operators(op):
      if op == '+':
         return lambda x, y: x + y
      elif op == '-':
         return lambda x, y: x - y
      elif op == '*':
         return lambda x, y: x * y
      elif op == '/':
         return lambda x, y: x / y
      else:
         print("Invalid operator")
      
input1 = float(input("Enter an num1: "))
input2 = float(input("Enter an num2: "))
op = input("Enter an operator (+, -, *, /): ")

result = operators(op)
print(result(input1, input2))


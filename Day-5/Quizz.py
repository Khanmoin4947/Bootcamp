def student_report(name, mark):
    print("\n----- Student Report -----")
    print("Name :", name)
    print("mark :", mark)
def add_bonus(mark):
    mark = mark + 5
    print("\nInside Function mark :", mark)
def sum_mark(n):
    if n == 1:
        return 1
    return n + sum_mark(n - 1)
def square(x):
    return x * x
def cube(x):
    return x ** 3
def apply_operation(func, value):
    return func(value)


name = input("Enter Student Name: ")
mark = int(input("Enter mark: "))

student_report(name, mark)

add_bonus(mark)
print("Outside Function mark :", mark)

n = int(input("\nEnter a number for recursive sum: "))
print("Recursive Sum =", sum_mark(n))

print("\nChoose Operation:")
print("1. Square")
print("2. Cube")

choice = int(input("Enter Choice: "))
num = int(input("Enter Number: "))

if choice == 1:
    operation = square
else:
    operation = cube

result = apply_operation(operation, num)

print("\nResult =", result)
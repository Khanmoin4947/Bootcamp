def student_report(name, mark):
    print("\n----- Student Report -----")
    print(f"Name : {name}")
    print(f"mark : {mark}")

name = input("Enter Student Name: ")
mark = int(input("Enter mark: "))

student_report(name, mark)

def add_bonus(mark):
    mark = mark + 5
    print(f"Inside Mark : {mark}")

add_bonus(mark)
print("Outside mark :", mark)

def sum_mark(n):
    if n == 1:
        return 1
    return n + sum_mark(n - 1)

n = int(input("number for recursive sum: "))
print("Recursive Sum =", sum_mark(n))

def square(x):
    return x * x

def cube(x):
    return x ** 3
    
print("Choose Operation:")
print("1. Square")
print("2. Cube")

choice = int(input("Choice: "))
num = int(input("Number: "))

if choice == 1:
    
    print(square(num))

else:
    print(cube(num))
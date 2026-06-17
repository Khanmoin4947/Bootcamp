for i in range(1, 51):
    if i % 7 != 0:
        print(i)



numbers = input("Enter numbers separated by commas: ")

total = sum(int(num.strip()) for num in numbers.split(","))

print("The sum is:", total)

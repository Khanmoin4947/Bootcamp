import random

while True:
    number=random.randint(1, 10)

    print("Generated number:", number)
    if number > 7:
        break

print("total number generated:", number)
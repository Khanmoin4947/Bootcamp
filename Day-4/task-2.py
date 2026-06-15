n=42

while True:
    input_1=int(input("Enter your number: "))

    if input_1==n:
        print("you guessed it")
        break
        
    elif input_1>n:
        print("more than number")
    elif input_1<n:
        print("less than number")

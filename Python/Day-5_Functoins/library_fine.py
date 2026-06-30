c=int(input("number of students: "))

list=[]

for i in range(c):
    a=input("Enter your name: ")
    b=int(input("Enter number of days: "))
    
    fine=0

    if b<=5:
        fine+=5*b
    elif 6<=b<=10:
        fine+=10*b
    else:
        fine+=15*b

    print(f"Total fine for student is: {fine}")


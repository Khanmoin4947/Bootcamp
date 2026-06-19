dict=[
    {"moin": 9.8}, 
    {"farhan": 8.9}, 
    {"navjot": 9.5}, 
    {"sahil": 8.2}
    ]

x=sorted(dict, key=lambda x: list(x.values())[0], reverse=True)

print(x)


b=int(input("Enter a number: "))
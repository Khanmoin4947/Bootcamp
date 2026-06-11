no_of_items=int(input("Enter no of items you want to Buy: "))

items=[]
quantity=[]
price=[]

for i in range(no_of_items):
    product_name=str(input("Product_name: "))
    product_quantity=int(input("Product_quantity: "))
    product_price=int(input("Product_price: "))

    items.append(product_name)
    quantity.append(product_quantity)
    price.append(product_price)

grand_total=0

print("\nBill Summary:")
for i in range(no_of_items):
    total_price=quantity[i]*price[i]
    grand_total=grand_total+total_price
    print(f"{items[i]} {quantity[i]}*{price[i]}={total_price}")

print(f"Grand Total={grand_total}")




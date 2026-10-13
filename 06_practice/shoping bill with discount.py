
# Shopping Receipt

item_name = input("Enter the item name: ")
price = float(input("Enter the price of one item: "))
quantity = int(input("Enter the quantity: "))

subtotal = price * quantity
discount = subtotal * 0.10
total = subtotal - discount

print("\n========== SHOPPING RECEIPT ==========")
print(f"Item Name : {item_name}")
print(f"Price     : Rs. {price:.2f}")
print(f"Quantity  : {quantity}")
print("--------------------------------------")
print(f"Subtotal  : Rs. {subtotal:.2f}")
print(f"Discount  : Rs. {discount:.2f}")
print("--------------------------------------")
print(f"Total     : Rs. {total:.2f}")
print("======================================")
print("       Thank you for shopping!")

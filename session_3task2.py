# Task 2. Write a Python program that takes a user's input for the price of a Zomato order as a string, converts it to a float using type casting, adds 18% GST, and prints the final bill amount.

order_price = input("Enter the Zomato order price: ")

order_price = float(order_price)

gst = order_price * 0.18

final_bill = order_price + gst

print("GST amount: ₹", round(gst, 2))
print("Final bill amount: ₹", round(final_bill, 2))

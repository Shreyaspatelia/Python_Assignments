# Task 3. Given a list of strings representing product prices from Flipkart, like ['199.99', '299.50', '150'], convert all to floats and calculate the total cart value.

prices = ['199.99', '299.50', '150']

float_prices = [float(price) for price in prices]

total = sum(float_prices)

print("Converted prices:", float_prices)
print("Total cart value: ₹", round(total, 2))

# Task 1. Create a list called playlist_ids with 5 integers representing Spotify playlist IDs, then use append() to add a new playlist ID at the end and print the updated list.

playlist_ids = [101, 102, 103, 104, 105]
playlist_ids.append(106)
print(playlist_ids)


# Task 2. Simulate a Flipkart shopping cart: start with a list cart_items containing 't-shirt', 'shoes'. Use extend() to add ['jeans', 'cap'] to the cart, then print the final list of items.

cart_items = ['t-shirt', 'shoes']
cart_items.extend(['jeans', 'cap'])
print(cart_items)


# Task 3. Write a function remove_last_item(order_list) that pops the last item from a Zomato order list and returns the removed item. Test it with a sample order_list.

def remove_last_item(order_list):
    removed_item = order_list.pop()
    return removed_item


order_list = ['pizza', 'burger', 'fries']

result = remove_last_item(order_list)

print("Removed item:", result)
print("Updated order list:", order_list)


# Task 4. Create a tuple called insta_filters with 4 Instagram filter names. Try to update the second filter and observe what error you get. Explain in a comment why this happens.<br><br><em><strong>Hint:</strong> Tuples are immutable, so direct assignment won't work.</em>

insta_filters = ('Clarendon', 'Juno', 'Lark', 'Ludwig')

# Trying to update the second filter
insta_filters[1] = 'Gingham'

# This gives a TypeError because tuples are immutable.

# Python raises a TypeError because tuples are immutable, meaning their elements cannot be changed after the tuple is created


# Task 5. Given two scenarios — storing a user's favorite genres (which may change) and storing a fixed set of IRCTC train classes ('Sleeper', 'AC 3 Tier', 'AC 2 Tier') — choose whether to use a list or tuple for each. Write one sentence explaining your choice for both.

# User's favorite music genres → List

favorite_genres = ['Pop', 'Rock']
favorite_genres.append('Jazz')
print(favorite_genres)

# IRCTC train classes → Tuple

train_classes = ('Sleeper', 'AC 3 Tier', 'AC 2 Tier')
print(train_classes)


# 1. List: A list is suitable for a user's favorite genres because they may add or remove genres.
# 2. Tuple: A tuple is suitable for the fixed set of IRCTC train classes because the values should remain unchanged.


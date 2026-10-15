# Task 5. You received a dataset of ratings as strings from Spotify: ['4.5', '3.0', '5', '4.2']. Use type casting to convert these to floats, then find and print the highest rating.<br><br><em><strong>Hint:</strong> Use the float() function inside a loop or list comprehension.</em>

ratings = ['4.5', '3.0', '5', '4.2']

float_ratings = [float(rating) for rating in ratings]

highest_rating = max(float_ratings)

print("Converted ratings:", float_ratings)
print("Highest rating:", highest_rating)

# Task 5. Write a Python script that intentionally mixes tabs and spaces for indentation, then fix the script so it runs without errors.<br><br><em><strong>Hint:</strong> Use only spaces for indentation, as per Python's best practices.</em>

# Incorrect code:

age = 22

"""if age >= 18:
    print("You are eligible to vote.")
 print("You are an adult.")
"""

# Output: IndentationError: unindent does not match any outer indentation level

# Python uses indentation to identify blocks of code, and mixing tabs and spaces can confuse the interpreter.

# Corrected code:
    

age = 22

if age >= 18:
    print("You are eligible to vote.")
    print("You are an adult.")

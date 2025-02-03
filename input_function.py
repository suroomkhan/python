--  Basic Input
# Asking for user input
name = input("Enter your name: ")
age = input("Enter your age: ")

# Displaying the input values
print(f"Hello, {name}! You are {age} years old.");

-- Validating Numeric Age
# Asking for user input
name = input("Enter your name: ")

# Ensure age is a valid number
while True:
    try:
        age = int(input("Enter your age: "))
        break  # Exit loop if input is valid
    except ValueError:
        print("Invalid input. Please enter a numeric age.")

# Displaying the input values
print(f"Hello, {name}! You are {age} years old.");

-- Storing Name and Age in a Dictionary
# Getting user input
user_data = {
    "name": input("Enter your name: "),
    "age": int(input("Enter your age: "))
}

# Displaying the stored information
print(f"User Info: {user_data}")

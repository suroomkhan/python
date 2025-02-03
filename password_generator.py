import random
import string

def generate_password(length=12):
    """Generate a secure password with uppercase, lowercase, numbers, and special characters."""
    
    if length < 6:
        print("Password length should be at least 6 characters!")
        return None

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        secure_password = generate_password(length)
        if secure_password:
            print(f"\n🔒 Your secure password: {secure_password}")
    except ValueError:
        print("Please enter a valid number for password length!")

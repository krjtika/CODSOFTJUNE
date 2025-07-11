# Task 3: Password Generator
import random
import string
def generate_password(length, use_upper, use_lower, use_digits, use_special):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    if characters == "":
        return "Error: No character type selected."
    password = "".join(random.choice(characters) for _ in range(length))
    return password
print("=== PASSWORD GENERATOR ===")
try:
    length = int(input("Enter desired password length: "))
    print("Include the following in your password:")
    use_upper = input("Uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Digits (0-9)? (y/n): ").lower() == 'y'
    use_special = input("Special characters? (y/n): ").lower() == 'y'
    result = generate_password(length, use_upper, use_lower, use_digits, use_special)
    print("Generated Password:", result)
except ValueError:
    print("Please enter a valid number for password length.")

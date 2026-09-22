import random
import string


def generate_password(length, use_uppercase, use_lowercase,
                      use_numbers, use_symbols):

    characters = ""

    # Add character types selected by the user
    if use_uppercase:
        characters += string.ascii_uppercase

    if use_lowercase:
        characters += string.ascii_lowercase

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    # Check whether at least one character type was selected
    if not characters:
        return None

    # Generate password
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------

print("=" * 45)
print("       🔐 PASSWORD GENERATOR")
print("=" * 45)

while True:

    # Get password length
    try:
        length = int(input("\nEnter password length: "))

        if length <= 0:
            print("❌ Password length must be greater than 0.")
            continue

    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    # Character options
    print("\nChoose password complexity:")

    uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"

    lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"

    numbers = input("Include numbers? (y/n): ").lower() == "y"

    symbols = input("Include special characters? (y/n): ").lower() == "y"

    # Generate password
    password = generate_password(
        length,
        uppercase,
        lowercase,
        numbers,
        symbols
    )

    if password is None:

        print("\n❌ Please select at least one character type.")
        continue

    # Display password
    print("\n" + "=" * 45)
    print("Generated Password:")
    print(password)
    print("=" * 45)

    # Generate another?
    again = input("\nGenerate another password? (y/n): ").lower()

    if again != "y":
        print("\nThank you for using Password Generator! 🔐")
        break
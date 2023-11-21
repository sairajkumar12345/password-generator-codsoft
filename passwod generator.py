import secrets
import string

def generate_password(length=12, uppercase=True, digits=True, special_characters=True):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if special_characters:
        characters += string.punctuation

    if length < 1:
        print("Password length should be at least 1.")
        return None

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def get_user_input():
    length = int(input("Enter the length of the password: "))
    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    special_characters = input("Include special characters? (y/n): ").lower() == 'y'

    return length, uppercase, digits, special_characters

def main():
    print("Welcome to the Password Generator!")
    length, uppercase, digits, special_characters = get_user_input()

    password = generate_password(length, uppercase, digits, special_characters)

    if password:
        print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()

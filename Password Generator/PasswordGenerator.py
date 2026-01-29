import random
import string
import getpass

print("Password Generator and Strength Checker....")

def check_password_strength(password):
    issues = []
    if len(password) < 8:
        issues.append("Password must be at least 8 characters long.")
    if not any(c.lower() for c in password):
        issues.append("Password must include at least one lowercase letter.")
    if not any(c.upper() for c in password):
        issues.append("Password must include at least one uppercase letter.")
    if not any(c.isdigit() for c in password):
        issues.append("Password must include at least one number.")
    if not any(c in string.punctuation for c in password):
        issues.append("Password must include at least one special character.") 
    return issues 
    
def generate_password(num_letters, num_numbers, num_symbols):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    random_letters = random.choices(letters, k=num_letters)
    random_numbers = random.choices(numbers, k=num_numbers) 
    random_symbols = random.choices(symbols, k=num_symbols)
    password_list = random_letters + random_numbers + random_symbols
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password
def main():
    print("Welcome to the Password Strength Checker and Generator!")
    choice = input("Would you like to (1) Check password strength or (2) Generate a password? Enter 1 or 2: ")
    
    if choice == '1':
        password = getpass.getpass("Enter the password to check its strength: ")
        issues = check_password_strength(password)
        if issues:
            print("Your password has the following issues:")
            for issue in issues:
                print(f"- {issue}")
        else:
            print("Your password is strong!")
    
    elif choice == '2':
        num_letters = int(input("Enter how many letters you want in your password: "))
        num_numbers = int(input("Enter how many numbers you want in your password: "))
        num_symbols = int(input("Enter how many symbols you want in your password: "))
        
        password = generate_password(num_letters, num_numbers, num_symbols)
        print(f"Generated password: {password}")
    
    else:
        print("Invalid choice. Please enter 1 or 2.")

main()


import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    character_pool = ""
    
    if use_letters:
        character_pool += string.ascii_letters  # Adds both uppercase and lowercase letters
    
    if use_numbers:
        character_pool += string.digits  # Adds numbers 0-9
    
    if use_symbols:
        character_pool += string.punctuation  # Adds special characters
    
    if not character_pool:
        raise ValueError("No character types selected! Please select at least one character type.")
    
    password = ''.join(random.choice(character_pool) for _ in range(length))
    
    return password

length = int(input("Enter the desired password length: ").strip())
use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
password = generate_password(length, use_letters, use_numbers, use_symbols)
print(f"Generated password: {password}")









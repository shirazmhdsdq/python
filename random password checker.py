import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''

    all_chars = lower + upper + digits + symbols

    if not all_chars:
        return "⚠️ Error: No character types selected."

    # Ensure at least one char from each selected type
    password = []
    if use_upper:
        password.append(random.choice(upper))
    if use_digits:
        password.append(random.choice(digits))
    if use_symbols:
        password.append(random.choice(symbols))
    password.append(random.choice(lower))  # always include at least one lowercase

    # Fill the rest
    while len(password) < length:
        password.append(random.choice(all_chars))

    # Shuffle to avoid predictable order
    random.shuffle(password)
    return ''.join(password)

def main():
    print("🔐 Random Password Generator")
    length = int(input("Enter desired password length (e.g., 12): "))
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_digits, use_symbols)
    print(f"\n✅ Your generated password: {password}")

if __name__ == "__main__":
    main()

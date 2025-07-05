import string
import secrets


def generate_password(length=12, use_letters=True, use_numbers=True, use_symbols=True):
    
    # Build pools
    pools = []
    if use_letters:
        pools.append(string.ascii_letters)
    if use_numbers:
        pools.append(string.digits)
    if use_symbols:
        pools.append(string.punctuation)

    if not pools:
        raise ValueError("At least one character type must be selected.")

    num_types = len(pools)
    if length < num_types:
        raise ValueError(
            f"Password length must be at least {num_types} to include each selected type."
        )

    # Guarantee at least one from each selected pool
    password_chars = [secrets.choice(pool) for pool in pools]

    # Fill the rest of the password
    all_chars = ''.join(pools)
    for _ in range(length - num_types):
        password_chars.append(secrets.choice(all_chars))

    # Shuffle to randomize order
    secrets.SystemRandom().shuffle(password_chars)

    return ''.join(password_chars)


def main():
    print("=== Secure Password Generator ===")
    try:
        length = int(input("Enter desired password length: "))
        use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

        password = generate_password(
            length=length,
            use_letters=use_letters,
            use_numbers=use_numbers,
            use_symbols=use_symbols,
        )
        print(f"\nGenerated Password: {password}")
    except ValueError as ve:
        print(f"Error: {ve}")


if __name__ == "__main__":
    main()

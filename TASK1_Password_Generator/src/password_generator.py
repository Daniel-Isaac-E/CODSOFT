import string
import secrets


def ask_int(prompt: str, min_value: int = 1) -> int:
    """Ask the user for an integer >= min_value."""
    while True:
        raw = input(prompt).strip()
        if not raw.isdigit():
            print("-> Please enter a valid number.")
            continue

        value = int(raw)
        if value < min_value:
            print(f"-> Please enter a number >= {min_value}.")
            continue

        return value


def ask_yes_no(prompt: str) -> bool:
    """Ask a yes/no question. Returns True for yes, False for no."""
    while True:
        choice = input(prompt + " (y/n): ").strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("-> Please answer with 'y' or 'n'.")


def build_charset() -> str:
    """Build the pool of characters based on user choices."""
    charset = ""

    use_lower = ask_yes_no("Include lowercase letters")
    use_upper = ask_yes_no("Include uppercase letters")
    use_digits = ask_yes_no("Include digits")
    use_symbols = ask_yes_no("Include symbols")

    if use_lower:
        charset += string.ascii_lowercase
    if use_upper:
        charset += string.ascii_uppercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        # You can tweak this if you want fewer/more symbols
        charset += string.punctuation

    if not charset:
        print("\nNo character sets selected. Cannot generate password.")
        return ""

    return charset


def generate_password(length: int, charset: str) -> str:
    """Generate a single password of given length using the charset."""
    return "".join(secrets.choice(charset) for _ in range(length))


def main() -> None:
    print("=" * 40)
    print("      PASSWORD GENERATOR (PYTHON)")
    print("=" * 40)

    length = ask_int("Enter password length: ", min_value=4)
    count = ask_int("How many passwords to generate?: ", min_value=1)

    charset = build_charset()
    if not charset:
        # nothing selected -> exit
        return

    print("\nGenerated password(s):\n")
    for i in range(1, count + 1):
        pwd = generate_password(length, charset)
        print(f"{i:>2}. {pwd}")

    print("\nDone. Keep your passwords safe.\n")


if __name__ == "__main__":
    main()

import secrets
import string
import pyperclip
import argparse


def gen_password(length: int = 16, use_symbols: bool = True) -> str:
    """Function get lower and upper symbols as well as digits. 
    Additional symbols will also be used if the use_symbols flag is set. 
    Generation password use library secrets, not random."""
    alphabet = string.ascii_letters + string.digits
    if use_symbols:
        alphabet += "!@#$%^&*()-_=+[]{}<>?,./:;"
    return "".join(secrets.choice(alphabet) for _ in range(length))

if __name__ == "__main__":
    description = "Password generation utils from terminal. After use utils\
        new password copy to clipboard. THIS UTILS NOT SAVE YOUR PASSWORD, \
        JUST GENERATION!"
    p = argparse.ArgumentParser(description=description)
    p.add_argument("--length", type=int, 
                   default=16, help="length password (default 16 symbols)")
    p.add_argument("--symbols", action="store_true", help="use symbols")
    args = p.parse_args()

    password = gen_password(length=args.length, use_symbols=args.symbols)
    
    print(f"New password: {password}\nPassword copy to clipboard")
    pyperclip.copy(password)
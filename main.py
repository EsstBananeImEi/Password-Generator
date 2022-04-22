import argparse
import uuid

from main_component.password_generator import PasswordGenerator
from main_component.string_generator import StringGenerator


def main(password_length: int, salt: str) -> None:
    generator = StringGenerator()
    password_generator = PasswordGenerator(generator, salt)
    password = password_generator.generate_password(password_length)
    generator.display_password(password)


if __name__ == "__main__":
    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument("-l", "--length", type=int, default=10)
    argumentParser.add_argument("-s", "--salt", type=str, default=str(uuid.uuid4()))
    args = argumentParser.parse_args()

    main(args.length, args.salt)

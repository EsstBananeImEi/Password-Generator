import random
import string


class StringGenerator:
    def _ascii_letters(self) -> str:
        return string.ascii_letters

    def _ascii_lowercase(self) -> str:
        return string.ascii_lowercase

    def _ascii_uppercase(self) -> str:
        return string.ascii_uppercase

    def _digits(self) -> str:
        return string.digits

    def _punctuation(self) -> str:
        return string.punctuation

    def generate(self) -> str:
        return (
            self._ascii_letters()
            + self._ascii_lowercase()
            + self._ascii_uppercase()
            + self._digits()
            + self._punctuation()
        )

    def display_password(self, password: str) -> None:
        print(password)
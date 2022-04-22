import random
import string
from dataclasses import dataclass

from main_component.generator import Generator


@dataclass
class PasswordGenerator:
    generator: Generator
    salt: str

    def _shuffle_string(self, password_length: int) -> str:
        return "".join(
            random.sample(self.generator.generate() + self.salt, password_length)
        )

    def generate_password(self, password_length: int) -> str:
        return self._shuffle_string(password_length)

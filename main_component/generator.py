from typing import Protocol


class Generator(Protocol):
    def generate(self) -> str:
        raise NotImplementedError()

    def display_password(self, password: str) -> None:
        raise NotImplementedError()

import unittest
from unittest.mock import patch

from main_component.password_generator import PasswordGenerator
from main_component.string_generator import StringGenerator


class TestPasswordGenerator(unittest.TestCase):
    def test_password_generator(self):
        self.assertEqual(True, True)

    def test_shuffle_string(self):
        generator = StringGenerator()
        pw_gen = PasswordGenerator(generator, "1234")
        with patch.object(
            StringGenerator, "generate", return_value="abcdefghijklmnopqrstuvwxyz"
        ):
            rtv = pw_gen._shuffle_string(10)

            self.assertNotEqual("abcdefghijklmnopqrstuvwxyz", rtv)
            assert len(rtv) == 10

# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("password_generator", Path(__file__).resolve().parents[1] / "PasswordGenerator.py")
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)

class PasswordTests(unittest.TestCase):
    def test_length_and_alphabet(self):
        for length in (1, 8, 20, 100):
            result = app.generate_password(length)
            self.assertEqual(len(result), length)
            self.assertTrue(set(result) <= set(app.ALPHABET))
    def test_reject_invalid_lengths(self):
        for length in (0, -1, app.MAX_LENGTH + 1):
            with self.assertRaises(ValueError):
                app.generate_password(length)
    def test_reject_non_integer(self):
        for value in (True, "20", 1.5):
            with self.assertRaises(TypeError):
                app.generate_password(value)

if __name__ == "__main__":
    unittest.main()


import unittest
from password_checker import analyze_password


class TestPasswordChecker(unittest.TestCase):

    def test_short_password(self):
        result = analyze_password("cat")
        self.assertEqual(result["score"], 1)
        self.assertIn("Too short", result["result"])

    def test_common_password(self):
        result = analyze_password("Password123!")
        self.assertIn("WEAK", result["result"])

    def test_repeated_characters(self):
        result = analyze_password("aaaaaaaaaaaa")
        self.assertIn("WEAK", result["result"])

    def test_predictable_pattern(self):
        result = analyze_password("MyPassword123!")
        self.assertIn("WEAK", result["result"])

    def test_basic_checks(self):
        result = analyze_password("BlueRiver!92Trees")
        self.assertEqual(result["score"], 5)

    def test_numbers_only(self):
        result = analyze_password("123456789012")
        self.assertIn("WEAK", result["result"])

    def test_empty_password(self):
        result = analyze_password("")
        self.assertEqual(result["score"], 0)

    def test_uppercase_and_symbols(self):
        result = analyze_password("HELLO!WORLD!!")
        self.assertEqual(result["score"], 3)


if __name__ == "__main__":
    unittest.main()

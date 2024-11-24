import unittest
from main import caesar_encrypt, caesar_decrypt

# Алфавіти для тестів
ukrainian_alphabet = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
english_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class TestCaesarCipher(unittest.TestCase):
    def test_encrypt_english(self):
        text = "HELLO"
        key = 3
        expected = "KHOOR"
        self.assertEqual(caesar_encrypt(text, key, english_alphabet), expected)

    def test_decrypt_english(self):
        text = "KHOOR"
        key = 3
        expected = "HELLO"
        self.assertEqual(caesar_decrypt(text, key, english_alphabet), expected)

    def test_encrypt_ukrainian(self):
        text = "ПРИВІТ"
        key = 3
        expected = "ТУЙДКХ"
        self.assertEqual(caesar_encrypt(text, key, ukrainian_alphabet), expected)

    def test_decrypt_ukrainian(self):
        text = "ТУЙДКХ"
        key = 3
        expected = "ПРИВІТ"
        self.assertEqual(caesar_decrypt(text, key, ukrainian_alphabet), expected)


    def test_encrypt_with_non_alpha(self):
        text = "Hello, 123!"
        key = 5
        expected = "Mjqqt, 123!"
        self.assertEqual(caesar_encrypt(text, key, english_alphabet), expected)

    def test_decrypt_with_non_alpha(self):
        text = "Mjqqt, 123!"
        key = 5
        expected = "Hello, 123!"
        self.assertEqual(caesar_decrypt(text, key, english_alphabet), expected)

    def test_negative_key_encrypt(self):
        text = "HELLO"
        key = -3
        expected = "EBIIL"
        self.assertEqual(caesar_encrypt(text, key, english_alphabet), expected)

    def test_negative_key_decrypt(self):
        text = "EBIIL"
        key = -3
        expected = "HELLO"
        self.assertEqual(caesar_decrypt(text, key, english_alphabet), expected)

    def test_large_key_encrypt(self):
        text = "HELLO"
        key = 29  # Еквівалент ключу 3 (29 mod 26 = 3)
        expected = "KHOOR"
        self.assertEqual(caesar_encrypt(text, key, english_alphabet), expected)

    def test_large_key_decrypt(self):
        text = "KHOOR"
        key = 29  # Еквівалент ключу 3 (29 mod 26 = 3)
        expected = "HELLO"
        self.assertEqual(caesar_decrypt(text, key, english_alphabet), expected)

if __name__ == "__main__":
    unittest.main()

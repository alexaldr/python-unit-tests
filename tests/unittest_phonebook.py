import unittest
import tempfile
from src.phonebook import PhoneBook


# to run unittest: python -m unittest file_name.py


class PhoneBookTest(unittest.TestCase):

    # setUpClass and tearDownClass are run once for the whole class
    # setUp and tearDown are run before and after each test method.
    def setUp(self) -> None:
        test_dir = tempfile.mkdtemp()
        self.phonebook = PhoneBook(test_dir)

    # method to release resources used during tests
    # will run even if exception be caught
    def tearDown(self) -> None:
        pass

    # sample of test case
    def test_lookup_by_name(self):              # Test Case Name
        self.phonebook.add("Bob", "12345")      # Arrange
        number = self.phonebook.lookup("Bob")   # Act
        self.assertEqual("12345", number)       # Assert

    def test_missing_name_raises_error(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    # this annotation ignores the test
    # @unittest.skip("Work in Progress")
    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_with_different_entries(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Anna", "012345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_with_duplicate_entries(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Sue", "12345")  # identical to Bob
        self.assertFalse(self.phonebook.is_consistent())

    def test_is_consistent_with_duplicate_prefix(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Sue", "123")  # prefix of Bob
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_adds_names_and_numbers(self):
        self.phonebook.add("Sue", "12345")
        # sample of wrong test case construction
        # Each test case must have only ONE assert in
        self.assertEqual({"Sue"}, self.phonebook.get_names())
        self.assertIn("12345", self.phonebook.get_numbers())

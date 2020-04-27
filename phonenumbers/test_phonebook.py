import unittest
from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):

    # setUpClass and tearDownClass are run once for the whole class
    # setUp and tearDown are run before and after each test method.
    def setUp(self) -> None:
        self.phonebook = PhoneBook()
    
    # method to release resources used during tests
    # will run even if exception be caught
    def tearDown(self) -> None:
        pass
    
    def test_lookup_by_name(self):
        self.phonebook.add("Bob", "12345")
        number = self.phonebook.lookup("Bob")
        self.assertEqual("12345", number)
    
    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    # this annotation ignores the test
    # @unittest.skip("Work in Progress")
    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

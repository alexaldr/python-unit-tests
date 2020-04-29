from src.phonebook import PhoneBook
import pytest


# to run pytest: python -m pytest file_name.py


@pytest.fixture         # annotation to test fixture
def phonebook(tmpdir):  # tmpdir is another test fixture
    return PhoneBook(tmpdir)


def test_lookup_by_name(phonebook):  # usage of test fixture as parameter
    phonebook.add("Bob", "1234")
    assert "1234" == phonebook.lookup("Bob")


def test_phonebook_contains_all_names(phonebook):
    phonebook.add("Bob", "1234")
    assert "Bob" in phonebook.get_names()


def test_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("missing")


def test_empty_phonebook_is_consistent(phonebook):
    assert phonebook.is_consistent()


def test_is_consistent_with_different_entries(phonebook):
    phonebook.add("Bob", "12345")
    phonebook.add("Anna", "012345")
    assert phonebook.is_consistent()


def test_is_consistent_with_duplicate_entries(phonebook):
    phonebook.add("Bob", "12345")
    phonebook.add("Sue", "12345")  # identical to Bob
    assert not phonebook.is_consistent()


def test_is_consistent_with_duplicate_prefix(phonebook):
    phonebook.add("Bob", "12345")
    phonebook.add("Sue", "123")  # prefix of Bob
    assert not phonebook.is_consistent()

# this annotation ignores the test
@pytest.mark.skip("Work in Progress")
def test_phonebook_adds_names_and_numbers(phonebook):
    phonebook.add("Sue", "12345")
    # sample of wrong test case construction
    # Each test case must have only ONE assert in
    assert "Sue" in phonebook.get_names()
    assert "12345" in phonebook.get_numbers()

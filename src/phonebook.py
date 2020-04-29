import os
import tempfile


class PhoneBook():

    def __init__(self, cache_directory):
        self.numbers = {}
        self.filename = os.path.join(cache_directory, "phonebook.txt")
        self.cache = open(self.filename, "w")

    def add(self, name, number):
        self.numbers[name] = number

    # to run doctest: python -m pytest --doctest-modules file_name.py
    # OR: python -m doctest file_name.py -v
    def lookup(self, name):
        ''' lookup returns the phone number of given name:
        >>> test_dir = tempfile.mkdtemp()
        >>> phonebook = PhoneBook(test_dir)
        >>> phonebook.add("Bob", "1234")
        >>> phonebook.lookup("Bob")
        '1234'
        '''
        return self.numbers[name]

    def is_consistent(self):
        for name1, number1 in self.numbers.items():
            for name2, number2 in self.numbers.items():
                if name1 == name2:
                    continue
                if number1.startswith(number2):
                    return False
        return True

    def get_names(self):
        return set(self.numbers.keys())

    def get_numbers(self):
        return self.numbers.values()

    def clear(self):
        self.cache.close()
        os.remove(self.filename)

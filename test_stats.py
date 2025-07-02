import unittest
from stats import word_count, count_characters, sort_characters

class TestStats(unittest.TestCase):
    def test_word_count(self):
        self.assertEqual(word_count("hello world"), 2)
        self.assertEqual(word_count(""), 0)
        self.assertEqual(word_count("one two three four"), 4)

    def test_count_characters(self):
        text = "aabbc!"
        result = count_characters(text)
        expected = {'a': 2, 'b': 2, 'c': 1, '!': 1}
        self.assertEqual(result, expected)
        self.assertEqual(count_characters("") , {})

    def test_sort_characters(self):
        char_counts = {'a': 3, 'b': 1, 'c': 2}
        sorted_result = sort_characters(char_counts)
        expected = [
            {'char': 'a', 'num': 3},
            {'char': 'c', 'num': 2},
            {'char': 'b', 'num': 1}
        ]
        self.assertEqual(sorted_result, expected)

if __name__ == "__main__":
    unittest.main()

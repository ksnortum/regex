import unittest
from regex import char_match, start_match, full_match


class Test(unittest.TestCase):
    def test_char_match(self):
        self.assertTrue(char_match("a", "a"), "Regex does not match itself")
        self.assertTrue(char_match(".", "a"), "Regex does not match wildcard")
        self.assertTrue(char_match("", "a"), "No regex should return True")
        self.assertTrue(char_match("", ""), "No regex and input string should return True")
        self.assertFalse(char_match("a", ""), "No input string should return False")
        self.assertFalse(char_match("a", "b"), "Regex does not math input string should return False")

    def test_start_match(self):
        self.assertTrue(start_match("apple", "apple"), "Regex should match itself")
        self.assertTrue(start_match(".pple", "apple"), "Wildcard as first character")
        self.assertTrue(start_match("appl.", "apple"), "Wildcard as last character")
        self.assertTrue(start_match(".....", "apple"), "Wildcard as all characters")
        self.assertFalse(start_match("peach", "apple"), "Regex and string different")

    def test_full_match(self):
        self.assertTrue(full_match("apple", "apple"), "Regex should match itself")
        self.assertTrue(full_match("ap", "apple"), "Regex should match first part of input")
        self.assertTrue(full_match("le", "apple"), "Regex should match last part of input")
        self.assertTrue(full_match("a", "apple"), "Regex should match first char of input")
        self.assertTrue(full_match(".", "apple"), "Regex should match wildcard")
        self.assertTrue(full_match("^app", "apple"), "Caret matches start of string")
        self.assertTrue(full_match("^a", "apple"), "Caret matches start of string")
        self.assertTrue(full_match("^apple", "apple pie"), "Caret matches start of string")
        self.assertTrue(full_match("^", "apple"), "Caret alone matches anything")
        self.assertTrue(full_match("le$", "apple"), "Dollar sign matches end of string")
        self.assertTrue(full_match("a$", "a"), "Okay for pattern to be longer than input if dollar")
        self.assertTrue(full_match("a$", "ba"), "Dollar sing matches end of longer string ")
        self.assertTrue(full_match("^a", "a"), "Okay for pattern to be longer than input if caret")
        self.assertTrue(full_match(".$", "apple"), "Wildcard and dollar meta characters")
        self.assertTrue(full_match("apple$", "tasty apple"), "Dollar matches end of phrase")
        self.assertTrue(full_match("^apple$", "apple"), "Dollar and caret anchors start and end of word")
        self.assertTrue(full_match("", ""), "Empty regex and input strings should return True")

        self.assertFalse(full_match("apwle", "apple"), "Regex and pattern don't match")
        self.assertFalse(full_match("peach", "apple"), "Regex and pattern don't match")
        self.assertFalse(full_match("peachx", "apple"), "Regex can't be longer than pattern")
        self.assertFalse(full_match("^le", "apple"), "Caret not at the beginning of the input string")
        self.assertFalse(full_match("app$", "apple"), "Dollar anchor in middle of word")
        self.assertFalse(full_match("^apple$", "tasty apple"), "Dollar and caret anchors word in phrase")
        self.assertFalse(full_match("^apple$", "apple pie"), "Dollar and caret anchors word in phrase")
        self.assertFalse(full_match("ap$le", "apple"), "Dollar sign not at end of pattern")
        self.assertFalse(full_match("ap^le", "apple"), "Caret not at beginning of pattern")


if __name__ == '__main__':
    unittest.main()

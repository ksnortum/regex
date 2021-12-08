import unittest
from regex import start_match, full_match


class Test(unittest.TestCase):
    
    def test_start_match(self):
        self.assertTrue(start_match("apple", "apple"), "Regex should match itself")
        self.assertTrue(start_match(".pple", "apple"), "Wildcard as first character")
        self.assertTrue(start_match("appl.", "apple"), "Wildcard as last character")
        self.assertTrue(start_match(".....", "apple"), "Wildcard as all characters")
        self.assertFalse(start_match("peach", "apple"), "Regex and string different")

    def test_full_match(self):

        # Empty regex
        self.assertTrue(full_match("", "apple"), "Empty regex should return True")
        self.assertTrue(full_match("", ""), "Empty regex and input strings should return True")

        # Simple matches
        self.assertTrue(full_match("apple", "apple"), "Regex should match itself")
        self.assertTrue(full_match("ap", "apple"), "Regex should match first part of input")
        self.assertTrue(full_match("le", "apple"), "Regex should match last part of input")
        self.assertTrue(full_match("a", "apple"), "Regex should match first char of input")
        self.assertFalse(full_match("apwle", "apple"), "Regex and pattern don't match")
        self.assertFalse(full_match("peach", "apple"), "Regex and pattern don't match")
        self.assertFalse(full_match("peachx", "apple"), "Regex can't be longer than pattern")

        # Wildcard matches
        self.assertTrue(full_match(".", "apple"), "Regex should match wildcard")
        self.assertTrue(full_match("ap.le", "apple"), "Wildcard in middle of input string")

        # Anchors
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
        self.assertFalse(full_match("^le", "apple"), "Caret not at the beginning of the input string")
        self.assertFalse(full_match("app$", "apple"), "Dollar anchor in middle of word")
        self.assertFalse(full_match("^apple$", "tasty apple"), "Dollar and caret anchors word in phrase")
        self.assertFalse(full_match("^apple$", "apple pie"), "Dollar and caret anchors word in phrase")
        self.assertFalse(full_match("ap$le", "apple"), "Dollar sign not at end of pattern")
        self.assertFalse(full_match("ap^le", "apple"), "Caret not at beginning of pattern")

        # Repetitions
        self.assertTrue(full_match("colou?r", "color"), "? matches absent char")
        self.assertTrue(full_match("colou?r", "colour"), "? matches present char")
        self.assertFalse(full_match("colou?r", "colouur"), "? matches only one char")
        self.assertTrue(full_match("col.?r", "color"), "? and wildcard matches only one char")
        self.assertTrue(full_match("a*", "a"), "* matches one character at end of string")
        self.assertTrue(full_match("a*", "aaa"), "* matches several characters at end of string")
        self.assertTrue(full_match("a*", "aaabbb"), "* matches several characters but not end of string")
        self.assertTrue(full_match("colou*r", "color"), "* matches absent char")
        self.assertTrue(full_match("colou*r", "colour"), "* matches present char")
        self.assertTrue(full_match("colou*r", "colouur"), "* matches more than one char")
        self.assertTrue(full_match("col.*r", "color"), "* and wildcard match one char")
        self.assertTrue(full_match("col.*r", "colour"), "* and wildcard match two different chars")
        self.assertTrue(full_match("col.*r", "colr"), "* and wildcard match no chars")
        self.assertTrue(full_match("col.*r", "collar"), "* and wildcard match two different chars")
        self.assertFalse(full_match("col.*r$", "colors"), "* and wildcard with $ anchor")
        self.assertTrue(full_match("no*", "noooooope"), "literal then * repetition, no match at end")
        self.assertTrue(full_match("a+", "a"), "+ matches single character")
        self.assertTrue(full_match("a+", "aaa"), "+ matches several characters")
        self.assertTrue(full_match("a+", "aaabbb"), "+ matches several characters but not end of string")
        self.assertTrue(full_match("no+", "noooooope"), "literal then + repetition, no match at end")
        self.assertTrue(full_match("^no+", "noooooope"), "^ anchor and + repetition, no match at end")


if __name__ == '__main__':
    unittest.main()

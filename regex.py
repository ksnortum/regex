# Regex Engine -- Stage 3

# Match one pattern character to an input character
def char_match(pattern_char, input_char):
    if pattern_char == "" or pattern_char == ".":
        return True

    if input_char == "":
        return False

    return input_char == pattern_char


# Match a pattern and input string of the same or greater length,
# only at the start of the string
def start_match(pattern_string, input_string):
    if pattern_string == "":
        return True

    if input_string == "":
        return False

    if char_match(pattern_string[0], input_string[0]):
        return start_match(pattern_string[1:], input_string[1:])

    return False


# Match a pattern to any length input string
def full_match(pattern_string, input_string):
    # if bad_syntax(pattern_string):
    #     return False

    pattern_len = len(pattern_string)
    input_len = len(input_string)
    # if pattern_len > input_len:
    #     return False

    if pattern_string.startswith("^"):
        return start_match(pattern_string[1:], input_string)

    input_index = 0
    while input_index + pattern_len <= input_len:
        if start_match(pattern_string, input_string[input_index:]):
            return True

        input_index += 1

    return False


def bad_syntax(pattern_string):
    rfind_caret = pattern_string.rfind("^")
    if rfind_caret != -1 and rfind_caret != 0:
        return False

    find_dollar = pattern_string.find("$")
    if find_dollar != -1 and find_dollar != len(pattern_string) - 1:
        return False

    return True


if __name__ == '__main__':
    # print(full_match(*input().split("|")))
    full_match("a$", "ba")  # testing

# Regex Engine -- Stage 5

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
        return pattern_string == "$"

    if pattern_string.find("?") == 1:
        if char_match(pattern_string[0], input_string[0]):
            input_string = input_string[1:]
        pattern_string = pattern_string[2:]
        return start_match(pattern_string, input_string)

    if pattern_string.find("*") == 1:
        if char_match(pattern_string[0], input_string[0]) \
                and len(input_string) > 1 \
                and (not pattern_string.startswith(".")
                     or len(pattern_string) < 3
                     or not char_match(pattern_string[2:3], input_string[0])):
            return start_match(pattern_string, input_string[1:])
        pattern_string = pattern_string[2:]
        return start_match(pattern_string, input_string)

    if pattern_string.find("+") == 1:
        if not char_match(pattern_string[0], input_string[0]):
            return False
        if len(input_string) > 1:
            input_string = input_string[1:]
            if char_match(pattern_string[0], input_string[0]) \
                    and (not pattern_string.startswith(".")
                         or len(pattern_string) < 3
                         or not char_match(pattern_string[2:3], input_string[0])):
                return start_match(pattern_string, input_string)
        pattern_string = pattern_string[2:]
        return start_match(pattern_string, input_string)

    if char_match(pattern_string[0], input_string[0]):
        return start_match(pattern_string[1:], input_string[1:])

    return False


# Match a pattern to any length input string
def full_match(pattern_string, input_string):
    if pattern_string.startswith("^"):
        return start_match(pattern_string[1:], input_string)

    if pattern_string == "":
        return True

    for input_index in range(len(input_string)):
        if start_match(pattern_string, input_string[input_index:]):
            return True

    return False


if __name__ == '__main__':
    print(full_match(*input().split("|")))

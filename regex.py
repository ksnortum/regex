# Regex Engine -- Stage 6
# Credit to user alcala21 for help cleaning up the code

def start_match(pattern_string, input_string):
    if pattern_string == "":
        return True

    if input_string == "":
        return pattern_string == "$"

    if pattern_string[0] == "\\":
        if pattern_string[1:2] == input_string[0]:
            return start_match(pattern_string[2:], input_string[1:])
        return False  # pattern error or escaped character doesn't match

    if pattern_string[0] != input_string[0] and pattern_string[0] != ".":
        if pattern_string[1:2] in ["*", "?"]:
            return start_match(pattern_string[2:], input_string)
        return False

    # Assert input character and pattern character match

    if pattern_string[1:2] == "?":
        return start_match(pattern_string[2:], input_string[1:])

    if pattern_string[1:2] == "*":
        return start_match(pattern_string, input_string[1:]) \
                or start_match(pattern_string[2:], input_string)

    if pattern_string[1:2] == "+":
        return start_match(pattern_string, input_string[1:]) \
                or start_match(pattern_string[2:], input_string[1:])

    return start_match(pattern_string[1:], input_string[1:])


def full_match(pattern_string, input_string):
    if pattern_string == "":
        return True

    if pattern_string[0] == "^":
        return start_match(pattern_string[1:], input_string)

    if start_match(pattern_string, input_string):
        return True

    if input_string == "":
        return pattern_string == "$"

    return full_match(pattern_string, input_string[1:])


if __name__ == '__main__':
    print(full_match(*input().split("|")))

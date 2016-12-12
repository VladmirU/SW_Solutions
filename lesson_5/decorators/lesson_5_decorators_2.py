import sys
import argparse

def check_args(func):
    def wrapper(*args):
        errors = ""
        if len(args) < 4:
            errors += "4 arguments are required!\n"
        if args[0] == "":
            errors += "Original string is required!\n"
        if args[1] == "":
            errors += "Substring for replace is required!\n"
        if args[2] not in ("()", "[]", "{}"):
            errors += "Incorrect brackets are used!\n"
        if args[3] not in ('0', '1'):
            errors += "Wrong variant is used. 0 or 1 should be used!\n"
        if errors != "":
            return errors
        else:
            result = func(*args)
            return result
    return wrapper

def find_substr(string, brackets, variant = '1'):
    count = 0
    substr = ''
    list_substr = []
    for symbol in string:

        if symbol == brackets[0]:
            count += 1

        if count > 0:
            substr += symbol

        if symbol == brackets[1]:
            count -= 1

        if count == 0 and substr != '' and substr != brackets and variant == 0:
            return substr
        elif count == 0 and substr != '' and substr != brackets:
            list_substr.append(substr)
            substr = ''
        elif substr == brackets:
            substr = ''
    return set(sorted(list_substr, key=len, reverse=True))

@check_args
def replace_substr(string, replace_string, brackets, variant):
    replace_string = brackets[0] + replace_string + brackets[1]
    if variant == '0':
        string = string.replace(find_substr(string, brackets, variant), replace_string, 1)
    else:
        for items in find_substr(string, brackets):
            string = string.replace(items, replace_string)

    return string

if __name__ == "__main__":
    print 'ORIGINAL:\n',sys.argv[1]
    print 'REPLACED:\n',replace_substr(*sys.argv[1:])
    raw_input()
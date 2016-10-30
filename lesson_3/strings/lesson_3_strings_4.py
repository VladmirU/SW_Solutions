def find_substr(string, variant=''):
    count = 0
    substr = ''
    list_substr = []
    for symbol in string:

        if symbol == '(':
            count += 1

        if count > 0:
            substr += symbol

        if symbol == ')':
            count -= 1

        if count == 0 and substr != '' and substr != '()' and variant in ['a', 'A']:
            return substr
        elif count == 0 and substr != '' and substr != '()':
            list_substr.append(substr)
            substr = ''
        elif substr == '()':
            substr = ''
    return set(sorted(list_substr, key=len, reverse=True))


def replace_substr(string, replace_string, variant):
    replace_string = '(' + replace_string + ')'
    if variant in ['a', 'A']:
        string = string.replace(find_substr(string, variant), replace_string, 1)
    elif variant in ['b', 'B']:
        for items in find_substr(string):
            string = string.replace(items, replace_string)
    else:
        return 'Wrong variant. Choose "a" or "b"'

    return string

original_string = raw_input('Please, input string to be formatted:\n')
new_sub_str = raw_input('\nPlease, input new string for replace:\n')
user_vaiant = raw_input('\nChoose "a" or "b" variant(a - first substring, b - all substrings)\n')
print ''
print 'ORIGINAL:',original_string
print 'REPLACED:',replace_substr(original_string, new_sub_str, user_vaiant)

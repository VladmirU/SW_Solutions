def is_it_polidrom(original_string):
    filtered_str = ''
    for char in original_string:
        if char.isalpha() or char.isdigit():
            filtered_str += char
    reversed_string = filtered_str[::-1]

    return reversed_string.lower() == filtered_str.lower()
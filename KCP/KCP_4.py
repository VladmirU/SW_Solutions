def del_duplicated_spaces_re(original_string):
    import re

    return re.sub(" +", ' ', original_string)
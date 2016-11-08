def count_substr(path, substring):
    with open(path, 'r') as all_file:
        all_text = all_file.read()
        return all_text.count(substring)
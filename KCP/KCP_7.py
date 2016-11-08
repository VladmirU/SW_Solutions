def get_transpose_matrix(original_matrix):
    transpose_matrix = []
    for row in zip(*original_matrix):
        transpose_matrix.append(list(row))
    return transpose_matrix
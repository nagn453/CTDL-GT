def get_diagonal(input_tuple):
    return tuple(row[i] for i, row in enumerate(input_tuple))
input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
output_tuple = get_diagonal(input_tuple)
print(output_tuple)

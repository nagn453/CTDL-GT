def reverse_dict(my_dict):
    reverse = {value: key for key, value in my_dict.items()}
    return reverse

my_dict = {'a': 1, 'b': 2, 'c': 3}
reversed = reverse_dict(my_dict)
print(reversed)

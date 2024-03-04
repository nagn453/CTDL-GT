def filter_dict(my_dict, filter_func):
    filtered_dict = {key: value for key, value in my_dict.items() if filter_func(key, value)}
    return filtered_dict
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0)
print(filtered_dict)

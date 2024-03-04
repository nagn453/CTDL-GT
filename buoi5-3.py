def merge_dicts(dict1, dict2):
    merge = {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1)|set(dict2)}
    return merge

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merged = merge_dicts(dict1, dict2)
print(merged)

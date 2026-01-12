def deep_copy(obj):
    if type(obj) == dict:
        new_dict = {}
        for key in obj:
            new_dict[deep_copy(key)] = deep_copy(obj[key])
        return new_dict

    if type(obj) == list:
        new_list = []
        for item in obj:
            new_list.append(deep_copy(item))
        return new_list

    if type(obj) == tuple:
        new_tuple = []
        for item in obj:
            new_tuple.append(deep_copy(item))
        return tuple(new_tuple)

    if type(obj) == set:
        new_set = set()
        for item in obj:
            new_set.add(deep_copy(item))
        return new_set
    return obj

data = {
    "name": "Amit",
    "marks": [80, 90],
    "info": ("India", {"city": "Delhi"})
}

copy_data = deep_copy(data)
copy_data["marks"][0] = 999
print("Original:", data)
print("Copy    :", copy_data)


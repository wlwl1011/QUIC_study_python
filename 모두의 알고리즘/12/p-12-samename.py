def find_same_name(a):
    name_dict = {}
    for name in a:
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1

    result = []
    for name in name_dict:
        if name_dict[name] >= 2:
            result.append(name)
    return result


name = ["Tom", "Mike", "Mike", "Tom"]
print(find_same_name(name))

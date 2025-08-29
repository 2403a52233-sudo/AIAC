def sort_list(data):
    nums = [x for x in data if isinstance(x, (int, float))]
    strs = [x for x in data if isinstance(x, str)]
    return sorted(nums) + sorted(strs)

items = [3, "apple", 1, "banana", 2]
print(sort_list(items))
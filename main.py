def second_index(text, some_str):
    ind = text.find(some_str)
    result = text.find(some_str, ind + 1)
    if result == -1:
        return None
    return result

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
def find_max(lst):
    if not lst:
        return None
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

def test_find_max():
    test_cases = [
        ([3, 1, 4, 1, 5, 9, 2, 6, 5], 9),
        ([1, 2, 3, 4, 5], 5),
        ([-5, -10, -3, -1], -1),
        ([100], 100),
        ([], None)
    ]
    
    for i, (input_lst, expected) in enumerate(test_cases):
        result = find_max(input_lst)
        if result == expected:
            print(f"Test case {i+1} passed.")
        else:
            print(f"Test case {i+1} failed: find_max({input_lst}) = {result}, expected {expected}")

test_find_max()

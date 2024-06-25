def remove_duplicates(lst):
    return list(set(lst))

def test_remove_duplicates():
    test_cases = [
        ([1, 2, 2, 3, 4, 4, 5], [1, 2, 3, 4, 5]),
        ([1, 1, 1, 1, 1], [1]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1, 5, 4], [1, 2, 3, 4, 5]),
        ([], [])
    ]
    
    for i, (input_lst, expected) in enumerate(test_cases):
        result = remove_duplicates(input_lst)
        if sorted(result) == sorted(expected):
            print(f"Test case {i+1} passed.")
        else:
            print(f"Test case {i+1} failed: remove_duplicates({input_lst}) = {result}, expected {expected}")

test_remove_duplicates()

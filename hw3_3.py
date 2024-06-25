def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def test_factorial():
    test_cases = [
        (0, 1),
        (1, 1),
        (5, 120),
        (7, 5040),
        (-1, None)
    ]
    
    for i, (input_n, expected) in enumerate(test_cases):
        result = factorial(input_n)
        if result == expected:
            print(f"Test case {i+1} passed.")
        else:
            print(f"Test case {i+1} failed: factorial({input_n}) = {result}, expected {expected}")

test_factorial()

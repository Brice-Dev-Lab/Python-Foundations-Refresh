"""This is a test module to check edge cases for the median function"""


def run_all_tests(get_median):
    test_cases = [
        ("Empty List", [], None),
        ("Odd Length", [3, 1, 2], 2),
        ("Even Length", [1, 2, 3, 4], 2),
    ]

    for name, input_data, expected in test_cases:
        result = get_median(input_data)
        if result == expected:
            print(f"✅ {name} passed")
        else:
            print(f"❌ {name} failed (expected {expected}, got {result})")

from app import add_numbers

def test_add_numbers():
    # This checks if function correctly adds 2 + 3 to get 5
    assert add_numbers(2, 3) == 5

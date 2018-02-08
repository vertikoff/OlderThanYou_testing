def test_sum_function():
    from number_manipulation import return_sum
    case_one = return_sum([5])
    case_two = return_sum([3, 7, -2])
    case_three = return_sum([-6, -90, -40, 26])
    case_four = return_sum([6.9, 3.2, -4])
    case_five = return_sum([-3.2, -1.8, -9.36, -872])

    assert case_one == 5
    assert case_two == 8
    assert case_three == -110
    # vertikoff - setting tollerance threshold here
    tollerance = 0.00000001
    assert case_four - 6.1 < tollerance
    assert case_five + 886.36 < tollerance

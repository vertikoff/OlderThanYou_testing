def test_sum_function():
    import pytest
    from number_manipulation import NumberListManipulator
    case_one = NumberListManipulator([5, 0])
    case_two = NumberListManipulator([3, 7, -2])
    case_three = NumberListManipulator([-6, -90, -40, 26])
    case_four = NumberListManipulator([6.9, 3.2, -4])
    case_five = NumberListManipulator([-3.2, -1.8, -9.36, -872])

    assert case_one.sum == 5
    assert case_two.sum == 8
    assert case_three.sum == -110
    # vertikoff - setting tollerance threshold here
    tollerance = 0.00000001
    assert case_four.sum - 6.1 < tollerance
    assert case_five.sum + 886.36 < tollerance

    with pytest.raises(TypeError):
        NumberListManipulator([8, "str"])
    with pytest.raises(ValueError):
        NumberListManipulator([])

def test_limits_function():
    from number_manipulation import return_limits
    output = return_limits([5])
    assert output == [5, 5]

    output = return_limits([-1, -3, 4, 0, 2])
    assert output == [-3, 4]

    tolerance = 0.00000001
    output = return_limits([3.3, -5.7, 9, -6.7])
    assert output[0] + 6.7 < tolerance
    assert output[1] - 9 < tolerance
    
    pass

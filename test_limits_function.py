def test_limits_function():
    from number_manipulation import NumberListManipulator
    import pytest

    with pytest.raises(TypeError):
        output = NumberListManipulator((1, 2, 3))
        output.limits
    with pytest.raises(ValueError):
        NumberListManipulator([])
        output.limits
    with pytest.raises(TypeError):
        NumberListManipulator([1, 's'])
        output.limits

    output = NumberListManipulator([5, 5])
    assert output.limits == (5, 5)

    output = NumberListManipulator([-1, -3, 4, 0, 2])
    assert output.limits == (-3, 4)

    tolerance = 0.00000001
    output = NumberListManipulator([3.3, -5.7, 9, -6.7])
    assert output.limits[0] + 6.7 < tolerance
    assert output.limits[1] - 9 < tolerance

    pass

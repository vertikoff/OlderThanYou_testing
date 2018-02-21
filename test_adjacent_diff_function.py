def test_max_adjacent():
    import pytest
    from number_manipulation import NumberListManipulator
    assert NumberListManipulator([1, 2]).max_adjacent == 1
    assert NumberListManipulator([0, 1, 3, 4, 5, 6,
                                  7, 8, 9, 10]).max_adjacent == 2
    assert NumberListManipulator([1, 2, 3]).max_adjacent == 1
    assert NumberListManipulator([1, 2, 2.5, 5]).max_adjacent == 2.5
    assert NumberListManipulator([-1, 1, -2]).max_adjacent == 3
    with pytest.raises(TypeError):
        output = NumberListManipulator(["str1", "str2"])
        output.max_adjacent
    with pytest.raises(ValueError):
        output = NumberListManipulator([1])
        output.max_adjacent
    with pytest.raises(ValueError):
        output = NumberListManipulator([])
        output.max_adjacent
    return

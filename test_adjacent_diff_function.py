def test_max_adjacent():
    import pytest
    from number_manipulation import list_max_adjacent
    assert list_max_adjacent([1, 2]) == 1
    assert list_max_adjacent([0, 1, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
    assert list_max_adjacent([1, 2, 3]) == 1
    assert list_max_adjacent([1, 2, 2.5, 5]) == 2.5
    assert list_max_adjacent([-1, 1, -2]) == 3
    pytest.raises(TypeError, list_max_adjacent,["str1","str2"])
    pytest.raises(ValueError, list_max_adjacent,[1])
    pytest.raises(ValueError, list_max_adjacent,[])
    return

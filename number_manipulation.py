# @vertikoff create sum function here
def return_sum(num_list):
    sum = 0
    for num in num_list:
        sum += num

    return(sum)


# @jlongc12 create tuple min/max function here
def return_limits(num_list):
    limits = (min(num_list), max(num_list))
    return limits


# @mackenna95 create max difference function here
def list_max_adjacent(num_list):   
    """
    Returns the maximum difference between two adjacent numbers in an array
    :param num_list : list of ints and floats
    :returns max_diff : the maximum difference between two adjacent numbers in num_list
    :raises : ImportError, TypeError, ValueError
    """

    import numpy as np

    try:

        diff = np.diff(num_list)
        abs_diff = np.absolute(diff)
        max_diff = np.max(abs_diff)

    except ImportError:
        raise ImportError('ImportError returned')
    except TypeError:
        raise TypeError('Invalid type (expects int or float).')
    except ValueError:
        raise ValueError('ValueError returned')

    return max_diff

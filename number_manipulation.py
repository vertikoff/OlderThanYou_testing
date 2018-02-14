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
    Returns maximum difference between two adjacent numbers
    :param num_list: list of numbers
    :returns max_diff: maximum difference between two adjacent numbers
    :raises TypeError: Input is not a list
    :raises ValueError: List is empty
    :raises ImportError: Importing unknown packages
    """
    import logging
    import numpy as np

    logging.basicConfig(filename="number_manipulation_log.txt",
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    try:

        diff = np.diff(num_list)
        abs_diff = np.absolute(diff)
        max_diff = np.max(abs_diff)

    except ImportError:
        logging.debug('ImportError: Import packages not found.')
        raise ImportError('Import packages not found.')
    except TypeError:
        logging.debug('TypeError: not a list')
        raise TypeError('Invalid type (expects int or float).')
    except ValueError:
        logging.debug('ValueError: empty list')
        raise ValueError('ValueError returned')

    return max_diff

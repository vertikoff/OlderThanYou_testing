# @vertikoff create sum function here
def return_sum(num_list):
    """

    Takes the values passed in as num_list and returns their sum
    :param num_list:        mixed list of ints and floats
    :returns sum:           the sum of the ints and floats passed in num_list
    :raises TypeError:      value not int or float
    :raises ValueError:     list is empty
    :raises ImportError:    packages not found
    """

    import logging
    logging.basicConfig(filename="number_manipulation_log.txt",
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    if not num_list:
        logging.warning('Your list is empty')
        raise ValueError("list is empty")

    sum_list = 0
    try:
        for num in num_list:
            sum_list += num
    except TypeError:
        logging.debug('TypeError: non-numeric')
        raise TypeError("List contains non-numeric elements.")
    except ValueError:
        logging.debug('ValueError: empty list')
        raise ValueError("List is empty.")
    except ImportError:
        logging.debug('ImportError: packages not found')
        raise ImportError("Import packages not found.")

    logging.info("Success: sum returned.")
    return sum_list


# @jlongc12 create tuple min/max function here
def return_limits(num_list):

    """"

    Returns the minimum and maximum value of a list of numbers.
    :param num_list:        mixed list of ints and floats
    :return limits:         a tuple in the form (minimum_value maximum_value)
    :raises TypeError:      list contains strings or input is not a list
    :raises ValueError:     list is empty
    :raises ImportError:    packages not found
    """
    import logging
    logging.basicConfig(filename="number_manipulation_log.txt",
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    if len(num_list) == 1:
        logging.warning('Your list only contains 1 element.')

    if not isinstance(num_list, list):
        logging.debug('TypeError: not a list')
        raise TypeError('Input is not a list.')

    if not num_list:
        logging.debug('ValueError: empty list')
        raise ValueError("List is empty.")

    try:
        min(num_list)
    except TypeError:
        if all(isinstance(x, int) or isinstance(x, float) for x in num_list):
            logging.debug('TypeError: non-numeric')
            raise TypeError('List contains non-numeric elements.')
        else:
            logging.debug('TypeError: unknown')
            raise TypeError('Unknown.')
    except ValueError:
        logging.debug('ValueError: unknown')
        raise ValueError('Unknown.')
    except ImportError:
        logging.debug('ImportError: packages not found')
        raise ImportError('Import packages not found.')

    limits = (min(num_list), max(num_list))
    logging.info('Success: limits returned.')
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

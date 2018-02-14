# @vertikoff create sum function here
def return_sum(num_list):
    sum = 0
    for num in num_list:
        sum += num

    return(sum)


# @jlongc12 create tuple min/max function here
def return_limits(num_list):

    """"

    Returns the minimum and maximum value of a list of numbers.
    :param num_list:        List of numbers
    :return limits:         Tuple in the form (num_list_minimum_value num_list_maximum_value)
    :raises TypeError:      Triggered when list contains strings or input is not a list
    :raises ValueError:     Triggered when list is empty
    :raises ImportError:    Triggered when trying to import unknown packages
    """
    import logging
    logging.basicConfig(filename="number_manipulation_log.txt", format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    if len(num_list) == 1:
        logging.warning('Your list only contains 1 element.')

    try:
        min(num_list)
    except TypeError:
        if not isinstance(a, list):
            logging.debug('TypeError: Your input is not a list.')
        elif all(isinstance(x, int) or isinstance(x, float) for x in num_list):
            logging.debug('TypeError: Your input contains non-numeric elements.')
        else:
            logging.debug('TypeError: Unknown.')
    except ValueError:
        if not a:
            logging.debug('ValueError: Your list is empty')
        else:
            logging.debug('ValueError: Unknown.')
    except ImportError:
        logging.debug('Import packages not found.')

    limits = (min(num_list), max(num_list))
    logging.info('No issues.')
    return limits


# @mackenna95 create max difference function here
def list_max_adjacent(num_list):
    import numpy as np

    if len(num_list) == 0:
        max_diff = 0
    elif len(num_list) == 1:
        max_diff = 0
    else:
        diff = np.diff(num_list)
        abs_diff = np.absolute(diff)
        max_diff = np.max(abs_diff)

    return max_diff

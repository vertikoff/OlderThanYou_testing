class NumberListManipulator:
"""

Determines, sum, max, min, and max adjacent diff for given list
:param num_list: list of ints and floats
:attr num_list: list passed by user
:attr sum: sum of num_list
:attr limits: a tuple in the form (minimum_value maximum_value)
:attr max_adjacent: max diff between two adjacent members of list
"""

    def __init__(self, num_list=None):
        self.num_list = num_list
        self.sum = None
        self.limits = None
        self.max_adjacent = None
        self.set_sum()
        self.set_limits()
        self.set_max_adjacent()

    # @vertikoff create sum function here
    def set_sum(self):
        """

        Determines the sum of a list of numbers.
        :param self:            instance of class NumberListManipulator
        :sets sum:           the sum of the ints and floats passed in num_list
        :raises TypeError:      value not int or float
        :raises ValueError:     list is empty
        :raises ImportError:    packages not found
        """

        import logging
        logging.basicConfig(filename="number_manipulation_log.txt",
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')

        if not self.num_list:
            logging.warning('Your list is empty')
            raise ValueError("list is empty")

        sum_list = 0
        try:
            for num in self.num_list:
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
        self.sum = sum_list

    # @jlongc12 create tuple min/max function here
    def set_limits(self):

        """"

        Determines the minimum and maximum value of a list of numbers.
        :param num_list:        mixed list of ints and floats
        :sets limits:         a tuple in the form (minimum_value maximum_value)
        :raises TypeError:      list contains strings or input is not a list
        :raises ValueError:     list is empty
        :raises ImportError:    packages not found
        """
        import logging
        logging.basicConfig(filename="number_manipulation_log.txt",
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')

        if len(self.num_list) == 1:
            logging.warning('Your list only contains 1 element.')

        if not isinstance(self.num_list, list):
            logging.debug('TypeError: not a list')
            raise TypeError('Input is not a list.')

        if not self.num_list:
            logging.debug('ValueError: empty list')
            raise ValueError("List is empty.")

        try:
            min(self.num_list)
        except TypeError:
            if all(isinstance(x, int) or
                   isinstance(x, float) for x in self.num_list):
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

        limits = (min(self.num_list), max(self.num_list))
        logging.info('Success: limits returned.')
        self.limits = limits

    # @mackenna95 create max difference function here
    def set_max_adjacent(self):
        """

        Determines maximum difference between two adjacent numbers
        :param num_list:        list of numbers
        :sets max_diff:      maximum difference between two adjacent numbers
        :raises TypeError:      input is not a list
        :raises ValueError:     list is empty
        :raises ImportError:    importing unknown packages
        """
        import logging
        import numpy as np

        logging.basicConfig(filename="number_manipulation_log.txt",
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')

        try:

            diff = np.diff(self.num_list)
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

        self.max_adjacent = max_diff

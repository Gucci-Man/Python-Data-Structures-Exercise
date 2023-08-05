def compact(lst):
    """Return a copy of lst with non-true elements removed.

    >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
    [1, 2, 'All done']
    """
    # new_list = [item for item in lst if not item == True]
    return [val for val in lst if val]

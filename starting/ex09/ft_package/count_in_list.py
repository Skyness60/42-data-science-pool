
def count_in_list(lst, value):
    """Return how many times 'value' appears in 'lst'."""
    if not isinstance(lst, list):
        raise TypeError("First argument must be a list.")
    return lst.count(value)

#!/usr/bin/python3
def best_score(a_dictionary):
    """
    returns a key with the biggest integer value

    Args:
        a_dictionary: intial dictionary

    Return:
        key with biggest integer value or none
        if score is not found
    """
    if not a_dictionary:
        return None
    high_score = list(a_dictionary.values())[0]  # Typecast to access value
    for key, value in a_dictionary.items():
        if high_score < value:
            high_score = value
            name = key
    return name

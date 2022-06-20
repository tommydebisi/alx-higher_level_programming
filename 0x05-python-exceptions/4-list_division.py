#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    divides element by element 2 lists.

    Args:
        my_list_1: first list
        my_list_2: second list
        list_length: length of the list
    """
    new_list = list()
    for iter in range(list_length):
        try:
            new_list.append(my_list_1[iter] / my_list_2[iter])
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            print(end="")
    return new_list

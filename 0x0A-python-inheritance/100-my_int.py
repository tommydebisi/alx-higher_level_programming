#!/usr/bin/python3
"""
    100-my_int Module
"""


class MyInt(int):
    """
        MyInt class
    """

    def __eq__(self, other_ob) -> bool:
        """ Equality special method

            Args:
                Other_ob: second object in consideration
        """
        return super().__ne__(other_ob)

    def __ne__(self, other_ob) -> bool:
        """ Non Equality special method

            Args:
                Other_ob: second object in consideration
        """
        return super().__eq__(other_ob)

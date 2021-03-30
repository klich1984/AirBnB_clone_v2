#!/usr/bin/python3
"""Database storage"""

class DBStorage():
    """class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        self.__engine
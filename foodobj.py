#!/usr/bin/env python

# Name:         foodobj.py
# Authors:      Matthew Sheridan
# Date:         01 May 2016
# Revision:     02 May 2016
# Licence:      Beer-Ware License, Revision 42

"""Provides a representation of a 'food', or meal, that can be consumed. Behaves as a dictionary."""

__authors__ = "Matthew Sheridan"
__credits__ = ["Matthew Sheridan"]
__date__    = "01 May 2016"
__version__ = "0.2"
__status__  = "Development"

import sys

class FoodObj:
    def _defaults(self):
        self._dict = dict()
        self._dict["kind"] = "Breakfast"
        self._dict["name"] = "Bacon, Egg, and Cheese"
        self._dict["takeout"] = False

    def __getitem__(self, key):
        if key in self._dict:
            return self._dict[key]
        else:
            raise KeyError

    def __setitem__(self, key, value):
        temp = self.__getitem__(key)
        if not value == "":
            if type(value) == type(temp) or temp == None:
                self._dict[key] = value
            else:
                raise KeyError
        else:
            raise ValueError

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (str(self.__getitem__("name")) + " (" +
                str(self.__getitem__("kind")) +
                ["", " takeout"][self.__getitem__("takeout")] + ")")

    def __init__(self, kind, name, takeout=False):
        self._defaults()
        self.__setitem__("kind", kind)
        self.__setitem__("name", name)
        self.__setitem__("takeout", takeout)

#!/usr/bin/env python
"""
Python script dat je om een woord vraagt  en het achterstrevoren weergeeft.
bron : https://www.w3schools.com/python/python_howto_reverse_string.asp
"""


__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Finished"


# CONFIGURING I/O
woord = input("typ hier een woord:  ") [::-1]   # Input dat vraagt of je een woord wilt ingeven
""" [::-1] zorgt ervoor dat je ingegeven woord achterstevoren wordt uitgelezen. """


def main():
    print(woord)    # Print het ingegeven woord in de console


if __name__ == '__main__':  # code to execute if called from command-line
    main()

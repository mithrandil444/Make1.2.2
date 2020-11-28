#!/usr/bin/env python
"""
Info about our project comes here
"""


__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Development"


# CONFIGURING I/O
sporten = ["voetbal", "skiën", "squash", "tennis", "zwemmen"]
guess = input("Enter guess: ")


def main():
    if guess in sporten:
        print("You win")

    else:
        print("Try again")



if __name__ == '__main__':  # code to execute if called from command-line
    main()

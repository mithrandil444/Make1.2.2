#!/usr/bin/env python
"""
Python script dat je vraagt naar een woord die in de lijst staat.
"""


__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Finished"


# Variabelen
sporten = ["voetbal", "skiën", "squash", "tennis", "zwemmen", "pingpong"]   # Lijst met sporten
hint = "welke sporten vind miranda leuk?"   # variabele genaamd hint


def main():
    print(hint)                         # Print de hint
    guess = input("Enter guess: ")      # Input dat ervoor zorgt dat je uw gok kan invoeren

    if guess in sporten:                # Als het ingegeven woord in de lijst staat print het You win
        print("You win")

    else:                               # Als het ingegeven woord niet in de lijst staat print het You lose
        print("You lose")

if __name__ == '__main__':  # code to execute if called from command-line
    main()

#!/usr/bin/env python
"""
Python script dat ervoor zorgt dat de matrix  90° en 270° draait en wordt weergeven op de console.
"""

# IMPORTS


__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Finished"

# CONFIGURING I/O
raster = [['.', '.', '.', '.', '.', '.'],
          ['.', 'O', 'O', '.', '.', '.'],
          ['O', 'O', 'O', 'O', '.', '.'],
          ['O', 'O', 'O', 'O', 'O', '.'],
          ['.', 'O', 'O', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'O', 'O', '.'],
          ['O', 'O', 'O', 'O', '.', '.'],
          ['.', 'O', 'O', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.']]


def main():
    rotated = rotate90(raster)  # 90°
    rotated = rotate90(rotated)  # 180°
    rotated = rotate90(rotated)  # 270°
    printList(rotated)
    print("\n")
    rotated2 = rotate90(raster)  # 90°
    printList(rotated2)


def rotate90(original):
    r = len(original)  # Aantal rijen orignele matrix
    c = len(original[0])  # Aantal kolommen orignele matrix
    rotated = [[j for j in range(r)] for i in range(c)]  # Nieuwe matrix met c (rijen) en r (kolommen)
    for x in range(c):
        for y in range(r):
            rotated[x][y] = original[y][(c - (x + 1))]
        # Waarde originele matrix kopiëerde naar positie - 90° nieuwe matrix
    return rotated  # Geroteerde matrix teruggeven aan main


def printList(l):  # Lijst uitprinten in matrixvorm
    # Aantal rijen en kolommen bepalen
    r = len(l)
    c = len(l[0])
    for x in range(r):

        for y in range(c):
            print(l[x][y], end='')  # voorkomt 'enter' op einde print instructie
        print("\n")


if __name__ == '__main__':  # run tests if called from command-line
    main()

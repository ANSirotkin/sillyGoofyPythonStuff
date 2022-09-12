#solves systems of equations (using rref)
import numpy as np

def checkM(matr):
    all0 = True
    for x in range(matr.shape[1] - 1):
        if matr[-1, x] != 0:
            all0 = False
    if all0:
        if matr[-1, -1] == 0:
            return 3
        else:
            return 4
    
    for x in range(matr.shape[0]):
        if matr[x, x] != 1:
            return 2
        for y in range(matr.shape[1] - 1):
            if x == y:
                continue
            if matr[x, y] != 0:
                return 2

    return 1

def checkR(row, rowNum):
    for x in range(len(row) - 1):
        if x == rowNum:
            if row[x] != 1:
                return False 
    return True

def vars(matr):
    for x in range(matr.shape[0]):
        print("Variable " + str(x + 1) + " = " + str(matr[x, -1]))

def m1n0(row, rowNum):
    if checkR(row, rowNum):
        return row
    else:
        div = row[rowNum]
        if div != 0:
            for x in range(len(row)):
                row[x] /= div

def rref(matr, rowNum):
    m1n0(matr[rowNum], rowNum)
    for x in range(matr.shape[0]):
        if x == rowNum:
            continue
        fac = matr[x, rowNum]
        for y in range(matr.shape[1]):
            matr[x, y] -= fac * matr[rowNum, y]
    print(matr)

def main():
    rc = input("What is the size of the matrix in row-major? (ex: 3x4) ")
    rc = rc.split("x")
    r = (int)(rc[0])
    c = (int)(rc[1])

    matrix = np.empty([r, c])

    for x in range(matrix.shape[0]):
        row = input("Type row " + (str)(x + 1) + " of the matrix (ex: 3x+4y=7 -> 3 4 7) ")
        rarr = row.split(" ")
        if len(rarr) != matrix.shape[1]:
            print("Row Size Error. Shutting Down.")
            quit()
        for y in range(matrix.shape[1]):
            matrix[x, y] = rarr[y]
    
    print(matrix)

    for x in range(r):
        rref(matrix, x)
        if checkM(matrix) == 3:
            print("Infinite solutions")
            quit()
        elif checkM(matrix) == 4:
            print("No solutions")
            quit()
    else:
        if checkM(matrix) == 1:
            vars(matrix)
            quit()
        else:
            print("Matrix unsolvable")
            quit()

main()
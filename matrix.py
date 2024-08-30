import math
import numpy

num = input("Enter the number of rows/columns: ")
val = int(num)

matrix = numpy.zeros((val, val))

for i in range(val):
    place = str(i + 1)
    inputRow = input("Enter the values of row " + place + ": ")
    row = inputRow.split()
    for x in range(val):
        matrix[i, x] = row[x]

def addRow(row1, row2, matrix):
    for i in range(len(matrix)):
        matrix[row1][i] = matrix[row1][i] + matrix[row2][i]
    return matrix

def subRow(row1, row2, matrix, scale_factor=1.0):
    for i in range(len(matrix)):
        matrix[row1][i] -= scale_factor * matrix[row2][i]
    return matrix

def scalar(row, sclr, matrix):
    for i in range(len(matrix)):
        matrix[row][i] = matrix[row][i] * sclr

def swap(row1, row2, matrix):
    matrix[[row1, row2]] = matrix[[row2, row1]]

def add(a, b):
    add = numpy.zeros((len(a), len(b)))

    for r in range(len(add)):
        for c in range(len(add)):
            add[r][c] = a[r][c] + b[r][c]
    return(add)

def subtract(a, b):
    subtract = numpy.zeros((len(a), len(b)))

    for r in range(len(subtract)):
        for c in range(len(subtract)):
            subtract[r][c] = a[r][c] - b[r][c]
    return(subtract)

def rref(matrix):
    numRows = matrix.shape[0]
    i = 0

    while i < numRows:
        if matrix[i][i] == 0.0:
            
            for k in range(i + 1, numRows):
                if matrix[k][i] != 0:
                    swap(i, k, matrix)
                    break
            else:
                i += 1
                continue 

        for j in range(i + 1, numRows):
            scaling_factor = matrix[j][i] / matrix[i][i]
            subRow(j, i, matrix, scaling_factor)

        i += 1

    for i in range(numRows - 1, -1, -1):
        if matrix[i][i] == 0.0:
            continue  
        scalar(i, 1 / matrix[i][i], matrix)  
        for j in range(i):
            scaling_factor = matrix[j][i]
            subRow(j, i, matrix, scaling_factor)

    return matrix


def get_cofactor(matrix, i, j):
    minor = []
    for row in range(len(matrix)):
        if row != i:
            minor_row = []
            for col in range(len(matrix[row])):
                if col != j:
                    minor_row.append(matrix[row][col])
            minor.append(minor_row)

    return minor

def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be square (same number of rows and columns)")
    
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for c in range(len(matrix)):
        cofactor = get_cofactor(matrix, 0, c)
        det += ((-1) ** c) * matrix[0][c] * determinant(cofactor)
    return det

repeat = 'y'
while (repeat == "y"):
    print("add = 1")
    print("subtract = 2")
    print("Find determinant = 3")
    print("Change to RREF = 4")
    out = input("What function do you want to use? ")

    if out == "1":
        matrix2 = numpy.zeros((val, val))
        print("Enter 2nd matrix")
        for i in range(val):
            place = str(i + 1)
            inputRow = input("Enter the values of row " + place + ": ")
            row = inputRow.split()
            for x in range(val):
                matrix2[i, x] = row[x]        
        result = add(matrix, matrix2)
        print(result)

    elif out == "2":
        matrix2 = numpy.zeros((val, val))
        print("Enter 2nd matrix")
        for i in range(val):
            place = str(i + 1)
            inputRow = input("Enter the values of row " + place + ": ")
            row = inputRow.split()
            for x in range(val):
                matrix2[i, x] = row[x]        
        result = subtract(matrix, matrix2)
        print(result)

    elif out == "3":
        print(determinant(matrix))

    elif out == "4":

        print(rref(matrix))

    repeat = input("Do you want to do another function (y/n)? ").lower()








import math
import numpy

num = input("Enter the number of rows: ")
val = int(num)

matrix = numpy.zeros((val, val))

for i in range(val):
    place = str(i + 1)
    inputRow = input("Enter the values of row " + place + ": ")
    row = inputRow.split()
    for x in range(val):
        matrix[i, x] = row[x]

# Define a 2D array (list of lists)
matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def addRow(row1, row2, matrix):
    for i in range(len(matrix)):
        matrix[row1][i] = matrix[row1][i] + matrix[row2][i]
    return matrix

def subRow(row1, row2, matrix):
    for i in range(len(matrix)):
        matrix[row1][i] = matrix[row1][i] - matrix[row2][i]
    return matrix

def scalar(row, sclr, matrix):
    for i in range(len(matrix)):
        matrix[row][i] = matrix[row][i] * sclr

def swap(row1, row2, matrix):
    for i in range(len(matrix)):
        temp = matrix[row1][i]
        matrix[row1][i] = matrix[row2][i]
        matrix[row2][i] = temp

def check(matrix):
    if matrix[0][0] != 0:
        return False
    temp = 0
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] != 0:
                if temp > c:
                    return False
                temp = c


        
            



def add(a, b):
    add = numpy.zeros((len(a), len(b)))
    for r in range(len(add)):
        for c in range(len(add)):
            add[r][c] = a[r][c] + b[r][c]
    for row in add:
        for item in row:
            print(item, end=' ')
        print()

def multiply(a, b):
    add = numpy.zeros((len(a), len(b)))
    for r in range(len(add)):
        for c in range(len(add)):
            add[r][c] = a[r][c] * b[r][c]
    for row in add:
        for item in row:
            print(item, end=' ')
        print()







# # Print each row of the 2D array
# for row in matrix:
#     for item in row:
#         print(item, end=' ')
#     print()  # Newline after each row


    





#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#
temp = [[51, 94, 26, 44],[59, 70, 95, 61],[109, 111, 52, 43],[30, 84, 67, 122]]
def reverse_row(arr):
    return arr[::-1]
    
def reverse_col(arr, col):
    col_arr = [ row.pop(col) for row in arr ]
    col_arr = reverse_row(col_arr)
    print(col_arr)
    for i in range(len(col_arr)):
        arr[i].insert(col, col_arr[i])
        
    return arr 
def flippingMatrix(matrix):
    # Write your code here
    sum_= 0
    print(np.array(matrix))
    size = len(matrix[0])
    for i in range(int(size/2)):
        for j in range(size-1,0,-1):
            if sum([matrix[i][j], matrix[i+1][j]]) < sum([matrix[-i-1-1][j], matrix[-i-1][j]]):
                matrix= reverse_col(matrix, j)
            elif matrix[i][j] < matrix[-i-1-1][j]:
                matrix= reverse_col(matrix, j)
                
            print(np.array(matrix))
        if sum(matrix[i][:int(size/2)]) < sum(matrix[i][int(size/2):]):
            matrix[i]= reverse_row(matrix[i])
    for j in range(int(size/2)):
        sum_ += sum(matrix[j][:int(size/2)])
    print(np.array(matrix))
    return sum_
                    

total = flippingMatrix(temp)
print(total)
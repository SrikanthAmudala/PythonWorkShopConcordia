import numpy as np


def transpose(matrix): # O(n^2)
    col, row = len(matrix[0]), len(matrix)
    transposeMatrix = []
    for i in range(col):  # i =0
        temp = []
        for j in range(row):  # j= 0,1,2,3
            temp.append(matrix1[j][i])
        transposeMatrix.append(temp)

    return transposeMatrix


matrix1 = [
    [1, 3, 4],  # 0,0
    [1, 1, 1],  # 1, 0
    [2, 12, 5],  # 2, 0
    [2, 12, 5]  # 3, 0
]

row_length = len(matrix1)
col_length = len(matrix1[0])

(row, col) = (4, 3)

from Week3 import majorityElement

print("Before the debug point")
# print(majorityElement.insideMajorityElement())
sampleList = [2, 2, 1, 1, 1, 2, 2]

print(majorityElement.majorityElementFunction(nums=sampleList))
print("After debug point")


import pandas

path_csv = "/Users/Srikanth/DOMO Projects/DOMO_UPLOAD_API-master 2/DOMO_UPLOAD/algorithm/output_csv_files/001_S3TEST.csv"

df = pandas.read_csv(path_csv)

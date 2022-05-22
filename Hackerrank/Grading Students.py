#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    mul_5 = []
    ans = []
    j = 0

    for l in range(0, 20):
        j += 5
        mul_5.append(j)

    for k in grades:
        res = mul_5[min(range(len(mul_5)), key=lambda i: abs(mul_5[i] - k))]

        if k < 38:
            ans.append(k)
        elif k >= res:
            ans.append(k)
        elif k < res:
            ans.append(res)
        else:
            print('error')

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

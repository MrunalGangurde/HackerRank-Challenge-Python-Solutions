#2-D array Matrics Hour glass problem

import math
import os
import re
import random
import sys


def hourglassSum(arr):

	max_sum = -math.inf

	for i in range(4):
	    for j in range(4):
		hourglass_Sum = (
			arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
		)
		max_sum = max(max_sum,hourglass_Sum)
	return max_sum

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'],'w')

	arr = []

	for _ in range(6):
		arr.append(list(map(int,input().rstrip().split())))

	result = hourglassSum(arr)

	fptr.write(str(result + '\n'))

	fptr.close()

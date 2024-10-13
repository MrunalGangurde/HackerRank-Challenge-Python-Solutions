# reverse an array

import math
import os
import random
import re
import sys

#objective is to reverse an array a

def reverseArray(a):
	reversed_a = a[::-1]
	return reversed_a
if__name__ =='__main__':
	fptr = open(os.environ['OUTPUT_PATH'],'w')

	arr_count = int(input().strip())
	arr = list(map(int,input().rstrip().split()))

	res = reverseArray(arr)

	fptr.write(''.join(map(str,res)))
	fptr.write('\n')

	fptr.close()
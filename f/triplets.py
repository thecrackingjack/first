import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(a,b):
    return map(lambda t: sum([x > y for x, y in zip(*t)]),((a, b), (b, a)))
    
    


    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = solve(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

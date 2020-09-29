import math
import os
import random
import re
import sys

def repeatedString(s, n):
    multi = n // len(s)
    count1 = s.count("a")*multi
    
    mod = n % len(s)
    count2 = s[:mod].count("a")
    
    return count1 + count2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    n = int(input())
    result = repeatedString(s, n)
    fptr.write(str(result) + '\n')
    fptr.close()
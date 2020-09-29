import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jump = 0
    flag = True
    
    if len(c) == 1:
        return 0
    
    for cnt,i in enumerate(c):
        print("before: ", cnt, i, jump, flag)        
        
        if cnt <= len(c) -3:
            if (i == 0) and (flag == True):
                if i == c[cnt+2]:
                    jump += 1
                    flag = False
                else:
                    jump += 1
            elif flag == False:
                flag = True
            else:
                jump += 1
                
        elif cnt == len(c) - 2:
            if (i == 0) and (flag == True):
                jump += 1
            elif flag == False:
                flag = True
            else:
                jump += 1
                
        print("after: ", cnt, i, jump, flag)
        print("\n")
    
    return jump



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    fptr.write(str(result) + '\n')
    fptr.close()
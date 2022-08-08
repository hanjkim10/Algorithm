# Consider a pair of integers (a, b)
# The following operations can be performed on (a, b) in any order, zero or more times.

# (a, b) -> (a + b, b)
# (a, b) -> (a, a + b)

# Return a string that denotes whether or not (a, b) can be converted to (c, d) by performing the operation zero or more times.

# (a, b) = (1, 1)
# (c, d) = (5, 2)
# Perform the operation (1, 1 + 1) to get (1, 2),
# Perform the operation (1 + 2, 2) to get (3, 2),
# and perform the operation (3 + 2, 2) to get (5, 2).open
# Alternatively, the first operation could be (1 + 1, 1) to get (2, 1) and so on.
# The diagram below demonstrates the example that represents the pairs as Certesian coordinates

# (a, b) = (1, 1)
# (c, d) = (5, 2)


import sys

def isPossible(a, b, c, d):
    if a == c and b == d:
        return "YES"
    if a < c:
        if isPossible(a + b, b, c, d) == "YES":
            return "YES"
    if b < d:
        if isPossible(a, a + b, c, d) == "YES":
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    a = int(input().strip())
    b = int(input().strip())
    c = int(input().strip())
    d = int(input().strip())
    
    sys.setrecursionlimit(1500)
    result = isPossible(a, b, c, d)
    
    fptr.write(result + '\n')
    
    fptr.close()
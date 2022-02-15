import sys

#Input: three real numbers.
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

#Output: string "triangle" if can exist a triangle formed by lengths from arguments
#or "not triangle" if can't.
if a > 0 and b > 0 and c > 0:
    if a < b + c and b < a + c and c < a + b:
        print("triangle")
    else:
        print("not triangle")
else:
    print("not triangle")
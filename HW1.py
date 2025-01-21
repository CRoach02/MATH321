# Unnamed functions for prior problems
def double_sum(x1: int, x2: int, y1: int, y2: int):
    result = 0
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            result += (x+y)
    return (result)

def sum(x, start, end):
    result = 0
    for i in range(start,end+1):
        result += (x+i)
    print(f"Result for ({x}): {result}/32")

def expected_value_xy(x1: int, x2: int, y1: int, y2: int):
    total = 0.0
    result = 0
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            print(x,y,(x+y), flush=True)
            result += (x * y * (x+y))
            total += (x * y * double_sum(x1,x2,y1,y2))/32
    print(f"{result}/32")
    return total
    
#double_sum(1,2,0,0)
#print(expected_value_xy(1,2,1,4))

# Problem 4.2-11

def joint_pmf(x,y):
    return ((x+1)*(4-x)*(y+1)*(3-y))

def partA_summation(xStart: int, xEnd: int, yStart: int, yEnd):
    total = 0
    print("Possible combinations: ")
    print("(3 3 is a coding error but doesn't affect the result)")
    print("X Y")
    for x in range(xStart,xEnd+1):
        for y in range(yStart,x+1):
            # y bound is limited to x because y<=x, 
            # the +1 are for 'for loop' bounding notation
            result = joint_pmf(x, y)
            print(x, y, result)
            total += result
    return total

#print("Result: ",partA_summation(0,3,0,2))

# Problem 4.3-1

def joint_pmf_431(x,y):
    return (x+y) # / 32

def probability_431(xStart: int, xEnd: int, yStart: int, yEnd: int):
    total = 0
    print("X Y Outcome")
    for x in range(xStart, xEnd+1):
        for y in range(yStart, yEnd+1):
            result = joint_pmf_431(x, y)
            print (x, y, f"{result}/32")
            total += result
    c = 1.0 / (total/32)
    print(f"C Value: {c}")
    print(f"Total: {total}/32")

def part_d(lBound, uBound, static_x, static_y):
    pass
probability_431(1,2,1,4)
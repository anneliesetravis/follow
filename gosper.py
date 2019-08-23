from follow import follow

def gosper(S, n):
    """
    Return the nth rewriting of the string S according to the given SRS.

    Arguments:

    :param S: the string to be rewritten
    :param n: the number of string rewritings to perform
    :return: the rewritten string
    """
    #base case
    if n == 0: 
        return S
    
    #general case: transform each symbol in S
    path = ""
    
    for letter in S :
        
        if letter == "E":
            path += gosper("ELFLLFRERREERFL", n - 1)
            
        elif letter == "F":
            path  += gosper("RELFFLLFLERRERF", n - 1)
            
        elif letter == "L":
            path  += gosper("L", n - 1)
            
        elif letter == "R":
            path  += gosper("R", n - 1)
        else:
            #ignore any characters other than E, F, R, L
            continue
        
    return path

def gosper_draw(S, n, T, step=10, angle=60):
    """
    Recursively rewrites and draws the string S. Default angle and step will give a hexagonal Gosper curve.

    Arguments:

    :param S: the string to be rewritten
    :param n: the recursion depth
    :param T: the Turtle object
    :param step: the amount by which the turtle draws forward 
    :param angle: the angle through which the turtle turns  
    """
    path = gosper(S, n)
    follow(T, path, step, angle)
    
    
print(gosper("E", 2))
gosper_draw("E", 5, "Turtle", step=10, angle=60)

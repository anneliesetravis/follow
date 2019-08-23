from exturtle import *

def follow(t, S, step = 10, angle = 90):
    """
    Causes the TurtleGraphics turtle to draw the path described by the string S.

    Arguments:

    :param t: = the Turtle object
    :param S: the string to dictate the turtle's movement
    :param step: the amount by which the turtle draws forward for "E" or "F" in the string
    :param angle: the angle through which the turtle turns left or right for "L" or "R" in the string (respectively)
    """
    t = Turtle()

    #speeding up the turtle by increasing the speed at which lines are drawn,
    #and reducing the delay between drawing individual lines
    t.getscreen().delay(0)
    t.speed(0)

    #hiding the turtle from view whilst drawing because it looks nicer
    t.ht()

    for letter in S :
        if letter == "E":
            forward(t, step) 
        elif letter == "F":
            forward(t, step)
        elif letter == "L":
            left(t, angle)
        elif letter == "R":
            right(t, angle)
        else:
            continue
        
if __name__ == "__main__":
    follow("Bob", "EELEELEELEEBLFFRFFRFFRFFR")

         

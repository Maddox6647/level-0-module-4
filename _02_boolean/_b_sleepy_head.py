"""
Use boolean variables to control program logic between two different code
paths.
"""

import tkinter
import turtle
if __name__ == '__main__':
    # TODO)
    #  1. Use a boolean variable to indicate if it is the weekend.
    #     Display a different message to the user depending on whether it is
    #     the weekend or not.
    weekend = False
    if weekend == False:
        print('no weekend today')
    else:
        print('it is the weekend!!!!!!')
    #  2. Use a boolean variable to indicate if a student passed an exam.
    #     Display a different message to the user depending on whether they
    #     passed or not.
    exam = False
    if exam == False:
        print('exam FAILED')
    else:
        print('U PASSED THE EXAM')
    #  3. Use a boolean variable to indicate if a game is over. When the game
    #     is over, tell the user.
    game = True
    if game == False:
        print("GAME OVER")
    else:
        print('game continue')
    #  4. Use two boolean variables, one to indicate if a shape should be red,
    #     the other to indicate if the shape is to be square. When both
    #     variables are true, use a turtle to draw a red square.
    square = True or False
    red = True or False
    if square and red == True:
        turtley_turtle = turtle.Turtle()
        for i in range(4):
            turtley_turtle.pencolor('red')
            turtley_turtle.forward(169)
            turtley_turtle.right(90)


    pass

import turtle
def line():
	board = turtle.Turtle()
	board.pencolor('black')
	board.forward(100) 
def square():
    board = turtle.Turtle()
    board.pencolor("green")
    num = 0
    while num < 4:
        board.forward(50)
        board.right(90)
        num += 1
def circle():
    board = turtle.Turtle()
    board.pencolor("red")
    board.circle(50,360)
def trigon():
    board = turtle.Turtle()
    board.pencolor('blue')
    num = 0
    while num < 3:
        board.forward(50)
        board.right(120)
        num += 1 
def drawing():
    window = turtle.Screen()
    window.bgcolor("white")
    square()
    circle()
    trigon()
    line()
    window.mainloop()
if __name__ == '__main__':
	drawing()   

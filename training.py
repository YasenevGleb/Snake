from turtle import Turtle, Screen
from random import randrange
import turtle
import time
import sys
class Snake():
    global listOfSegments
    listOfSegments=[]
    snakeObj=Turtle()
    def __init__(self,obj):
            self.snakeObj.color('red')
            self.snakeObj.penup()
            self.snakeObj.speed(10)
            self.snakeObj.shape("square")
            self.snakeObj.shapesize(1,1,1)
            listOfSegments.append(self.snakeObj)
    def travel(self):
        self.snakeObj.forward(5)
        turtle.ontimer(self.travel, 50)
        thegame.boardObj.update()
    def distanceToFood(self):
       X_cor = abs(int(self.snakeObj.xcor()))
       Y_cor = abs(int(self.snakeObj.ycor()))
       if any ((X_cor>=300,
               Y_cor>=300)):
          thegame.gameOver(self)
       turtle.ontimer(self.distanceToFood,50)
    def movingforfood(self):
        if self.snakeObj.distance(food.foodObj)<15:
            food.foodObj.goto(randrange(-200,200,20),randrange(-200,200,20))
            self.TrueTurtle=Turtle()
            self.TrueTurtle.shape("square")
            self.TrueTurtle.color("black")
            self.TrueTurtle.shapesize(1, 1, 1)
            self.TrueTurtle.penup()
            self.TrueTurtle.speed(0)
            self.TrueTurtle.hideturtle()
            listOfSegments.append(self.TrueTurtle)
        turtle.ontimer(self.movingforfood, 50)
    def movesOfSnakeSegments(self):
        for i in range(len(listOfSegments) - 1, 0, -1):
            listOfSegments[i].showturtle()
            x=listOfSegments[i-1].xcor()
            y= listOfSegments[i - 1].ycor()
            listOfSegments[i].goto(x,y)
            listOfSegments[i-1].forward(10)
        turtle.ontimer(self.movesOfSnakeSegments,50)
    def bordersInSnake(self):
        if len(listOfSegments)>=1:
            for i in range(1,len(listOfSegments)):
                x=listOfSegments[i].xcor()
                y=listOfSegments[i].ycor()
                if listOfSegments[0].distance(x,y) <= 5:
                    thegame.gameOver(self)
        turtle.ontimer(self.bordersInSnake, 50)
class thegame(Snake):
    boardObj = Screen()
    def __init__(self):
        self.boardObj.setup(600, 600)
        self.boardObj.bgcolor('green')
        self.direction=0
        self.boardObj.tracer(0)
        time.sleep(1)
    def moves(self):
        self.boardObj.onkey(lambda : snake.snakeObj.setheading(90)\
            if snake.snakeObj.heading()!=270  else snake.snakeObj.setheading(270), 'w')
        self.boardObj.onkey(lambda: snake.snakeObj.setheading(270)\
            if snake.snakeObj.heading()!=90 else snake.snakeObj.setheading(90), 's')
        self.boardObj.onkey(lambda: snake.snakeObj.setheading(180)\
            if snake.snakeObj.heading()!=0 else snake.snakeObj.setheading(0), 'a')
        self.boardObj.onkey(lambda: snake.snakeObj.setheading(0) \
            if snake.snakeObj.heading()!=180 else snake.snakeObj.setheading(180) , 'd')
        self.boardObj.onkey(lambda:self.gameOver(),"e")
        self.boardObj.onkey(lambda : self.restarTheGame(), "r")
        turtle.ontimer(self.moves,10)
    def restarTheGame(self):

        if len(listOfSegments)>=1:
            for i in range(len(listOfSegments) - 1, 0, -1):
                # listOfSegments[i].color("green")
                listOfSegments[i].reset()
        snake.snakeObj.home()

    def gameOver(self):
        food.foodObj.hideturtle()
        self.snakeObj.home()
        self.snakeObj.hideturtle()
        game.boardObj.bgcolor("green")
        self.snakeObj.color("red")
        tegGameOver=Turtle()
        tegGameOver.hideturtle()
        tegGameOver.color("red")
        pen=tegGameOver.getpen()
        pen.write("GAME OVER", True, align="center",font=("Arial", 20, "normal"))
        pen.write("your score {}".format(len(listOfSegments)-1))
        time.sleep(2)
        sys.exit()

    def check_update(self):
        self.boardObj.update()
    def  borders(self):
        borderObj = turtle.Turtle()
        borderObj.hideturtle()
        borderObj.penup()
        borderObj.goto(-300, 300)
        borderObj.pendown()
        borderObj.goto(300, 300)
        borderObj.goto(300, -300)
        borderObj.goto(-300, -300)
        borderObj.goto(-300, 300)
class Food:
    foodObj=Turtle()
    def __init__(self):
        self.foodObj.shape("circle")
        self.foodObj.shapesize(1,1,1)
        self.foodObj.penup()
        self.foodObj.sety(int(randrange(-200,200)))
        self.foodObj.setx(int(randrange(-200,200)))

while True:
    start=time.time()
    turtle.update()
    snake = Snake(Food)
    food=Food()
    game = thegame()
    game.borders()
    game.moves()
    snake.travel()
    snake.distanceToFood()
    snake.movingforfood()
    snake.bordersInSnake()
    game.movesOfSnakeSegments()

    turtle.listen()
    turtle.mainloop()
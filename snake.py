from turtle import Turtle
UP=90
DOWN=270
RIGHT=0
LEFT=180
STARTING_POSITIONS=[(0,0),(-15,0),(-30,0)]

class Snake:
    def __init__(self):
        self.turtle_list=[]
        self.create_snake()
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_turtle(position)
        
    def add_turtle(self,position):
        new_turtle = Turtle()
        new_turtle.color("white")
        new_turtle.shape("square")
        new_turtle.shapesize(stretch_len=0.75,stretch_wid=0.75)
        new_turtle.penup()
        new_turtle.goto(position)
        self.turtle_list.append(new_turtle)

    def extend(self):
        self.add_turtle(self.turtle_list[-1].position())
    def move(self):
        for index in range(len(self.turtle_list)-1,0,-1):
            new_coordinates=self.turtle_list[index-1].position()
            self.turtle_list[index].goto(new_coordinates)
    
        self.turtle_list[0].forward(15)
    
    def up(self):
        if self.turtle_list[0].heading() != DOWN:
            self.turtle_list[0].setheading(UP)
        
    def down(self):
        if self.turtle_list[0].heading() != UP:
            self.turtle_list[0].setheading(DOWN)
    def left(self):
        if self.turtle_list[0].heading() != RIGHT:
            self.turtle_list[0].setheading(LEFT)

    def right(self):
       if self.turtle_list[0].heading() != LEFT:
            self.turtle_list[0].setheading(RIGHT)
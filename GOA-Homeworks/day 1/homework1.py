import turtle

# Function to draw a rectangle
def draw_rectangle(width, height):
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

# Function to draw a triangle
def draw_triangle(length):
    for _ in range(3):
        turtle.forward(length)
        turtle.left(120)

# Move the turtle to the starting position
turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()

# Draw the base of the house (rectangle)
draw_rectangle(200, 150)

# Move to the roof starting position
turtle.penup()
turtle.goto(-100, 50)
turtle.pendown()

# Draw the roof (triangle)
draw_triangle(200)

# Move to the door starting position
turtle.penup()
turtle.goto(-30, -100)
turtle.pendown()

# Draw the door (rectangle)
draw_rectangle(60, 100)

# Hide the turtle
turtle.hideturtle()

# Keep the window open
turtle.done()


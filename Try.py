# You have used different colors: red, orange, yellow, green, blue, lightgreen...
# You can use different font sizes: Stylish, Roboto Slab, Merriweather, Lora, PT Serif...
# Import turtle package 
import turtle 

# Creating a turtle object(pen) 
pen = turtle.Turtle()

# You can decide how large the snow flake is
pen.pensize(5) # <- Try to change the size of the pen!

# You can choose the color the the snow flake!
pen.color('lightblue')

# we want the pen to draw the  quickest
pen.speed(0)

# set the pen to the center first
pen.home()

def branch():
    # You can change the number of the branch on each branch by changing the loop number
    for i in range(4): # <- try to change this number
        for j in range(3):
            pen.forward(20)
            pen.backward(20)
            pen.right(45)
        pen.right(90)
        pen.backward(20)
        pen.right(136)

# You can decide how many main brach the snow flake have 
NumberOfBranch = 8 # <- try to change this number
angle = 360 / NumberOfBranch
PenAngle = 360 / NumberOfBranch
for i in range(NumberOfBranch):
    branch()
    pen.home()
    pen.left(PenAngle)
    PenAngle += angle


# Give a function for the title!
def Text(): 
	# Move turtle to air 
	pen.up() 

	# Move turtle to a given position 
	pen.setpos(-150, 120) 
     
	# Move the turtle to the ground 
	pen.down() 

	# Set the text color to lightgreen 
	pen.color('red') 

	# Write the specified text in 
	# specified font style and size 
	pen.write("Its my snow flake", font=( 
	"Roboto Slab", 30, "bold"))  

# Run the Text function to write the title
Text()

# Remember to hide turtle after drawing it!
pen.ht() 

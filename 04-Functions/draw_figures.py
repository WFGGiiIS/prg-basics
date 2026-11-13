import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")  

# Side length
side_length = 100
same_length = 200
rec_width = 50
rec_length = 90

# Draw a square
figures.draw_square(side_length)
figures.draw_square(side_length)
figures.draw_triangle(same_length)
figures.draw_triangle(same_length)
figures.draw_rectangle(rec_length, rec_width)
figures.draw_rectangle(rec_length, rec_width)

# Hide the turtle and finish
window.mainloop()

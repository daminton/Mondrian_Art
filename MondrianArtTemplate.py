#Created by Ben Stephenson (ben.stephenson@ucalgary.ca)
#  Draw random "art" in a Mondrian style
#
import tkinter as tk
import random

WIDTH = 1024
HEIGHT = 768

SPLIT_LOW = 120
SPLIT_PENALTY = 1.5

def randomColor():
    number_of_colors = 1

    color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                for i in range(number_of_colors)]
    print(''.join(color))


""" # TODO:
# Split the region both vertically and horizontally
# Invoke mondrian on all four quadrants
#

def split_both(x, y, w, h, canvas):
"""

""" #
# TODO:
# Split so that the regions are side by side
# Invoke mondrian on both halves
def split_horizontal(x, y, w, h, canvas):
 """

""" # TODO:
# Split so that one region is above the other
# Invoke mondrian on both halves
#
def split_vertical(x, y, w, h, canvas):
 """
# 
# Use recursion to draw "art" in a Mondrian style
# This is the algorithm in the project description
#

def mondrian(x, y, w, h, canvas):
    if (w > WIDTH / 2 and h > HEIGHT / 2):
        split_both(x, y, w, h, canvas)
    elif (w > WIDTH / 2):
        split_vertical(x,y,w,h,canvas)
    elif (h > HEIGHT / 2):
        split_horizontal(x,y,w,h,canvas)
    else:
        vertical_split = 
        horizontal_split = 
#
# Main method - driver of the program
#
def main():
  # Create a window with a canvas
  master = tk.Tk()
  canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT)
  canvas.pack()

  # Draw the art
  mondrian(0, 0, WIDTH, HEIGHT, canvas)
  tk.mainloop()

main()
#
#  Draw random "art" in a Mondrian style
# import packages
import tkinter as tk
import random 

WIDTH = 1024
HEIGHT = 768

SPLIT_LOW = 120
SPLIT_PENALTY = 1.5

#
# Select a color randomly
#i wanted to make it a true random color and give it some uniquness
def randomColor():
    number_of_colors = 1

    color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                for i in range(number_of_colors)]
    return(''.join(color))


def random_point():
    #chooses split point randomly and it is needed as a decimal, thus divide by 100
    return random.randrange(33, 68) / 100

#
# Split the region both vertically and horizontally
#
def split_both(x, y, w, h, canvas):
  horizontal_split_pt = random_point()
  vertical_split_pt = random_point()

  left = round(horizontal_split_pt * w)
  left = w - left
  top = round(vertical_split_pt * h)
  base = h - top

  mondrian(x, y, left, top, canvas)
  mondrian(x + left, y, left, top, canvas)
  mondrian(x, y + top, left, base, canvas)
  mondrian(x + left, y + top, left, base, canvas)


# Split horizontally, thus it splits top and bottom

def split_horizontal(x, y, w, h, canvas):
  horizontal_split_pt = random_point()

  left = round(horizontal_split_pt * w)
  left = w - left

  mondrian(x, y, left, h, canvas)
  mondrian(x + left, y, left, h, canvas)

#
# Split so that one region is above the other
#
def split_vertical(x, y, w, h, canvas):
  vertical_split_pt = random_point()

  top = round(vertical_split_pt * h)
  base = h - top

  mondrian(x, y, w, top, canvas)
  mondrian(x, y + top, w, base, canvas)

#
# Use recursion to draw "art" in a Mondrian style
#
def mondrian(x, y, w, h, canvas):
  # Splits based parameters given in assignment tasks
  if w > WIDTH / 2 and h > HEIGHT / 2:
    split_both(x, y, w, h, canvas)
  elif w > WIDTH / 2:
    split_horizontal(x, y, w, h, canvas)
  elif h > HEIGHT / 2:
    split_vertical(x, y, w, h, canvas)
  else:
    # Splits based parameters given in assignment tasks
    horizontal_split_pt = random.randrange(SPLIT_LOW, max(round(SPLIT_PENALTY * w) + 1, \
                       SPLIT_LOW + 1))
    horizontal_split_pt = random.randrange(SPLIT_LOW, max(round(SPLIT_PENALTY * h) + 1, \
                       SPLIT_LOW + 1))

    if horizontal_split_pt < w and horizontal_split_pt < h:
      split_both(x, y, w, h, canvas)
    elif horizontal_split_pt < w:
      split_horizontal(x, y, w, h, canvas)
    elif horizontal_split_pt < h:
      split_vertical(x, y, w, h, canvas)


    else:
      color = randomColor()
      canvas.create_rectangle(x, y, x + w, y + h, fill=color, outline="black", width=10)

def main():
  # Create a window with a canvas
  master = tk.Tk()
  canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT)
  canvas.pack()

  # Draw the art
  mondrian(0, 0, WIDTH, HEIGHT, canvas)
  tk.mainloop()

main()

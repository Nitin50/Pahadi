
"Welcome to the Gaming World of Nitin"

Step 1: Importing Required Module.
import tkinter
from PIL import Image, ImageTk
import random

Step 2: Building a top-level widget to make the main window for our application
# top-level widget which represents the main window of an application
root = tkinter.Tk()
root.geometry('400x400')
root.title('DataFlair Roll the Dice') 

Step 3: Designing the buttons
# Adding label into the frame
BlankLine = tkinter.Label(root, text="")
BlankLine.pack()

# adding label with different font and formatting
HeadingLabel = tkinter.Label(root, text="Hello from DataFlair!",
   fg = "light green",
     bg = "dark green",
     font = "Helvetica 16 bold italic")
HeadingLabel.pack()

# images
dice = ['die1.png', 'die2.png', 'die3.png', 
    'die4.png', 'die5.png', 'die6.png']
# simulating the dice with random numbers between
# 0 to 6 and generating image
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for image
ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage

# packing a widget in the parent widget 
ImageLabel.pack( expand=True
                
Step 4: Forming a list of images to be randomly displayed
# images
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']
# simulating the dice with random numbers between
# 0 to 6 and generating image
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

Step 5: Constructing a label for image, adding a button and assigning functionality
# construct a label widget for image
ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage

# packing a widget in the parent widget 
ImageLabel.pack( expand=True)

# function activated by button
def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    ImageLabel.configure(image=DiceImage)
    # keep a reference
    ImageLabel.image = DiceImage

# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)

# pack a widget in the parent widget
button.pack( expand=True)
 
Step 6: Forming a list of images to be randomly displayed
# call the mainloop of Tk
# keeps window open
root.mainloop()               

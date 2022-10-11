import os
import random
import tkinter

from PIL import Image, ImageTk

# toplevel widget which represents the main window of an application
root = tkinter.Tk()
root.geometry('400x400')
root.title('Group-1 Roll the Dice')

# adding label with different font and formatting
welcome_label = tkinter.Label(root, text="Welcome! Please Click Roll the Dice",
                              fg="black", font="Helvetica 16 bold italic",
                              pady=20)
welcome_label.pack()

# images
dices = os.listdir("resources/")
# simulating the dice with random numbers between 0 to 6 and generating image
image = ImageTk.PhotoImage(Image.open("resources/"+random.choice(dices)))

# construct a label widget for image
diceImage = tkinter.Label(root, image=image)
diceImage.image = image

# packing a widget in the parent widget
diceImage.pack(expand=True)

# function activated by button


def rolling_dice():
    image = ImageTk.PhotoImage(Image.open(("resources/"+random.choice(dices))))
    # update image
    diceImage.configure(image=image)
    # keep a reference
    diceImage.image = image


# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll the Dice',
                        fg='blue', command=rolling_dice)

# pack a widget in the parent widget
button.pack(expand=True)

# call the mainloop of Tk
# keeps window open
root.mainloop()

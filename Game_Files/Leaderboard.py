#Author: Jhan Gomez
#Version 1.0.0
#Date: 07/09/2025
#Purpose: To demonstrate a leaderboard system for my game, it had to be done using simple python because pygame is very limited due to its lack of support for newlines and
#the constant need to render chunks of multiline text would prove impractical and a waste of memory.
# THIS HAS SINCE BEEN MERGED INTO THE MAIN FILE, BUT THIS REMAINS AS A REFERENCE!
from tkinter import * #Imports the entire tkinter module
from tkinter import ttk #Imports the ttk submodule.
root = Tk() #Root is set to the main window where everything else will be attached
root.title("A Bull In A China Shop") #A title is set for the program.
with open ("Leaderboard.txt", "r") as file: #Opens the leaderboard file.
     scores=file.read() #Reads the text from the file with the appropriate line spacing.
frame = ttk.Frame(root) #A frame is made using the .Frame method and will be attached to root.
frame.pack(fill=BOTH, expand=True, padx=10, pady=10) #This frame will fill from both left and right, will expand if necessaring and will have x and y spacing of 10.
scrollbar = ttk.Scrollbar(frame)  #A scrollbar is implemented using ttk's.scrollbar method on the frame.
scrollbar.pack(side=RIGHT, fill=Y) #The scrollbar will be on the right side, with control of the Y axis.
text_widget = Text(frame, wrap=NONE, yscrollcommand=scrollbar.set, height=15, width=50) # Text will be passed on to the frame, with vertical scrolling and a height and width for the text area.
text_widget.insert(END, scores) #Text is added after the last characther, scores will be this text.
text_widget.pack(side=LEFT, fill=BOTH, expand=True) #Puts the text to the left side, fills the textbox from both sides, and will expand if necessary.
text_widget.config(state=DISABLED) #This prevents the player from typing in junk values.
root.mainloop() #handles events

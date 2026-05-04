from tkinter import *

# create main window
frame = Tk()
frame.title("Text Widget with Button")

# create text widget
text_widget = Text(frame)
text_widget.pack()

# insert some text
text_widget.insert("insert", "Hello, world!")

# create a button widget (parent is frame is okay, but better practice: use same context)
button = Button(frame, text="Click Me!")

# insert the button within the Text widget at index 1.6
text_widget.window_create("1.6", window=button)

# start the main event loop (correct method name is mainloop, not mainLoop)
frame.mainloop()
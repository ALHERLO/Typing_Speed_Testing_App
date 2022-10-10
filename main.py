from tkinter import *




window = Tk()    #👉🏽 Start The window always at the beginning
window.title("The Typing Test")
window.minsize(width=1000, height=500)

my_label = Label(text="Test your Typing Speed!",  font = ("Arial", 24, "bold"))
my_label.pack()

# Button
def button_clicked():
    my_label.config(text = "I got clicked")

button = Button(text = "Click Me", command=button_clicked)
button.pack()

window.mainloop() #👉🏽 Mainloop always at the end
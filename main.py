from tkinter import *




window = Tk()    #👉🏽 Start The window always at the beginning
window.title("The Typing Test")
window.minsize(width=1000, height=500)

my_label = Label(text="Test your Typing Speed!",  font = ("Arial", 24, "italic"))
my_label.pack()

# Button
def button_clicked():
    my_label.config(text = input.get())

button = Button(text = "Click Me", command=button_clicked)
button.pack()

#Entry

input = Entry(width=80)
input.pack()
print(input.get())

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

window.mainloop() #👉🏽 Mainloop always at the end


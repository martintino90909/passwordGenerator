from tkinter import *

root = Tk()
root.title("Password generator")
root.geometry("400x100")


def print_name(event):
    print("Martin")
    print(event)


topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Punctuation", bg="white", fg="red")
button1.bind("<Button-1>", print_name)
button2 = Button(topFrame, text="Digits", bg="white", fg="blue")
button3 = Button(topFrame, text="Capital Letters", bg="white", fg="green")
button4 = Button(topFrame, text="Lower-case Letters", bg="white", fg="purple")
button5 = Button(bottomFrame, text="Create Password", bg="white", fg="teal")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button5.pack(side=LEFT)

root.mainloop()

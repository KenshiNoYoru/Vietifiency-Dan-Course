from tkinter import *

window = Tk()
window.title('Example')
border_color = Frame(window, background="black")
text = Text(border_color, bd=0)
text.pack(padx=1, pady=1)
border_color.pack(padx=40, pady=40)
window.mainloop()

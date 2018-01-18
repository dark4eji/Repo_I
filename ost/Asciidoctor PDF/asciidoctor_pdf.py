from tkinter import *
from pack import main_logic as b
from pack import lblw as lb
from tkinter import ttk


root = Tk()

nb = ttk.Notebook(root)
nb.grid(row=1, column=1)



fr1 = Frame()
fr2 = Frame()
nb.add(fr1, text="tab")
nb.add(fr2, text="tab2")

lb.LabelW(fr1)
b.Mlogic(fr1)
root.title('Asciidoctor PDF')
root.geometry('490x300')
root.resizable(width=False, height=False)
root.mainloop()

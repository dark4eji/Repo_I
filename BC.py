from tkinter import *
from pack import *

class MainClass:
    def __init__(self, parent):
        self.parent = parent
        version_class.Version(parent)
        config_class.Config(parent)
        opening_class.Opening(parent)
        pass


if __name__ == "__main__":
    root = Tk()
    MainClass(root)
    root.title("Build Changer")
    root.geometry('620x300')
    root.mainloop()


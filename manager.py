from tkinter import *
from tkinter import ttk, messagebox
from container import Container
from login import Login, Registro

class Manager(Tk):
    
    def __init__(self, *args, **kwars):
        super().__init__(*args, **kwars)
        self.title("sistema de ventas")
        self.resizable(False, False)
        self.geometry("1100x650+120+50")

        self.container = Frame(self, bg="#dcdcdc")
        self.container.pack(fill=BOTH, expand=True)

        self.frames = {}
        for i in (Login, Registro, Container):
            frame = i(self.container, self)
            self.frames[i] = frame

            self.show_frame(Container)

    def show_frame(self, frame_class, user=None):
        frame = self.frames

        if user is not None:
            frame.set_user(user)

            frame.tkraiser()

def main():
    app = Manager()
    app.mainloop()

if __name__ == "__main__":
    main()
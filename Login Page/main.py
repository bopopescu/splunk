import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from LoginPage import LoginWindow
from RegisterPage import RegisterWindow
from HomePage import HomeWindow
from FileSystem import FileSystemWindow
from  ConnectPage import ConnectWindow
import LogPage

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.geometry("630x600+500+200")
        self.resizable(False,False)
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        page_name = StartPage.__name__
        frame = StartPage(parent=self.container, controller=self)
        self.frames[page_name] = frame

        # put all of the pages in the same location;
        # the one on the top of the stacking order
        # will be the one that is visible.
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage", "Start Page")


    def show_frame(self, page_name, title):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        self.title(title)
        frame.tkraise()
        # frame.update()


    def get_page(self, page_class):
        return self.frames[page_class]

    def framess(self, class_names):
        for F in class_names:
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

    def removeFrame(self, class_name):
        self.frames.pop(class_name)
        print("frame was removed")

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # button1 = tk.Button(self, text="Login",
        #                     command=lambda: controller.show_frame("LoginWindow", "Login Page"))
        self.controller.framess([HomeWindow, RegisterWindow])
        button1 = tk.Button(self, text="Home",width="20",height="3",font='Courier 26',
                            command=lambda: controller.show_frame("HomeWindow", "Home Page"))


        button2 = tk.Button(self, text="Register",width="20",height="3",font='Courier 26',
                            command=lambda: controller.show_frame("RegisterWindow", "Register Page"))
        button1.pack(pady="130")
        button2.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
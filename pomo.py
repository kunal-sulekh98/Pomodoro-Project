
from settings import *
import customtkinter as ctk

class App(ctk.CTk):
    
    def __init__(self):

        #window setup
        super().__init__(fg_color = GREEN)
        self.title('')
        #empty icon yet to be found (empty.ico not working as of now)...
        self.iconbitmap()
        self.geometry('400x400')
        self.resizable(False, False)

        self.change_title_bar_color()

        self.mainloop()

    def change_title_bar_color(self):
        pass
        # change the color of the title bar

App()




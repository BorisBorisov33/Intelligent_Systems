from tkinter import *
import tkinter as tk

class MyApp:

    def __init__(self):
        self.window = Tk()
        self.window.title("My Application")
        self.window.geometry("960x540")
        self.window.minsize(480, 360)
        self.window.iconbitmap("logo.ico")
        self.window.config(background='#e28743')
        # initialization des composants
        self.frame = Frame(self.window, bg='#e28743')

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.frame.pack(expand=YES)

    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
        self.create_textbox()
        self.create_youtube_button()

    def create_textbox(self):
        text = Label(self.frame, text="Sleep Time", font=("Helvetica", 40), bg='#e28743',
                            fg='white')
        text.pack()
        textBox = Text(self.frame, height=2, width=10).place(x=300, y=400)
        # textBox.pack(side=self.root.RIGHT)

    def create_title(self):
        label_title = Label(self.frame, text="Welcome", font=("Helvetica", 40), bg='#e28743',
                            fg='white')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame, text="Hey guys", font=("Helvetica", 25), bg='#e28743',
                               fg='white')
        label_subtitle.pack()

    def create_youtube_button(self):
        yt_button = Button(self.frame, text="Run", font=("Helvetica", 25), bg='white', fg='#e28743',
                           # command=
                           )
        yt_button.pack(pady=25, fill=X)

# afficher
app = MyApp()
app.window.mainloop()

from tkinter import *
import tkinter as tk

class MyApp:

    def __init__(self):
        self.window = Tk()
        self.window.title("My Application")
        self.window.geometry("960x540")
        self.window.minsize(480, 360)
        # self.window.iconbitmap("logo.ico")
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
        self.create_grid()
        self.create_youtube_button()

    def create_grid(self):
        # entries
        time_in_bed = tk.Entry(master=self.frame, fg="white", bg="blue", width=50)
        time_go_bed = tk.Entry(master=self.frame, fg="white", bg="blue", width=50)
        time_wake_up = tk.Entry(master=self.frame, fg="white", bg="blue", width=50)
        steps = tk.Entry(master=self.frame, fg="white", bg="blue", width=50)

        # labels
        lbl_title = tk.Label(master=self.frame, text="Please input your details")
        lbl_time_in_bed = tk.Label(master=self.frame, text="time in bed")
        lbl_time_go_to_bed = tk.Label(master=self.frame, text="start of sleep")
        lbl_wake_up = tk.Label(master=self.frame, text="end of sleep")
        lbl_steps = tk.Label(master=self.frame, text="number of steps")

        # grid of the frame
        self.frame.grid(row=0, column=0, padx=10,pady=10)

        # position of entries
        time_in_bed.grid(row=1, column=0, padx=10,pady=10)
        time_go_bed.grid(row=2, column=0,pady=10)
        time_wake_up.grid(row=3, column=0,pady=10)
        steps.grid(row=4, column=0,pady=10)

        # position of labels
        lbl_title.grid(row=0, column=1)
        lbl_time_in_bed.grid(row=1, column=1, sticky="w")
        lbl_time_go_to_bed.grid(row=2, column=1, sticky="w")
        lbl_wake_up.grid(row=3, column=1, sticky="w")
        lbl_steps.grid(row=4, column=1, sticky="w")

    def create_title(self):
        label_title = Label(self.frame, text="Welcome", font=("Helvetica", 40), bg='#e28743',
                            fg='white')
        # label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame, text="Hey guys", font=("Helvetica", 25), bg='#e28743',
                               fg='white')
        # label_subtitle.pack()

    def create_youtube_button(self):
        yt_button = Button(self.frame, text="Run", font=("Helvetica", 25), bg='white', fg='#e28743',
                           # command=
                           )
        # yt_button.pack(pady=25, fill=X)

# afficher
app = MyApp()
app.window.mainloop()

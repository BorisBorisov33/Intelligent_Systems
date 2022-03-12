from tkinter import *
import tkinter as tk

class MyApp:

    def __init__(self):
        self.window = Tk()
        self.window.title("My Sleeping Score")
        self.window.geometry("960x540")
        self.window.minsize(480, 360)
        self.window.iconbitmap("images/coffee.ico")
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
        time_in_bed = tk.Entry(master=self.frame, fg="white", bg="#e28743", width=20, font = ('Helvetica', 15))
        time_go_bed = tk.Entry(master=self.frame, fg="white", bg="#e28743", width=20, font = ('Helvetica', 15))
        time_wake_up = tk.Entry(master=self.frame, fg="white", bg="#e28743", width=20, font = ('Helvetica', 15))
        steps = tk.Entry(master=self.frame, fg="white", bg="#e28743", width=20, font = ('Helvetica', 15))

        # labels
        lbl_title = tk.Label(master=self.frame, text="Please input your details", font=("Helvetica", 40), bg='#e28743', fg='white')
        empty_text = tk.Label(master=self.frame, text="", bg='#e28743', fg='#e28743')
        lbl_time_in_bed = tk.Label(master=self.frame, text="time in bed", font=("Helvetica", 25), bg='#e28743', fg='white')
        lbl_time_go_to_bed = tk.Label(master=self.frame, text="start of sleep", font=("Helvetica", 25), bg='#e28743', fg='white',)
        lbl_wake_up = tk.Label(master=self.frame, text="end of sleep", font=("Helvetica", 25), bg='#e28743', fg='white')
        lbl_steps = tk.Label(master=self.frame, text="number of steps", font=("Helvetica", 25), bg='#e28743', fg='white')

        # button
        button = Button(self.frame, text="Get my Sleep Score!", font=("Helvetica", 25), bg='white', fg='#e28743',
                           # command=
                           )

        # grid of the frame
        self.frame.grid(row=0, column=0, padx=10)

        # position of entries
        time_in_bed.grid(row=2, column=1, padx=10,pady=10)
        time_go_bed.grid(row=3, column=1,pady=10)
        time_wake_up.grid(row=4, column=1,pady=10)
        steps.grid(row=5, column=1,pady=10)

        # position of labels
        lbl_title.grid(row=0, column=0, columnspan=2)
        empty_text.grid(row=1,column=0, columnspan=2)
        lbl_time_in_bed.grid(row=2, column=0, sticky="w")
        lbl_time_go_to_bed.grid(row=3, column=0, sticky="w")
        lbl_wake_up.grid(row=4, column=0, sticky="w")
        lbl_steps.grid(row=5, column=0, sticky="w")

        button.grid(row=6, column=0, columnspan=2)

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

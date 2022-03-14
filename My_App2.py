from tkinter import *
import tkinter as tk
from turtle import shape
import joblib
import numpy as np
import datetime
import GA_lifestyle


class MyApp:

    def __init__(self):
        self.window = Tk()
        self.window.title("My Sleeping Score")
        self.window.geometry("960x540")
        self.window.minsize(480, 360)
        self.window.iconbitmap("images/coffee.ico")
        self.window.config(background='#140096')
        # initialization des composants
        self.frame = Frame(self.window, bg='#140096')

        # creation des composants
        self.profit = tk.IntVar()
        self.create_widgets()

        # empaquetage
        self.frame.pack(expand=YES)

    def create_widgets(self):
        self.create_grid()

    def create_grid(self):
        # entries
        self.age = tk.Entry(master=self.frame, fg="white", bg="#140096", width=20, font=('Helvetica', 15))
        self.time_go_bed = tk.Entry(master=self.frame, fg="white", bg="#140096", width=20, font=('Helvetica', 15))
        self.time_wake_up = tk.Entry(master=self.frame, fg="white", bg="#140096", width=20, font=('Helvetica', 15))
        self.steps = tk.Entry(master=self.frame, fg="white", bg="#140096", width=20, font=('Helvetica', 15))
        self.drinks = tk.Entry(master=self.frame, fg="white", bg="#140096", width=20, font=('Helvetica', 15))
        # labels
        self.lbl_title = tk.Label(master=self.frame, text="Please input your details", font=("Helvetica", 40),
                                  bg='#140096', fg='white')
        empty_text = tk.Label(master=self.frame, text="", bg='#140096', fg='#140096')
        lbl_age = tk.Label(master=self.frame, text="age", font=("Helvetica", 25), bg='#140096', fg='white')
        lbl_time_go_to_bed = tk.Label(master=self.frame, text="start of sleep", font=("Helvetica", 25), bg='#140096',
                                      fg='white', )
        lbl_wake_up = tk.Label(master=self.frame, text="end of sleep", font=("Helvetica", 25), bg='#140096', fg='white')
        lbl_steps = tk.Label(master=self.frame, text="number of steps", font=("Helvetica", 25), bg='#140096',
                             fg='white')
        lbl_caffenated_drinks = tk.Label(master=self.frame, text="Number of caffenated drinks", font=("Helvectica", 25),
                                         bg='#140096', fg='white')

        # button
        button = Button(self.frame, text="Get my Sleep Score!", font=("Helvetica", 25), bg='white', fg='#140096',
                        command=self.increase)

        rec_sleep_btn = Button(self.frame, text="Sleep Recommendation", font=("Helvetica", 25), bg='white',
                               fg='#140096', command=self.recommend)
        # grid of the frame
        self.frame.grid(row=0, column=0, padx=10)

        # labelProfit = tk.Label(self.frame, textvariable=self.profit)
        # labelProfit.grid(row=7, column=0)

        # position of entries
        self.age.grid(row=2, column=1, padx=10, pady=10)
        self.time_go_bed.grid(row=3, column=1, pady=10)
        self.time_wake_up.grid(row=4, column=1, pady=10)
        self.steps.grid(row=5, column=1, pady=10)
        self.drinks.grid(row=6, column=1, pady=10)
        # position of labels
        self.lbl_title.grid(row=0, column=0, columnspan=2)
        empty_text.grid(row=1, column=0, columnspan=2)
        lbl_age.grid(row=2, column=0, sticky="w")
        lbl_time_go_to_bed.grid(row=3, column=0, sticky="w")
        lbl_wake_up.grid(row=4, column=0, sticky="w")
        lbl_steps.grid(row=5, column=0, sticky="w")
        lbl_caffenated_drinks.grid(row=6, column=0, sticky="w")
        button.grid(row=7, column=0, columnspan=2)
        rec_sleep_btn.grid(row=8, column=0, columnspan=2)

    def increase(self):
        filename = 'finalized_model.joblib'
        loaded_model = joblib.load(filename)
        age = self.age.get()
        time_g_bed = datetime.datetime.strptime(self.time_go_bed.get(), '%H:%M:%S')
        time_w_bed = datetime.datetime.strptime(self.time_wake_up.get(), '%H:%M:%S')
        sleep = time_g_bed - time_w_bed
        f_time_in_bed = (86400 - sleep.total_seconds())
        init = datetime.datetime(1900, 1, 2)
        f_time_go_bed = (86400 - (init - time_g_bed).total_seconds())
        f_time_wake_bed = (86400 - (init - time_w_bed).total_seconds())
        X = [f_time_in_bed, f_time_go_bed,
             f_time_wake_bed, int(self.steps.get()), int(self.drinks.get())]
        X = np.array(X)
        X = X.reshape(1, -1)
        sleep_score = loaded_model.predict(X)[0]

        for widget in self.frame.winfo_children():
            widget.destroy()

        recommended_sleep = self.recommended_time_sleep(int(age))

        # labels for second frame
        self.lbl_title = tk.Label(master=self.frame, text="Your sleep quality card", font=("Helvetica", 40),
                                  bg='#140096', fg='white')
        empty_text = tk.Label(master=self.frame, text="", bg='#140096', fg='#140096')
        lbl_sleep_score = tk.Label(master=self.frame, text="Your sleep score:", font=("Helvetica", 25), bg='#140096',
                                   fg='white')
        lbl_time_bed = tk.Label(master=self.frame, text="You need at least that time in bed:", font=("Helvetica", 25),
                                bg='#140096', fg='white')

        lbl_sleep_score_ans = tk.Label(master=self.frame, text=sleep_score, font=("Helvetica", 25, "bold"),
                                       bg='#140096', fg='white')
        lbl_sleep_time = tk.Label(master=self.frame, text=recommended_sleep, font=("Helvetica", 25, "bold"),
                                  bg='#140096', fg='white')

        # positionisn for second frames
        empty_text.grid(row=1, column=0, columnspan=2)
        lbl_sleep_score.grid(row=2, column=0, sticky="w")
        lbl_time_bed.grid(row=3, column=0, sticky="w")
        lbl_sleep_score_ans.grid(row=2, column=1)
        lbl_sleep_time.grid(row=3, column=1)

        self.lbl_title.grid(row=0, column=0, columnspan=2)

    def recommend(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        # recommended_sleep = self.recommended_time_sleep(int(age))

        # labels for second frame
        lbl_text_title = tk.Label(master=self.frame, text="Your sleep quality card", font=("Helvetica", 40),
                                  bg='#140096', fg='white')
        empty_text = tk.Label(master=self.frame, text="", bg='#140096', fg='#140096')
        lbl_previous_night_sleep_score = tk.Label(master=self.frame, text="Previous night sleep score: ",
                                                  font=("Helvetica", 25), bg='#140096', fg='white')
        self.sleep_score = tk.Entry(master=self.frame, fg="white", bg="#140096", width=20, font=('Helvetica', 15))
        # global sleepScore_int
        sleepScore = self.sleep_score.get()
        # sleepScore_int = int(float(sleepScore))
        btn_recommend = Button(self.frame, text="Get Recommendation", font=("Helvetica", 25), bg='white', fg='#140096',
                               command=self.ga)
        # lbl_sleep_score = tk.Label(master=self.frame, text="Your sleep score:", font=("Helvetica", 25), bg='#140096', fg='white')
        # lbl_time_bed = tk.Label(master=self.frame, text="You need at least that time in bed:", font=("Helvetica", 25), bg='#140096', fg='white')

        # lbl_sleep_score_ans = tk.Label(master=self.frame, text=sleep_score, font=("Helvetica", 25, "bold"), bg='#140096', fg='white')
        # lbl_sleep_time = tk.Label(master=self.frame, text=recommended_sleep, font=("Helvetica", 25, "bold"), bg='#140096', fg='white')

        # positionisn for second frames
        empty_text.grid(row=1, column=0, columnspan=2)
        lbl_previous_night_sleep_score.grid(row=2, column=0, sticky="w")
        self.sleep_score.grid(row=2, column=1)
        btn_recommend.grid(row=3, column=0, columnspan=2)
        # lbl_time_bed.grid(row=3, column=0, sticky="w")
        # lbl_sleep_score_ans.grid(row=2, column=1)
        # lbl_sleep_time.grid(row=3, column=1)

        lbl_text_title.grid(row=0, column=0, columnspan=2)

    def ga(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        object = GA_lifestyle.GA(3, 100, 0.05, self.recommend(int(sleep_Score_int)))
        sorted = object.runGA()
        top_val = list(sorted)[0]

        lbl_sleep = tk.Label(master=self.frame, text="We recommend you the following:", font=("Helvetica", 25),
                             bg='#140096',
                             fg='white')
        lbl_sleep.grid(row=1, column=0)
        lbl_sleeptime = tk.Label(master=self.frame, text="Sleep time" + str(int(top_val[0] / 3600)),
                                 font=("Helvetica", 25), bg='#140096',
                                 fg='white')
        lbl_steps = tk.Label(master=self.frame, text="Sleep time" + str(top_val[3]), font=("Helvetica", 25),
                             bg='#140096',
                             fg='white')
        if (top_val[4] == 1):
            lbl_caffenated = tk.Label(master=self.frame,
                                      text="We recommend you to have 2 caffenated drinks at most and work out.",
                                      font=("Helvetica", 25),
                                      bg='#140096',
                                      fg='white')
        else:
            lbl_caffenated = tk.Label(master=self.frame,
                                      text="We do not recommend you to have any caffenated drinks or work out.",
                                      font=("Helvetica", 25),
                                      bg='#140096',
                                      fg='white')

    def recommended_time_sleep(self, age):
        if 1 < age <= 2:
            return 12
        elif 3 <= age <= 5:
            return 11
        elif 6 <= age <= 13:
            return 10
        elif 14 <= age <= 17:
            return 9
        elif 18 <= age <= 25:
            return 9
        elif 26 <= age <= 64:
            return 8
        elif age > 65:
            return 7


# show
app = MyApp()
app.window.mainloop()

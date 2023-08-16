from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
counting = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global counting
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="25:00")
    checks.config(text="")
    title.config(text="Timer", fg=GREEN)
    window.after_cancel(counting)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps
    if reps == 7:
        # secs = 20*60
        secs = 3
        title.config(text="Long Break", fg=RED)
        count(secs)
    elif reps % 2 == 0:
        # secs = 25*60
        secs = 3
        title.config(text="Work, bish", fg=GREEN)
        count(secs)
    elif not reps % 2 == 0:
        # secs = 5*60
        secs = 3
        title.config(text="Hol' up", fg=PINK)
        count(secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count(time):
    global counting
    checkmarks = ""
    global reps
    status = True
    if status:
        mins = time // 60
        secs = time % 60
        if secs < 10:
            secs = f"0{secs}"
        canvas.itemconfig(timer_text, text=f"{mins}:{secs}")
        counting = window.after(1000, count, time - 1)
        if secs == "00":
            if reps == 7:
                reps = 0
            else:
                reps += 1
            time = 0
            for i in range(reps // 2):
                checkmarks += "✔"
            checks.config(text=checkmarks)
            start()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

title = Label(text="Timer", font=(FONT_NAME, 30), fg=GREEN, bg=YELLOW, highlightthickness=0)
title.config(padx=20, pady=20)
title.grid(column=1, row=0)

checks = Label(text="", font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW, highlightthickness=0)
checks.config(padx=20, pady=20)
checks.grid(column=1, row=3)

button = Button(text="Start", command=start)
button.grid(column=0, row=2)

button = Button(text="Reset", command=reset)
button.grid(column=2, row=2)

window.mainloop()

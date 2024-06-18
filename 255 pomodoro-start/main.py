from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Open Sans"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_in_the_tomato_working_loop = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    global works
    works = ""
    reps = 0
    window.after_cancel(timer_in_the_tomato_working_loop)
    # text in the timer again == "00:00"
    canvas.itemconfig(timer_in_tomato, text="00:00")
    # tittle label again to timer
    timer.config(text="Timer", fg=GREEN)
    # reseting the checkmarks
    check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
works = ""

def start_timer():
    global reps
    global works
    reps += 1

    work_min = WORK_MIN
    short_break_min = SHORT_BREAK_MIN
    long_break_min = LONG_BREAK_MIN

    if reps % 2 == 0 and reps != 8:
        count_down(short_break_min)
        timer.config(text="Short Break", fg=PINK)

    elif reps == 8:
        count_down(long_break_min)
        timer.config(text="Long Break", fg=RED)
        reset_timer()

    else:
        count_down(work_min)
        timer.config(text="Work Time", fg=GREEN)
        works += " *"
        check_marks.config(text=f"{works}")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer_in_the_tomato_working_loop
    time_in_minutes = math.floor(count/60)
    time_in_sec = count % 60
    if time_in_sec < 10:
        time_in_sec = f"0{time_in_sec}"
    canvas.itemconfig(timer_in_tomato, text=f"{time_in_minutes}:{time_in_sec}")
    if count > 0:
        timer_in_the_tomato_working_loop = window.after(1000, count_down, count-1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodaro")
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 100, image=tomato_img)
timer_in_tomato = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=2, row=2)
# now making the timer label

timer = Label(text="Timer", font=(FONT_NAME, "45", "bold"), bg=YELLOW, fg=GREEN)
timer.grid(column=2, row=1)

# now making the start and reset button:

start_button = Button(text="Start", highlightthickness=0)
start_button.config(bg=YELLOW)
start_button.config(command=start_timer)
start_button.grid(column=1, row=3)


reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

# now finally making the tic mark and completing user interface

check_marks = Label( font=(FONT_NAME, "25", "bold"), bg=YELLOW, fg=GREEN)
check_marks.grid(column=2, row=4)
# hint 1: use foreground color fg
# hint 2: copy and paste check mark symbol I will insted use the astric sign "*"
# hint 3: use the grid intead of pack






window.mainloop()

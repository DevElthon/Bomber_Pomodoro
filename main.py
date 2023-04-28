from tkinter import *
from tkinter import ttk
import math
from PIL import Image, ImageTk

#CONSTANTES
PINK = "#e2979c"
RED = "#A50303"
BLACK = "#000000"
WHITE = "#ffffff"
FONT_NAME = "Courier"
WORK_MIN = 30
FINISH_WORK_MIN = 15
SHORT_BREAK_MIN = 10
RECOVER_MIN = 5
LONG_BREAK_MIN = 1
reps = 0
runs = 0
timer = None
running = False


#TIMER RESET
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Temporizador")
    check_marks.config(text="")
    global reps
    global runs
    global running
    reps = 0
    runs = 0
    running = False

#TIMER MECHANISM
def start_timer():
    global reps
    global runs
    global running

    if not running:
        reps += 1
        running = True

        work_sec = WORK_MIN * 60
        finish_sec = FINISH_WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        recover_sec = RECOVER_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if runs == 6:
            count_down(long_break_sec)
            title_label.config(text="Descansar", fg=BLACK)
            update_img(image5)
            runs += 1

        else:
            match reps:
                case 1:
                    count_down(work_sec)
                    title_label.config(text="Trabalhe", fg=BLACK)
                    update_img(image1)
                case 2:
                    count_down(finish_sec)
                    title_label.config(text="Termine a tarefa", fg=BLACK)
                    update_img(image2)
                case 3:
                    count_down(short_break_sec)
                    title_label.config(text="Procrastinar", fg=BLACK)
                    update_img(image3)
                case 4:
                    count_down(recover_sec)
                    title_label.config(text="Prepare-se", fg=BLACK)
                    update_img(image4)

                    reps = 0
                    runs += 1

#Next Timer
def pass_timer():
    global runs
    global reps
    global running

    if running:
        if runs > 6:
            reset_timer()
        if reps >= 5:
            reps = 0

        running = False
        window.after_cancel(timer)
        start_timer()

#COUNTDOWN MECHANISM
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec <= 9:
        count_sec = f"0{count_sec}"
    if count_min <= 9:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = runs
        for _ in range(work_sessions):
            mark += "✓"
        check_marks.config(text=mark, font=(FONT_NAME, 30))

def update_img(image):
    canvas.itemconfig(image_container, image=image)

#UI SETUP
window = Tk()
window.geometry("940x660")
window.title("Bomber Pomodoro")
window.config(padx=40, pady=20, bg=RED)

title_label = Label(text="Temporizador", fg=BLACK, bg=RED, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=700,height=500, bg=PINK, highlightthickness=0)

blackbox_img = PhotoImage(file="blackbox.png")
canvas.create_image(350, 500, image=blackbox_img, tag="image")

timer_text = canvas.create_text(350, 460, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)

start_button = Button(width=10,height=2, text="Começar", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

pass_button = Button(width=10, height=2, text="Pular", highlightthickness=0, command=pass_timer)
pass_button.grid(column=1, row=2)

reset_button = Button(width=10,height=2,text="Finalizar", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=BLACK, bg=RED)
check_marks.grid(column=1, row=3)

image1 = PhotoImage(file="work_img.png")
image2 = PhotoImage(file="finish_img.png")
image3 = PhotoImage(file="procrastinate_img.png")
image4 = PhotoImage(file="recover_img.png")
image5 = PhotoImage(file="rest_img.png")

image_container = canvas.create_image(350, 220, image=image1)


window.mainloop()
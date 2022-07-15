from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
tim = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    window.after_cancel(tim)
    canvas.itemconfig(timer, text='00:00')
    lable.config(text='TIMER')
    check_mark.config(text='')
    global rep
    rep = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    rep += 1
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    if rep in [1,3,5,7]:
        count_down(work_sec)
        lable.config(text='WORK', fg=GREEN)
    elif rep in [2,4,6]:
        count_down(short_sec)
        lable.config(text='BREAK', fg=PINK)
    elif rep == 8:
        lable.config(text='BREAK', fg=RED)
        count_down(long_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global rep,tim
    min = count // 60
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    if min < 10:
        min = f"0{min}"
    canvas.itemconfig(timer,text=f"{min}:{sec}")
    if count > 0:
        tim = window.after(1000, count_down, count-1)
    else:
        if rep%2==0:
            t=rep//2 * '✔ '
            check_mark.config(text=t)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title('reading guide alarm')
window.config(pady=50, padx=100, bg=YELLOW)

canvas=Canvas(width = 200,height = 224 , bg = YELLOW, highlightthickness = 0)
image=PhotoImage(file = 'tomato.png')
canvas.create_image(100,112,image = image)
timer = canvas.create_text(100,130,text='00:00',fill = 'white', font = (FONT_NAME,35,'bold'))
canvas.grid(row=1,column=1)

lable=Label(text='TIMER',fg=GREEN,font=(FONT_NAME,45,'bold'),bg=YELLOW)
lable.grid(row=0,column=1)

start_button=Button(text='start',font=(FONT_NAME,25,'bold'),command=start_timer)
start_button.grid(row=2,column=0)

reset_button=Button(text='reset',font=(FONT_NAME,25,'bold'),command=reset_time)
reset_button.grid(row=2,column=2)

check_mark=Label(font=(FONT_NAME,25,'bold'),fg=GREEN,bg=YELLOW)
check_mark.grid(row=3,column=1)
window.mainloop()
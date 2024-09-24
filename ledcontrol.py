from tkinter import Tk, Label, Scale, HORIZONTAL
import tkinter.font as FONT
from gpiozero import PWMLED

red_pwm = PWMLED(17)
green_pwm = PWMLED(27)
blue_pwm = PWMLED(22)

app = Tk()
app.title("RGB Controller")

font_style = FONT.Font(family='Helvetica', size=14, weight='bold')

def red_slider_update(value):
    red_pwm.value = int(value) / 100

def green_slider_update(value):
    green_pwm.value = int(value) / 100

def blue_slider_update(value):
    blue_pwm.value = int(value) / 100

Label(app, text="Red Value", font=font_style, fg="red").grid(row=0, column=0)
red_slider = Scale(app, from_=0, to=100, orient=HORIZONTAL, command=red_slider_update)
red_slider.grid(row=0, column=1)

Label(app, text="Green Value", font=font_style, fg="green").grid(row=1, column=0)
green_slider = Scale(app, from_=0, to=100, orient=HORIZONTAL, command=green_slider_update)
green_slider.grid(row=1, column=1)

Label(app, text="Blue Value", font=font_style, fg="blue").grid(row=2, column=0)
blue_slider = Scale(app, from_=0, to=100, orient=HORIZONTAL, command=blue_slider_update)
blue_slider.grid(row=2, column=1)

def exit_app():
    app.destroy()

app.protocol("WM_DELETE_WINDOW", exit_app)
app.mainloop()

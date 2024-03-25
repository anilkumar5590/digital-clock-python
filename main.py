#Different Modules
from tkinter import *
import time

#tkinter initialization
root=Tk()

#Title of the window
root.title("Digital Clock")

#Sizes of the window
root.geometry("560x50")

#Present Time Function calls recursively after every second
def clock():
    current_time=time.localtime()
    # %d-day[1-31] %b-month name[Jan-Dec] %Y-year %a-weekday name[Mon-Sun]
    # %I-hours[1-12] %M-minutes[00-59] %S-seconds[00-59] %p-AM/PM
    time_format=time.strftime("%d-%b-%Y %a %I:%M:%S %p",current_time)
    label.config(text=time_format)
    label.after(1000,clock)

#Assigning background color,foreground color and font size
label=Label(root,font= ("roboto",30),bg="black",fg = "red")
label.pack(anchor="center")

#Calling the time fucntion
clock()

mainloop()
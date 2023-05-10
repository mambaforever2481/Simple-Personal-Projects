### Author:  CJ
### Date written: 5//2023
### Description:   The intention of this tKinter Python application is to display the current live time and date.


def exit():
    window.destroy()

import tkinter  as tk 
window = tk.Tk()
window.geometry("500x400")
window.title('Current Time and Date')
from time import strftime

def time():
    time_string = strftime('%I:%M:%S %p')
    l2.config(text=time_string)
    l2.after(1000,time)

def date():
    date_string= strftime('%B %d, %Y')
    l4.config(text=date_string)
    l2.after(30000,date)
	

l1=tk.Label(window, text= "The current time is:", font= "Times, 40")
l2=tk.Label(window, font= "Times, 20")
l3=tk.Label(window, text= "The current date is:", font= "Times, 40")
l4=tk.Label(window, font= "Times, 20", pady=0)


time()
date()
btn1 = tk.Button(window,text="Exit application",font=("Arial", 10),command=exit)

l1.pack()
l2.pack()
l3.pack()
l4.pack()

btn1.pack()

window.mainloop()


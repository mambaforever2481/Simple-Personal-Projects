### Author:  CJ
### Date written: 5//2023
### Description:   The intention of this tKinter Python application is to display the current live time and date.


def exit(): #creates a function that closes the main window
    window.destroy()

import tkinter  as tk #imports the tkinter module
window = tk.Tk() #creates a window
window.geometry("500x400") #initializes the window with geometry 500 x 400
window.title('Current Time and Date') #Sets the title of the window
from time import strftime #imports the strftime module

def time(): #creates a function that captures the current time every second
    time_string = strftime('%I:%M:%S %p')
    l2.config(text=time_string) #configures the time string to update the l2 label
    l2.after(1000,time)

def date(): #creates a function that captures the current date every 30 seconds(time can be adjusted as necessary)
    date_string= strftime('%B %d, %Y')
    l4.config(text=date_string) #configures the time strong to update the l4 label
    l4.after(30000,date)
	

l1=tk.Label(window, text= "The current time is:", font= "Times, 40") #creates the label "The current time is"
l2=tk.Label(window, font= "Times, 20") #displays the current time
l3=tk.Label(window, text= "The current date is:", font= "Times, 40") #creates the label "The current date is"
l4=tk.Label(window, font= "Times, 20", pady=0) #displays the current date


time() #initializes the time function
date() #initializes the date function
btn1 = tk.Button(window,text="Exit application",font=("Arial", 10),command=exit) #initializes the button "Exit application"

l1.pack() #packs the l1 label
l2.pack() #packs the l2 label
l3.pack() #packs the l3 label
l4.pack() #packs the l4 label

btn1.pack() #packs btn1

window.mainloop() #main window loop


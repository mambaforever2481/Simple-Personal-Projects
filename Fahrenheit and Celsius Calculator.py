### Author:  Clyde Kershaw
### Date written: 02/24/2023
### Assignment:   Module 6 Ex 1
### Description:   The intention of this tKinter Python application is to convert the user's given temperature (either in Fahrenheit or Celsius) to the other temperature measurement.(i.e. Fahrenheit to Celsius or Celsius to Fahrenheit) The program will display the correct answer based on the button clicked.


def exit():
    window.destroy()
 
def convertF():
    c = float(e1.get())
    f = c * 9/5+32
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    t1.insert(tk.END,f)
    t1.config(state='disabled')

def convertC():
    f = float(e1.get())
    c = (((f*5)/9)-(160/9))
    t2.config(state='normal')
    t2.delete('1.0', tk.END)
    t2.insert(tk.END,c)
    t2.config(state='disabled')

import tkinter as tk
window = tk.Tk()
window.geometry("300x250")
window.config(bg="white")
window.resizable(width=True,height=True)
window.title('Celsius and Fahrenheit Converter')
 
l1 = tk.Label(window,text="Celsius and Fahrenheit Converter",font=("Arial", 15),fg="black",bg="white")
l2= tk.Label(window,text="Enter temperature in either F or C: ",font=("Arial", 10,"bold"),bg="white")
l3= tk.Label(window,text="Temperature in Fahrenheit is: ",font=("Arial", 10,"bold"),bg="white")
l4= tk.Label(window,text="Temperature in Celsius is: ",font=("Arial", 10,"bold"),bg="white")
 
e1= tk.Entry(window,font=('Arial',10))
 
btn1 = tk.Button(window,text="Convert to Fahrenheit",font=("Arial", 10),command=convertF)
btn2 = tk.Button(window,text="Convert to Celsius",font=("Arial", 10),command=convertC)
btn3 = tk.Button(window,text="Exit application",font=("Arial", 10),command=exit)
 
t1=tk.Text(window,state="disabled",width=15,height=0)
t2=tk.Text(window,state="disabled",width=15,height=0)
 
l1.pack()
l2.pack()
e1.pack()
btn1.pack()
btn2.pack()
l3.pack()
t1.pack()
l4.pack()
t2.pack()

 
window.mainloop()


### Author:  CJ
### Date written: 5//2023
### Description:   The intention of this tKinter Python application is to display the current live time and date.


def exit():
    window1.destroy()

chooseRock = 0


def chooseRock():
    if playerChoice == 0 and compChoice == 0:
        yield "The result is a draw"
    else:
        return "The result is"

playerChoice = chooseRock()
compChoice = 0


from tkinter import *
import random

window1 = Tk()
window1.geometry("500x400")
window1.title("Rock Paper Scissors Demo")

l1 = Label(window1, text= "Rock Paper Scissors Demo", font= "Arial, 25")

btn1 = Button(window1,text="Exit application",font=("Arial", 10),command=exit)
btn2 = Button(window1,text="Pick rock", font=("Arial", 10),command= chooseRock)

l1.pack()
btn2.pack()
btn1.pack()




window1.mainloop()


### Author:  CJ
### Date written: 5//2023
### Title:  Rock Paper Scissors Game
### Description:   The intention of this tKinter Python application is to create an interactive rock paper scissors game.


def exit():
    window1.destroy() #creates a function that will close the main window

def restartGame(): #creates a function that will restart the game when the button is clicked
    global playerChoice
    playerChoice = 0
    global compChoice
    compChoice = random.randint(1,3)
    window2.destroy()

def chooseRock(): #creates a function that will set the players choice (rock) to the given value (1) and return the result based on the random value chosen by the program.
    global playerChoice
    playerChoice = 1
    global window2
    window2 = Toplevel(window1)
    window2.geometry = window1.geometry
    window2.config(bg="white")
    window2.resizable(width=False, height= False)
    window2.title("You chose Rock")
    
    l1 = Label(window2, text= "You chose rock", font= ("Arial", 40))
    l1.pack()
    btn1 = Button(window2, text= "Restart game", font= ("Arial", 20), command=restartGame)
    btn1.pack()

    if playerChoice == compChoice:
          l1 = Label(window2, text= "It is a draw! Try again.", font= ("Arial", 30))
          l1.pack()
    elif playerChoice == 1 and compChoice == 2:
          l1 = Label(window2, text= "Paper covers rock. You lose!", font= ("Arial", 30))
          l1.pack()
    elif playerChoice == 1 and compChoice == 3:
          l1 = Label(window2, text= "Rock smashes scissors. You win!", font= ("Arial", 30))
          l1.pack()
         
              
def choosePaper(): #creates a function that will set the players choice (paper) to the given value (2) and return the result based on the random value chosen by the program.
    global playerChoice
    playerChoice = 2
    global window2
    window2 = Toplevel(window1)
    window2.geometry = window1.geometry
    window2.config(bg="white")
    window2.resizable(width=False, height= False)
    window2.title("You chose Paper")

    l1 = Label(window2, text= "You chose paper", font= ("Arial", 40))
    l1.pack()
    btn1 = Button(window2, text= "Restart game", font= ("Arial", 20), command=restartGame)
    btn1.pack()
    
    if playerChoice == compChoice:
          l1 = Label(window2, text= "It is a draw! Try again.", font= ("Arial", 30))
          l1.pack()
    elif playerChoice == 2 and compChoice == 1:
          l1 = Label(window2, text= "Paper covers rock. You win!", font= ("Arial", 30))
          l1.pack()
    elif playerChoice == 2 and compChoice == 3:
          l1 = Label(window2, text= "Scissors cut paper. You lose!", font= ("Arial", 30))
          l1.pack()


def chooseScissors(): #creates a function that will set the players choice (scissors) to the given value (3) and return the result based on the random value chosen by the program.
    global playerChoice
    playerChoice = 3
    global window2
    window2 = Toplevel(window1)
    window2.geometry = window1.geometry
    window2.config(bg="white")
    window2.resizable(width=False, height= False)
    window2.title("You chose Scissors")

    l1 = Label(window2, text= "You chose scissors", font= ("Arial", 40))
    l1.pack()
    btn1 = Button(window2, text= "Restart game", font= ("Arial", 20), command=restartGame)
    btn1.pack()
    
    if playerChoice == compChoice:
          l1 = Label(window2, text= "It is a draw! Try again.", font= ("Arial", 30))
          l1.pack()
    elif playerChoice == 3 and compChoice == 2:
          l1 = Label(window2, text= "Scissors cut paper. You win!", font= ("Arial", 30))
          l1.pack()
    elif playerChoice == 3 and compChoice == 1:
          l1 = Label(window2, text= "Rock smashes scissors. You lose!", font= ("Arial", 30))
          l1.pack()    


from tkinter import *       #imports the tkinter module
import random

compChoice = random.randint(1,3)

window1 = Tk()      #initializes the main window
window1.geometry("500x500")     #sets the size of the main window to 500x500
window1.config(bg="white")      #initializes the window's background color to be white  
window1.resizable(width=True,height=True)       #configures the window to be resizable with width and height
window1.title('Rock Paper Scissors Game')        #initializes the title of the window
 
l1 = Label(window1,text="Rock Paper Scissors Game",font=("Arial", 25),fg="black",bg="white") #creates the main label
l2= Label(window1,text="Choose rock, paper or scissors: ",font=("Arial", 10,"bold"),bg="white") #creates the label that asks the user to choose rock, paper or scissors

btn1 = Button(window1,text="Rock", command=chooseRock) #creates the button that asks the user to choose rock
btn2 = Button(window1,text="Paper", command=choosePaper) #creates the button that asks the user to choose paper
btn3 = Button(window1,text="Scissors", command=chooseScissors) #creates the button that asks the user to choose scissors
btn4 = Button(window1,text="Exit application",font=("Arial", 10),command=exit) #creates the exit button

l1.pack() #packs the l1 label
l2.pack() #packs the l2 label
btn1.pack() #packs the btn1 button
btn2.pack() #packs the btn2 button
btn3.pack() #packs the btn3 button
btn4.pack() #packs the btn4 button

window1.mainloop() #main loop window

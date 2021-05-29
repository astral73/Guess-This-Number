import random
import tkinter as tk
from functools import partial

gui = tk.Tk()

gui.geometry("720x720")

gui.configure(bg = 'black')

labelmenu = tk.Label(master=gui, text = "Guess This Number", bg='black', fg='white')
labelmenu.place(x=220,y=200)
labelmenu.config(font = ('Ariel', 25))

labelcreator = tk.Label(master=gui,text = "Created by Astral", bg='black', fg='white')
labelcreator.place(relx=0.0, rely=1.0, anchor='sw')

number = random.randint(0,100)
life = tk.IntVar()
life.set(5)

def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list

def guess(labelask,entrylabel,life,lifelabel):
    usernumber = int(entrylabel.get())

    if(usernumber == number):
        widgets_list = all_children(gui)
        for item in widgets_list:
            item.destroy()

        labelwin = tk.Label(master=gui,text = "You won... :) . Please Click the Quit Button",bg='black',fg='white')
        labelwin.place(x=310,y=200)

        labelnumber = tk.Label(master=gui,text="You guessed " + str(number) + ".",bg='black',fg='white')
        labelnumber.place(x=250,y=300)

        buttonquitx1 = tk.Button(gui, text = 'Quit',command=quit,height=1,width= 10)
        buttonquitx1.place(x=300,y=500)


    if(usernumber > number):
        labelask = tk.Label(master=gui,text="Your number is higher than this number",bg='black',fg = 'white')
        labelask.place(x=310,y=200)
        life.set(life.get()-1)

        lifelabel = tk.Label(master = gui,text = "Life: " + str(life.get()),bg='black',fg='white')
        lifelabel.pack(side=tk.LEFT,anchor = tk.NW)

    if(usernumber < number):
        labelask = tk.Label(master=gui,text="Your number is lower than this number",bg='black',fg = 'white')
        labelask.place(x=310,y=200)
        life.set(life.get()-1)

        lifelabel = tk.Label(master = gui,text = "Life: " + str(life.get()),bg='black',fg='white')
        lifelabel.pack(side=tk.LEFT,anchor = tk.NW)

    if(life.get() == 0):
        widgets_list = all_children(gui)
        for item in widgets_list:
            item.destroy()

        labellose = tk.Label(master=gui,text = "You lose... :( . Please Click the Quit Button",bg='black',fg='white')
        labellose.place(x=250,y=200)

        labelnumber = tk.Label(master=gui,text="You had to guess " + str(number) + ".",bg='black',fg='white')
        labelnumber.place(x=250,y=300)

        buttonquitx1 = tk.Button(gui, text = 'Quit',command=quit,height=1,width= 10)
        buttonquitx1.place(x=300,y=500)



def game():
    buttonstart.destroy()
    buttonquit.destroy()
    labelmenu.destroy()

    buttonquitx = tk.Button(gui, text = 'Quit',command=quit,height=1,width= 10)
    buttonquitx.place(x=310,y=500)

    lifelabel = tk.Label(master = gui,text = "Life: " + str(life.get()),bg='black',fg='white')
    lifelabel.pack(side=tk.LEFT,anchor = tk.NW)

    labelask = tk.Label(master = gui, text = "Please enter a number", bg='black', fg='white')
    labelask.place(x=310,y=200)

    entrylabel = tk.Entry(master = gui)
    entrylabel.place(x=310,y=250)

    buttonentry = tk.Button(master = gui, text="Enter",command = partial(guess,labelask,entrylabel,life,lifelabel),height=1,width= 10)
    buttonentry.place(x = 310,y=300)   

buttonstart = tk.Button(gui, text = 'Start',command=game,height=1,width= 10)
buttonstart.place(x=310,y=250)

buttonquit = tk.Button(gui, text = 'Quit',command=quit,height=1,width= 10)
buttonquit.place(x=310,y=300)

gui.mainloop()
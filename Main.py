#imports the required libraries
from tkinter import *                
import sys
import os
from datetime import datetime
import time

rt = Tk()#creates a new tkinter (GUI) window
rt.configure(background='light blue')#set background colour

#gets the background image for the main page
canvas = Canvas(rt, width =500, height = 1123)      
canvas.pack()      
img = PhotoImage(file="FP_img.png")      
canvas.create_image(20,20, anchor=NW, image=img)

#declares global variables
weekday=""
sys_date=""
sys_time=""
timestr = ''

def run_UIDT(): # Function to run the required code, if user chooses to view by chosen date and time
    os.system('Stalls_UIDT.py')

def getSDT(): #gets the System date and time updates
    global weekday
    global sys_date
    global sys_time
    # datetime object containing current date and time
    now = datetime.now()
    sys_date = now.strftime("%d/%m/%Y") #stores current (system) date
    sys_time = now.strftime("%H:%M:%S") #stores current (system) time
    hrs = now.strftime("%H")
    mins = now.strftime("%M")
    today = datetime.today()
    x = today.weekday() #stores current (system) generated weekday's code. Here x=0 refers to Monday, x=1 refers to Tuesday, and so on.
    weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    wkday_num = [0,1,2,3,4,5,6]  
    for i in range(7):
        if(x==wkday_num[i]):
            weekday = weekdays[i]#returns weekday corresponding to 'x'
    timestr = weekday + " " + "|" + " " + sys_date + " " + "|" + " " + sys_time #creates a string containing current weekday, system date and system time
    return timestr

def tick(time1=timestr):
    # get the current local time from the PC
    time2 = getSDT()
    # if time string has changed, update it
    if time2 != timestr:
        time1 = time2
        l1.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    l1.after(200, tick)

def run_SDDT(): # Function to run the required code, if user chooses to view by system date and time
    os.system('Stalls_SDDT.py')


# Creates a button to run the required code, if user chooses to view by chosen date and time   
button1 = Button(rt,text="View by Current Date time",command=run_SDDT)
button1.pack()
button1.place(x=100,y=650)

# Creates a button to run the required code, if user chooses to view by system date and time
button2 = Button(rt,text="Choose the date and time",command=run_UIDT)
button2.pack()
button2.place(x=300,y=650)

getSDT()# invokes the function 'getSDT()'



#code for time below
l1 = Label(rt,text=timestr,compound=CENTER)
l1.config(font=('Times New Roman',12))
l1.pack()
l1.place(x=170,y=350)

tick()# invokes the function 'tick()'

rt.resizable(width=False, height=False)# ensures that the main page cannot be resized (maximized or minimized)

rt.mainloop()# runs the main loop for execution







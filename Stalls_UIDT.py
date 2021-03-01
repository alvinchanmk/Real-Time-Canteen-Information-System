#imports the modules and dependencies required
from tkinter import *           
from UserInput_date_time import return_values


import pandas as pd
import numpy
import dateutil
import pytz



root = Tk() #creates a new tkinter (GUI) window
root.configure(background='light blue')#set background colour
root.title('menu')# sets the title of this window

#declares global variables
tkvar=""
number=""
resultLabel=""
wd=""
h=0

def WT_PerPerson(X): # Function to create a dictionary with key = stall name, and value = corresponding waiting time (in minutes) per person
    stall={'Mini Wok':5,'Western':6,'Japanese and Korean Delights':4,'McDonald\'s':3,'Subway':2}
    return stall[X] #returns that value corresponding to the parameter key (X)

def display_menus_info_sun(*args): # Function to display the menu corresponding to the selected stall, if the user defined date is a sunday
    global tkvar
    global wd
    global h
    
    wd,h=return_values() # calls the function 'return_values' from the 'UserInput_date_time' module, to get the weekday and the hour (corresponding to the entered time and date)
    if(wd=="Sunday"): 
        if(tkvar.get()=='Subway'): #checks if the selected stall is Subway
            if(h<11 or h>=18): #displays "CLOSED" if the time entered is not within Subway's operating hours
                rl=Label(root, text="CLOSED",font=('Comic Sans',14,'bold'))
                rl.pack()
                rl.place(x=560,y=500)
            else:
                #display's Subway's lunch/dinner menu
                data = pd.read_csv("Stalls_Menus_LD.csv",encoding="ISO-8859-1") #'pandas' library used to read the '.csv' file that stores lunch/dinner menus, and store it in 'data' variable
                list1 = (str(data.iloc[2,1])).split(",")#stores all items from Subway's lunch/dinner menu in a list
                for i in range(len(list1)): #looping structure to display each of these items as labels in the tkinter window
                    rl=Label(root,text=list1[i],font=('Comic Sans',10))
                    rl.pack()
                    rl.place(x=775,y=(350+50*i))
        elif(tkvar.get()=="McDonald's"): #checks if the selected stall is McDonald's 
            if(h<10 or h>=22): #displays "CLOSED" if the time entered is not within McDonald's operating hours
                rl=Label(root, text="CLOSED",font=('Comic Sans',14,'bold'))
                rl.pack()
                rl.place(x=560,y=500)
            else:
                if(h<11):
                    data = pd.read_csv("Stalls_Menus_BK.csv",encoding="ISO-8859-1") #'pandas' library used to read the '.csv' file that stores breakfast menus, and store it in 'data' variable
                    list1 = (str(data.iloc[4,1])).split(",")#stores all items from McDonald's breakfast menu in a list
                    for i in range(len(list1)):
                        rl=Label(root,text=list1[i],font=('Comic Sans',10))
                        rl.pack()
                        rl.place(x=775,y=(350+50*i))
                else:
                    data = pd.read_csv("Stalls_Menus_LD.csv",encoding="ISO-8859-1") #'pandas' library used to read the '.csv' file that stores lunch/dinner menus, and store it in 'data' variable
                    list1 = (str(data.iloc[4,1])).split(",")#stores all items from McDonald's lunch/dinner menu in a list
                    for i in range(len(list1)):
                        rl=Label(root,text=list1[i],font=('Comic Sans',10))
                        rl.pack()
                        rl.place(x=775,y=(350+50*i))
        else: #displays "CLOSED" if the selected stall is Japanese and Korean Delights/Mini Wok/Western, as they are closed on Sundays
            rl=Label(root, text="CLOSED",font=('Comic Sans',14,'bold'))
            rl.pack()
            rl.place(x=560,y=500)
def display_menus_info_sat(*args): # Function to display the menu corresponding to the selected stall, if the user defined date is a saturday
    global wd
    global h
    wd,h=return_values()
    if(wd=="Saturday" and tkvar.get()!="Subway" and tkvar.get()!="McDonald's"):
        # Also checks if the selected stall is Japanese and Korean Delights/Mini Wok/Western (neither Subway nor McDonald's)
        if(h<7 or h>=15): #displays "CLOSED" if the time entered is not within their operating hours
            rl=Label(root, text="CLOSED",font=('Comic Sans',14,'bold'))
            rl.pack()
            rl.place(x=560,y=500)
        elif(h<11):
            data = pd.read_csv("Stalls_Menus_BK.csv",encoding="ISO-8859-1")
            for i in range(5):
                if(tkvar.get()==data.iloc[i,0]): 
                    list1 = (str(data.iloc[i,1])).split(",") #stores all items from the chosen stall's breakfast menu in a list
                    for j in range(len(list1)):
                        rl=Label(root,text=list1[j],font=('Comic Sans',10))
                        rl.pack()
                        rl.place(x=775,y=(350+50*j))
        else:
            data = pd.read_csv("Stalls_Menus_LD.csv",encoding="ISO-8859-1")
            for i in range(5):
                if(tkvar.get()==data.iloc[i,0]):
                    list1 = (str(data.iloc[i,1])).split(",") #stores all items from the chosen stall's lunch/dinner menu in a list
                    for j in range(len(list1)):
                        rl=Label(root,text=list1[j],font=('Comic Sans',10))
                        rl.pack()
                        rl.place(x=775,y=(350+50*j))
    elif(wd=="Saturday" and tkvar.get()=="Subway"): # checks if the selected stall is Subway 
        if(h<11 or h>=18):
            rl=Label(root, text="CLOSED",font=('Comic Sans',14,'bold'))
            rl.pack()
            rl.place(x=560,y=500)
        else:
            data = pd.read_csv("Stalls_Menus_LD.csv",encoding="ISO-8859-1")
            list1 = (str(data.iloc[2,1])).split(",")
            for i in range(len(list1)):
                rl=Label(root,text=list1[i],font=('Comic Sans',10))
                rl.pack()
                rl.place(x=775,y=(350+50*i))
        
                
    elif(wd=="Saturday" and tkvar.get()=="McDonald's"): # checks if the selected stall is McDonald's
        if(h<7):
            rl=Label(root, text="CLOSED",font=('Comic Sans',14,'bold'))
            rl.pack()
            rl.place(x=560,y=500)
        elif(h<11):
            data = pd.read_csv("Stalls_Menus_BK.csv",encoding="ISO-8859-1")
            list1 = (str(data.iloc[4,1])).split(",")
            for i in range(len(list1)):
                rl=Label(root,text=list1[i],font=('Comic Sans',10))
                rl.pack()
                rl.place(x=775,y=(350+50*i))
        else:
            data = pd.read_csv("Stalls_Menus_LD.csv",encoding="ISO-8859-1")
            list1 = (str(data.iloc[4,1])).split(",")
            for i in range(len(list1)):
                rl=Label(root,text=list1[i],font=('Comic Sans',10))
                rl.pack()
                rl.place(x=775,y=(350+50*i))

def display_menus_info_wkday(*args):  # Function to display the menu corresponding to the selected stall, if the user defined date is a weekday (Monday - Friday)
    global wd
    global h
    wd,h=return_values()
    if(tkvar.get()!="Subway" and tkvar.get()!="McDonald's"):
        if(h<7 or h>=21):
            rl=Label(root, text="CLOSED",font=('Comic Sans',14,'bold'))
            rl.pack()
            rl.place(x=560,y=500)
        elif(h<11):
            data = pd.read_csv("Stalls_Menus_BK.csv",encoding="ISO-8859-1")
            for i in range(5):
                if(tkvar.get()==data.iloc[i,0]):
                    list1 = (str(data.iloc[i,1])).split(",")
                    for j in range(len(list1)):
                        rl=Label(root,text=list1[j],font=('Comic Sans',10))
                        rl.pack()
                        rl.place(x=775,y=(350+50*j))
        else:
            data = pd.read_csv("Stalls_Menus_LD.csv",encoding="ISO-8859-1")
            for i in range(5):
                if(tkvar.get()==data.iloc[i,0]):
                    list1 = (str(data.iloc[i,1])).split(",")
                    for j in range(len(list1)):
                        rl=Label(root,text=list1[j],font=('Comic Sans',10))
                        rl.pack()
                        rl.place(x=775,y=(350+50*j))

    elif(tkvar.get()=="Subway"):
        if(h<8 or h>=21):
            rl=Label(root, text="CLOSED",font=('Comic Sans',14,'bold'))
            rl.pack()
            rl.place(x=560,y=500)
        elif(h<11):
            data = pd.read_csv("Stalls_Menus_BK.csv",encoding="ISO-8859-1")
            list1 = (str(data.iloc[2,1])).split(",")
            for i in range(len(list1)):
                rl=Label(root,text=list1[i],font=('Comic Sans',10))
                rl.pack()
                rl.place(x=775,y=(350+50*i))
        else:
            data = pd.read_csv("Stalls_Menus_LD.csv",encoding="ISO-8859-1")
            list1 = (str(data.iloc[2,1])).split(",")
            for i in range(len(list1)):
                rl=Label(root,text=list1[i],font=('Comic Sans',10))
                rl.pack()
                rl.place(x=775,y=(350+50*i))
    elif(tkvar.get()=="McDonald's"):
        if(h<7):
            rl=Label(root, text="CLOSED",font=('Comic Sans',14,'bold'))
            rl.pack()
            rl.place(x=560,y=500)
        elif(h<11):
            data = pd.read_csv("Stalls_Menus_BK.csv",encoding="ISO-8859-1")
            list1 = (str(data.iloc[4,1])).split(",")
            for i in range(len(list1)):
                rl=Label(root,text=list1[i],font=('Comic Sans',10))
                rl.pack()
                rl.place(x=775,y=(350+50*i))
        else:
            data = pd.read_csv("Stalls_Menus_LD.csv",encoding="ISO-8859-1")
            list1 = (str(data.iloc[4,1])).split(",")
            for i in range(len(list1)):
                rl=Label(root,text=list1[i],font=('Comic Sans',10))
                rl.pack()
                rl.place(x=775,y=(350+50*i))


def display_stalls_info(*args):  # Function to display the selected stall's details/information 
    global tkvar
    info = pd.read_csv("Stalls_info.csv",encoding="ISO-8859-1") #'pandas' library used to read the '.csv' file that stores stalls' information, and store it in 'info' variable
    for i in range(5): #looping structure to display each of these as labels in the tkinter window
        if(tkvar.get()==info.iloc[i,0]):
            info_list = (str(info.iloc[i,1])).split(",") #stores all data from the chosen stall's information in a list
            for j in range(len(info_list)):
                rlab=Label(root,text=info_list[j],font=('Comic Sans',10))
                rlab.pack()
                rlab.place(x=560,y=(350+50*j))
    

                    

def no(*args):  #Function to display the estimated waiting time (given the entered no. of people), for the selected stall
    try: # 'try' block to perform these operations
        global tkvar
        global number
        global resultLabel
        time=WT_PerPerson(tkvar.get()) #stores the waiting time per person for that selected stall, in 'time' variable, by invoking the function 'WT_PerPerson'
        try: # 'try' block to get the total estimated waiting time
            if(int(number.get())<0): #Checks if the entered no. of people is a negative value
                resultLabel.config(text='Please enter a positive integer') # If yes, then an error message is displayed as a label in the new tkinter window
            else:   
                result=int(number.get()) # gets the (entered) no. of people in the queue, before that person
                lastresult=int(time)*result # gets the total estimated waiting time
                resultLabel.config(text='The waiting time should be {} min'.format(lastresult)) # displays the estimated waiting time as a label in a new tkinter window
        except (ValueError): # 'except' block to catch a 'Value Error', if raised by the 'try' block.
            # In this case, it will be raised when the (entered) no. of people in the queue, before that person, is not an integer value.
            resultLabel.config(text='Please enter a positive integer') #error message displayed as a label in the new tkinter window
        
        number.delete(0,END) # Clears the entry widget (for no. of people in the queue)
        
    except(NameError,AttributeError,UnboundLocalError): {} # 'except' block to catch a 'Name Error', 'Attribute Error', or 'Unbound Local Error', if raised by the 'try' block.
    # Name Error: raised when a variable or function name has been used based on a previous definition
    # Attribute Error: raised when an invalid attribute reference is made, or when an attribute assignment fails.
    # Unbound Local Error: raised when a local variable is referenced before it has been assigned.
    
        
def wt_setup(): # Function to setup the new tkinter window for getting the estimated waiting time
    global tkvar
    global number
    global resultLabel
    newwin = Toplevel(root) # creates a new tkinter (GUI) window
    newwin.title('WaitingTime')# sets the title of this window
    newwin.geometry('300x300')# sets the geometry of this window

    Label(newwin,text='The number of people in the queue').pack(side='top') # label created to prompt the user to enter the no. of people in the queue, before that person

    number=Entry(newwin)# creates the required entry widget
    number.focus()
    
    #number.bind('<Return>',no)
    number.pack(side='top') # packs this entry widget on the top of this window

    enternumber = Button(newwin,text= "Enter", command=no) # creates a button, which when pressed, gets the value entered by the user
    enternumber.pack(side='top')# packs this button on the top of this window

# Create and empty Label to put the result in
    resultLabel = Label(newwin, text = "")
    resultLabel.pack(side='top')
#Creates a refresh button (packed on the left of this window) , named 'CLOSE', to close this new tkinter window
    frame2=Frame(newwin)
    frame2.pack()
    button_refresh = Button(frame2, text = "close",command=newwin.destroy)
    button_refresh.pack(side = LEFT)

def oh_setup(): # Function to setup the new tkinter window for getting the selected stall's operating hours
    global tkvar
    n = Toplevel(root) # creates a new tkinter (GUI) window
    n.title('WaitingTime')# sets the title of this window
    n.geometry('300x300')# sets the geometry of this window

    try: # 'try' block to perform these operations
        list_oh=list()
        Label(n,text='Operating Hours',font=('Comic Sans',14)).pack(side='top')  # label created to display the title: 'Operating Hours'
        data_oh = pd.read_csv("Stalls_OH.csv",encoding="ISO-8859-1")#'pandas' library used to read the '.csv' file that stores stalls' operating hours, and store it in 'data_oh' variable
        for i in range(5):
            name_oh = data_oh.iloc[i,0]
            list_oh = (str(data_oh.iloc[i,1])).split(",")#stores all data from the chosen stall's operating hours in a list
            if(tkvar.get()==name_oh):
                for j in range(len(list_oh)):
                    Label(n,text=list_oh[j],font=('Comic Sans',12)).pack(side='top')
    except AttributeError: {} # 'except' block to catch an 'Attribute Error', if raised by the 'try' block.
                                                                     
        
#Creates a refresh button (packed on the left of this window) , named 'CLOSE', to close this new tkinter window
    frame2=Frame(n)
    frame2.pack()
    button_refresh = Button(frame2, text = "close",command=n.destroy)
    button_refresh.pack(side = LEFT)


    
# creates the drop-down menu structure, to display the stalls available    
mainframe=Frame(root)
mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight = 1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=1,padx=1)

tkvar=StringVar(root)# creates a string variable for storing the selected stall's name
choices={"McDonald's",'Subway','Western','Mini Wok','Japanese and Korean Delights'}
tkvar.set('Choose') #setting the default option in dropdown

popupMenu=OptionMenu(mainframe,tkvar,*choices)
Label(mainframe, text="Choose a food stall",font=('Comic Sans',14,'bold'),fg='black').grid(row=1,column=1)# label created to prompt the user to choose a stall
popupMenu.grid(row=2,column=1)

#gets the background image for the root page
canvas = Canvas(root, width =500, height = 707)      
canvas.pack()      
img = PhotoImage(file="P2_img.png")      
canvas.create_image(0,0, anchor=NW, image=img)

# creates a button, which when pressed, opens the window for getting the estimated waiting time
WT=Button(text='Estimate waiting time',command=wt_setup)
WT.pack()
WT.place(x=580,y=625)

# creates a button, which when pressed, opens the window for getting the stall's operating hours
OH=Button(text='View Operating Hours',command=oh_setup)
OH.pack()
OH.place(x=580,y=675)

# Required function calls
tkvar.trace('w',no)
tkvar.trace('w',display_menus_info_sun)
tkvar.trace('w',display_menus_info_sat)
tkvar.trace('w',display_menus_info_wkday)
tkvar.trace('w',display_stalls_info)

root.mainloop()# runs the main loop for execution

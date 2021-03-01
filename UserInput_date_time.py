#imports the library required
from tkinter import *   
import sys
import os
import datetime


root = Tk() #creates a new tkinter (GUI) window
root.configure(background='light blue') #set background colour
root.title("Northspine Canteen lookup") #title

wkday = ""
hrs = 0
mins = 0


def return_values(): #returns global variables of wkday and hours after it has been verified by getWeekDay
    global wkday
    global hrs
    return wkday,hrs
  

def getWeekDay():#procedure that checks user date and time input and returns error msg if it is not valid/ not within correct range
    global wkday 
    global hrs
    global mins
    date_full = entry1.get() # user defined date input
    time_full = entry.get() # user defined time input
    
    if(time_full[2]!=':' or len(time_full)!=5):  #checks for : between the hr and min for time input and lenght of characters input to be 
        label2 = Label(root,text="Invalid Input! Time entered must be in the format hh:mm") #error message
        label2.config(font=('Times New Roman',15))  #font and size
        label2.pack()
        label2.place(x=100,y=600) #position of error label msg

    else:
        try:
            h = int(time_full[0:2]) #checks if input hour is an integer
            m = int(time_full[3:])  #checks if input min is an integer
            
        except ValueError: # executes if input of hour or min is not an integer
            label2 = Label(root,text="Invalid Input! Hours and Minutes must be integer values, entered in the format hh:mm") # error message
            label2.config(font=('Times New Roman',15))#font and size
            label2.pack()    
            label2.place(x=100,y=600) #position of error label msg
            

        else:
            if(int(time_full[0:2])<0 or int(time_full[0:2])>23 or int(time_full[3:])<0 or int(time_full[3:])>59): #checks input for hours and mins is within the correct range
                label2 = Label(root,text="Invalid Input! Correct Ranges: 0<=Hours<=23 and 0<=Minutes<=59") #error msg
                label2.config(font=('Times New Roman',15)) #font and size
                label2.pack()
                label2.place(x=100,y=600)#position of error label msg
               
            else:
                hrs = int(time_full[0:2]) #splices full time to hour
                mins = int(time_full[3:]) #splices full times to min

    if(date_full[2]!='/' or date_full[5]!='/' or len(date_full)!=10): #checks date to ensure '/' is at the correct positions
        label3 = Label(root,text="Invalid Input! Date entered must be in the format dd/mm/yyyy") #error message
        label3.config(font=('Times New Roman',15)) #font and size
        label3.pack()
        label3.place(x=100,y=700)   #position of error label msg
        
    else:
        try: #checks if the remaining characters are integers
            d = int(date_full[0:2]) #int value of user input day
            mo = int(date_full[3:5]) #int value of user input month
            y = int(date_full[6:]) #int value of user input year
            
        except ValueError: #executes if char input into date are not integers
            label3 = Label(root,text="Invalid Input! Date, month and year must be integer values, entered in the format dd/mm/yyyy") #error message
            label3.config(font=('Times New Roman',15)) #font and size
            label3.pack()
            label3.place(x=100,y=700)  #position of error label msg
           
        else:
            #calculate weekday from given date 
            date = int(date_full[0:2]) #user input date
            month = int(date_full[3:5]) #user input month
            year = int(date_full[6:])  #user input year
            Month_Num = ["01","02","03","04","05","06","07","08","09","10","11","12"] #list of months in str form
            Days = [31,28,31,30,31,30,31,31,30,31,30,31] # list of the days in the month for

            
            if(year%4==0 or (year%100==0 and year%400==0)):  #checks for leap year
                Days[1]=29    #sets days in feb to 29 for leap year
            check = False #sets check to false # boolean if its a leap year
            
            if(month==1 or month==2 or month==3 or month==4 or month==5 or month==6 or month==7 or month==8 or month==9 or month==10 or month==11 or month==12):
                # month btwn 1 & 12

                
                if(1<=date<=Days[month-1]): #if user input date is between 1 and the max date for that month 
                    check = True #set check to true 
                        
                else: #return error message 
                    label3 = Label(root,text="Invalid Input! Date does not exist for the given month") #error message
                    label3.config(font=('Times New Roman',15)) #font and size
                    label3.pack()
                    label3.place(x=100,y=700) #position of error label msg
                    
            else: #error printing for month not btwn 1-12
                label3 = Label(root,text="Invalid Input! Month entered does not exist") #error message
                label3.config(font=('Times New Roman',15))#font and size
                label3.pack()
                label3.place(x=100,y=700) #position of error label msg
                if(date<1 or date>31): # checks if date is outside possible range of 1-31 for dates
                    label4 = Label(root,text="Invalid Input! Date does not exist") #error message
                    label4.config(font=('Times New Roman',15))#font and size
                    label4.pack()
                    label4.place(x=100,y=800) #position of error label msg
                        
            if(check==True):
                num = datetime.datetime(year,month,date).weekday() #uses date time library to generate day of the week as a number
                weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] #list of days in a str
                wkday_code = [0,1,2,3,4,5,6] #list of week in decimal format
                for i in range(7): #lineral search comparing date generated by function and sorted list
                    if(num==wkday_code[i]): #if found,
                        wkday = weekdays[i] # assign the string value of week day to wday updated as global variable

    

label1 = Label(root,text="Enter the date in the format dd/mm/yyyy")#display msg for date
label1.config(font=('Times New Roman',16))#font and size
label1.pack()
label1.place(x=525,y=200)#position of description

entry1 = Entry(root)    #entry box for date
entry1.pack()
entry1.place(x=525,y=250)   #position of entry box

label = Label(root, text="Enter the time in the format hh:mm. Use 24-hour format.") #display msg for time
label.config(font=('Times New Roman',16))#font and size
label.pack()
label.place(x=525,y=300)#position of description

entry = Entry(root)#entry box for time
entry.pack()
entry.place(x=525,y=350)     #position of entry box


button1 = Button(root,text="Enter",font=('Times New Roman',16),command=getWeekDay)#font and size
button1.pack()
button1.place(x=525,y=400)   #position of button


root.mainloop()


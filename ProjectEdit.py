
# Filename: Project.py
# Author: Mark Holton
# Last Edit: Febuary 17, 2017
# Version Number: 1.0.a
# Description: python code for setting up the input output interface for calender

calender ={  }
#form of calender example
# "1":{'title':{ }, 'time':{ }, 'date':{ }, 'description':{ } }
#title = Lecture 
#time = 14:01-14:50
#date = Month/Day/Year 04/20/17
#description = string


# Filename: Project.py
# Author: Mark Holton
# Last Edit: Febuary 17, 2017
# Version Number: 1.0.a
# Description: python code for setting up the input output interface for calender
 
calender ={  }
#form of calender example
# "1":{'title':{ }, 'time':{ }, 'date':{ }, 'description':{ } }
#title = Lecture 
#time = 14:01-14:50
#date = Month/Day/Year 04/20/17
#description = string

def addEvent():
    title = input('Enter a title(use less than 24 characters): ')
    time = input('Enter a time in military time: ')
    date = input('Enter a date in the form Month/Day/Year: ')
    description = input('Enter a description: ')
    calender[str(len(calender)+1)] ={'title': {title}, 'time':{time}, 'date':{date}, 'description':{description} }
    outputCalender()

def deleteEvent():
    outputCalenderOnly()
    delete = input('Enter number of event you want to delete:  ')
    if delete in calender:
        del calender[delete]
    outputCalender()

def editEvent():
    outputCalenderOnly()
    whatToEdit = input('What would you like to edit?(enter event number):  ')
    if whatToEdit in calender:
        title = input('Enter a title(use less than 24 characters): ')
        time = input('Enter a time in military time: ')
        date = input('Enter a date in the form Month/Day/Year: ')
        description = input('Enter a description: ')
        calender[whatToEdit] ={'title': {title}, 'time':{time}, 'date':{date}, 'description':{description} }
    outputCalender()



def outputCalender():
    print('Event Number   Title                   Time       Date       Description')
    itemNumber = 1
    for item in calender:
        entry = '      '+str(item)
        while len(entry)< len('Event Number   '):
            entry = entry +' '
        for y in calender[item]:
            entry = entry +str(calender[item][y]).strip("{''}") 
            while y == "title" and len(entry) < len('Event Number   Title                   '):
                entry = entry + ' '
            while y == "time" and len(entry) < len('Event Number   Title                   Time       '):
                entry = entry + ' '
            while y == "date" and len(entry) < len('Event Number   Title                   Time       Date       '):
                entry = entry + ' '
            while y == "description" and len(entry) < len('Event Number   Title                   Time       Date       Description'):
                entry = entry + ' '
        print(entry)
    chooseMethod()

def outputCalenderOnly():
    print('Event Number   Title                   Time       Date       Description')
    itemNumber = 1
    for item in calender:
        entry = '      '+str(item)
        while len(entry)< len('Event Number   '):
            entry = entry +' '
        for y in calender[item]:
            entry = entry +str(calender[item][y]).strip("{''}") 
            while y == "title" and len(entry) < len('Event Number   Title                   '):
                entry = entry + ' '
            while y == "time" and len(entry) < len('Event Number   Title                   Time       '):
                entry = entry + ' '
            while y == "date" and len(entry) < len('Event Number   Title                   Time       Date       '):
                entry = entry + ' '
            while y == "description" and len(entry) < len('Event Number   Title                   Time       Date       Description'):
                entry = entry + ' '
        print(entry)
    

def chooseMethod():
    method = input('Type "add" to add an event, "edit" if you wish to edit an event, "delete" to delete an event, or "show" to display your Calender.  ')
    if method == "add":
        addEvent()    
    if method == "edit":
        editEvent()
    if method == "show":
        outputCalender()
    if method == "delete":
        deleteEvent()
    

chooseMethod()







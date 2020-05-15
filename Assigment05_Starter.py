# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2020,Created started script
# erikjk,5.14.2020, Created text file and populated it with tasks
# erikjk,5.14.2020, Worked through Step 4 - Adding to the document
# erikjk,5.14.2020, Worked through Step 6 - Appending values to document
# erikjk,5.14.2020, Worked through Step 1 - Failed and worked on Step 3
# erikjk,5.14.2020, Realized I had done Step 6 wrong  - Overwrite after read, not append
# erikjk,5.14.2020, Figured out Step 1 - Worked on formatting
# erikjk,5.14.2020, Worked through Step 5 - Deleting dictionary entries based on keys
# erikjk,5.14.2020, Added timer in Step 7 after printing goodbye message
# erikjk,5.14.2020, Organized Data section, variables, etc.
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants

objFile = "ToDoList.txt" # An object that represents a file
todoTxt = "" # For opening and closing the target document
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A capture of the user's option selection
taskName = "" # A capture of the user's preferred task name
taskPriority = "" # A capture of the user's priority for the task
myTask = "" # A variable used throughout to reference dictionary values within the list

# -- Processing -- #

# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

import time # Using timer in place of "enter to exit" to avoid double input

todoTxt = open(objFile, "r")
for line in todoTxt:
    strData = line.split(" | ")
    dicRow = {"Task":strData[0].title(), "Priority":strData[1].strip()}
    lstTable.append(dicRow)
todoTxt.close()

# -- Input/Output -- #

# Step 2 - Display a menu of choices to the user
print("Welcome to Task Manager!\n")
while (True):
    print("""
    Menu of Options
    1) Show Current Data
    2) Add a New Item
    3) Remove an Existing Item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Task | Priority")
        for myTask in lstTable:
            print(myTask["Task"], myTask["Priority"], sep=" | ")
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        taskName = input("Task Name: ").title()
        taskPriority = input("Task Priority: ")
        dicRow = {"Task": taskName, "Priority": taskPriority}
        lstTable.append(dicRow)
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        myTask = input("Which Task do you wish to remove: ")
        for dicRow in lstTable:
            if dicRow["Task"].lower() == myTask:
                lstTable.remove(dicRow)
                print("The requested Task has been deleted.")
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        todoTxt = open(objFile, "w")
        for myTask in lstTable:
            todoTxt.write(myTask["Task"] + " | " + myTask["Priority"] + "\n")
        todoTxt.close()
        print("Your Tasks document has been successfully updated.")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Thank you for using Task Manager!")
        time.sleep(3)
        break  # and Exit the program

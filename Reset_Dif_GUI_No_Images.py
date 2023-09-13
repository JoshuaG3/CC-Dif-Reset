import pyautogui
import time
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Reset Dif Tool")

#have WDIpad in the bottom right corner of middle screen
#password = ("af087037")
#store_num = ("121")


def log_in():
    password = password_input.get()
    store_num = store_input.get()

    time.sleep(2)
    pyautogui.click(145, 559)  #clicks to type in store number
    pyautogui.press(['backspace', 'backspace', 'backspace', 'backspace'])
    pyautogui.typewrite(store_num)  #types in the store number in WDIpad
    pyautogui.click(130, 635)  #clicks on SSH to make sure it is selected
    pyautogui.click(270, 687)  #clicks on the CC button on WDIpad
    time.sleep(5)
    pyautogui.click(799, 195) #clicks the ok button when the CC comes up        
    time.sleep(3)
    pyautogui.click(623, 244)  #clicks on the username bar to type
    pyautogui.typewrite("5000")  #types in the username for the CC
    time.sleep(2)
    pyautogui.click(617, 299)   #clicks on the password bar
    pyautogui.typewrite(password)  #types in the password
    pyautogui.click(730, 218)   #clicks the Ok button to login
    time.sleep(5)
    pyautogui.click(642, 18)  #click on the CC screen to make sure its active
    pyautogui.typewrite("5000")   #enters the username on the CC
    time.sleep(2)
    pyautogui.typewrite(["enter"])  #clicks enter to go to the password
    time.sleep(2)
    pyautogui.typewrite(password)  #types in the password
    time.sleep(2)
    pyautogui.typewrite(["enter"])  #clicks enter to log into the CC
    time.sleep(2)
    pyautogui.typewrite("7")   #opening the command prompt
    pyautogui.typewrite(["enter"])
    time.sleep(2)
    pyautogui.typewrite("adx_ipgm:dqstatus -q c:/adx_idt1/EESAFQUE.DAT")  #typing in the command to show the queue
    pyautogui.typewrite(["enter"])
    message.set("Is the queue at more than 0?")  #asking if the shown queue is more than 0
    finish.set("Yes")  #if it is moves onto reseting the dif
    No.set("No")  #if not resets the box and closes the CC

def reset_dif():   #rest of script to reset the dif then clear everything
    return

def clear(): #clears all of the text boxes to get ready for new input
    message.set("The CC is closing...")    
    #create more to close the CC and logout
    labelStoreNum.delete(0, END)
    labelPassword.delete(0, END)
    No.set("")
    finish.set("")
    message.set("")

message = StringVar()
message.set("")
finish = StringVar()
No = StringVar()
finish.set("")
No.set("")

#All of the labels, inputs and buttons
labelStoreNum = Label(root, text="Enter Store Num: ")
labelPassword = Label(root, text="Enter Todays Password: ")

store_input = Entry(root, width=20, borderwidth=5)
password_input = Entry(root, width=20, borderwidth=5)

labelmessage = Label(root, textvariable=message)

start_button = Button(root, text="Start", command=log_in)
yes_button = Button(root, textvariable=finish, command=reset_dif)
no_button = Button(root, textvariable=No, command=clear)

#Placing all of the objects on the screen
start_button.grid(row=2, column=0,padx=0, pady=20, columnspan=2)
labelStoreNum.grid(row=0, column=0, padx=25, pady=5, columnspan=1)
labelPassword.grid(row=1, column=0, padx=25, pady=5, columnspan=1)
store_input.grid(row=0, column=1, padx=25, pady=5, columnspan=1)
password_input.grid(row=1, column=1, padx=25, pady=5, columnspan=1)
labelmessage.grid(row=3, column=0, padx=15, pady=5, columnspan=2)

start_button.grid(row=2, column=0,padx=0, pady=20, columnspan=2)
yes_button.grid(row=4, column=0,padx=0, pady=20, columnspan=1)
no_button.grid(row=4, column=1,padx=0, pady=20, columnspan=1)

root.mainloop()
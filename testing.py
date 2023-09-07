#pygui, opencv, keyboard
import pyautogui
import time
import keyboard
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("CC Dif Reset Tool")

def WDipad_steps():
    store_number = StoreNum_Input.get()

    try:
        a1, a2 = pyautogui.locateCenterOnScreen('imgs/testwdimg.png', confidence=0.9)   #finding WDIpad logo on the taskbar
        pyautogui.click(a1, a2) #clicks logo
    except:
        print("WDipad is not opened")
    time.sleep(1)

    try:
        b1, b2 = pyautogui.locateCenterOnScreen('imgs/locationnumberimg.png', confidence=0.9) #finding and clicking in the location number
    except:
        print("WDipad issue")
    b1 = b1 + 120
    pyautogui.click(b1, b2)
    pyautogui.press('backspace', presses=4)
    pyautogui.typewrite(store_number)
    time.sleep(1)

    try:
        c1, c2 = pyautogui.locateCenterOnScreen('imgs/SSH.png', confidence=0.9) #clicking on the SSH button
    except:
        print("WDipad issue")
    c1 = c1 - 20
    pyautogui.click(c1, c2)
    time.sleep(1)

    try:
        d1, d2 = pyautogui.locateCenterOnScreen('imgs/CCcontroller.png', confidence=0.9)  #clicks the CC Controller button
    except:
        print("WDipad issue")
    pyautogui.click(d1, d2)
    time.sleep(5)

    logging_into_CC()  #calling next function


def logging_into_CC():
    password = Password_Input.get()
    keyboard.press_and_release('enter') #presses enter incase the first time logon button comes up
    LookForPasswordAuth = False
    while LookForPasswordAuth == False:
        try:
            e1, e2 = pyautogui.locateCenterOnScreen('imgs/passwordauth.png', confidence=0.7)    #checking if the CC is up 
            time.sleep(1)
            LookForPasswordAuth = True
        except:
            time.sleep(1)

    e2 = e2 + 15
    pyautogui.typewrite('5000') #typing in the username
    time.sleep(1)
    pyautogui.click(e1, e2)
    pyautogui.typewrite(password)  #typing in the password

    f1, f2 = pyautogui.locateCenterOnScreen('imgs/cancel.png', confidence=0.9)  #finding the cancel button to click on the ok button
    f2 = f2 - 25
    pyautogui.click(f1, f2)
    time.sleep(5)

    pyautogui.write('5000', interval=.15)  #logging in on the CC
    pyautogui.press('enter')
    pyautogui.write(password, interval=.15)
    pyautogui.press('enter')
    time.sleep(3)

    check_dif()



def check_dif():
    time.sleep(2)
    pyautogui.typewrite('7') 
    time.sleep(1) #getting to the command window
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('adx_ipgm:dqstatus -q c:/adx_idt1/EESAFQUE.DAT', interval=.1)  #typing the command to view the queue
    pyautogui.press('enter')
    message.set("Does the dif need to be reset")

            

def page_number(): 
    message.set("")  #function to reset the dif
    g1, g2 = pyautogui.locateCenterOnScreen('imgs/goback.png', confidence=0.9)   #finding image on screen to make the CC window active again
    g2 = g2 + 25 
    pyautogui.click(g1, g2)
    pyautogui.typewrite("`b", interval=.3)
    message.set("What page num?")#asking user what page the CC is on to go to the correct page


def num_1():
    g1, g2 = pyautogui.locateCenterOnScreen('imgs/goback.png', confidence=0.9)   #finding image on screen to make the CC window active again
    g2 = g2 + 25 
    pyautogui.click(g1, g2)
    keyboard.press('page down')
    time.sleep(.5) 
    keyboard.press('page down')
    message.set("Correct page?")

    
def num_2():
    g1, g2 = pyautogui.locateCenterOnScreen('imgs/goback.png', confidence=0.9)   #finding image on screen to make the CC window active again
    g2 = g2 + 25 
    pyautogui.click(g1, g2)
    keyboard.press('page down')
    message.set("Correct page?")

        
def num_3():
    g1, g2 = pyautogui.locateCenterOnScreen('imgs/goback.png', confidence=0.9)   #finding image on screen to make the CC window active again
    g2 = g2 + 25 
    pyautogui.click(g1, g2)
    message.set("Correct page?")

        
def num_4():
    g1, g2 = pyautogui.locateCenterOnScreen('imgs/goback.png', confidence=0.9)   #finding image on screen to make the CC window active again
    g2 = g2 + 25 
    pyautogui.click(g1, g2)
    keyboard.press('page up')
    message.set("Correct page?")

        
def num_5():
    g1, g2 = pyautogui.locateCenterOnScreen('imgs/goback.png', confidence=0.9)   #finding image on screen to make the CC window active again
    g2 = g2 + 25 
    pyautogui.click(g1, g2)
    keyboard.press('page up')
    time.sleep(.5) 
    keyboard.press('page up')
    message.set("Correct page?")

        
def num_6():
    g1, g2 = pyautogui.locateCenterOnScreen('imgs/goback.png', confidence=0.9)   #finding image on screen to make the CC window active again
    g2 = g2 + 25 
    pyautogui.click(g1, g2)
    keyboard.press('page up')
    time.sleep(.5) 
    keyboard.press('page up')
    time.sleep(.5) 
    keyboard.press('page up')  
    message.set("Correct page?")
 
        
def num_7():
    g1, g2 = pyautogui.locateCenterOnScreen('imgs/goback.png', confidence=0.9)   #finding image on screen to make the CC window active again
    g2 = g2 + 25 
    pyautogui.click(g1, g2)
    keyboard.press('page up')
    time.sleep(.5) 
    keyboard.press('page up')
    time.sleep(.5) 
    keyboard.press('page up')
    time.sleep(.5) 
    keyboard.press('page up')
    message.set("Correct page?")

        
def num_8():
    g1, g2 = pyautogui.locateCenterOnScreen('imgs/goback.png', confidence=0.9)   #finding image on screen to make the CC window active again
    g2 = g2 + 25 
    pyautogui.click(g1, g2)
    keyboard.press('page up')
    time.sleep(.5) 
    keyboard.press('page up')
    time.sleep(.5) 
    keyboard.press('page up')
    time.sleep(.5) 
    keyboard.press('page up')
    time.sleep(.5) 
    keyboard.press('page up')
    message.set("Correct page?")

    
def num_9():
    g1, g2 = pyautogui.locateCenterOnScreen('imgs/goback.png', confidence=0.9)   #finding image on screen to make the CC window active again
    g2 = g2 + 25 
    pyautogui.click(g1, g2)
    keyboard.press('page up')
    time.sleep(.5) 
    keyboard.press('page up')
    time.sleep(.5) 
    keyboard.press('page up')
    time.sleep(.5) 
    keyboard.press('page up')
    time.sleep(.5) 
    keyboard.press('page up')
    time.sleep(.5) 
    keyboard.press('page up')
    message.set("Correct page?")

        
def num_10():
    g1, g2 = pyautogui.locateCenterOnScreen('imgs/goback.png', confidence=0.9)   #finding image on screen to make the CC window active again
    g2 = g2 + 25 
    pyautogui.click(g1, g2)
    keyboard.press('page up') 
    time.sleep(.5)             
    keyboard.press('page up')
    time.sleep(.5) 
    keyboard.press('page up')
    time.sleep(.5) 
    keyboard.press('page up')
    time.sleep(.5) 
    keyboard.press('page up')
    time.sleep(.5) 
    keyboard.press('page up')
    time.sleep(.5) 
    keyboard.press('page up')
    message.set("Correct page?")


def reset_diff():  
    message.set("Resetting the Dif")  
    g1, g2 = pyautogui.locateCenterOnScreen('imgs/goback.png', confidence=0.9)   #finding image on screen to make the CC window active again
    g2 = g2 + 25 
    pyautogui.click(g1, g2)
    keyboard.send('f8') 
    time.sleep(1)
    pyautogui.write("y")
    keyboard.send('enter')
    message.set("waiting 30 seconds")
    time.sleep(20)
    message.set("10 more seconds")
    time.sleep(10)
    pyautogui.click(g1, g2)
    keyboard.send('f7') #restarting the process
    time.sleep(3)
    keyboard.send('f3')
    message.set("waiting 20 seconds to check queue...")
    time.sleep(20)
    pyautogui.click(g1, g2)
    keyboard.send('up arrow')  #checking the queue status
    keyboard.send('enter')
    message.set("Is the queue 0?")




def dif_close():  #function to close the dif 
    message.set("Closing CC...")
    g1, g2 = pyautogui.locateCenterOnScreen('imgs/goback.png', confidence=0.9)
    g2 = g2 + 25
    pyautogui.click(g1, g2)
    pyautogui.write("exit")
    pyautogui.press('enter')
    keyboard.send('f9')
    message.set("")
    message.set("http://oppwrp01hdqww:5000/NoOffersdashboard/Home")

def dif_close2():  #function to close the dif 
    message.set("Closing CC...")
    g1, g2 = pyautogui.locateCenterOnScreen('imgs/goback.png', confidence=0.9)
    g2 = g2 + 25
    pyautogui.click(g1, g2)
    keyboard.send('f3')
    pyautogui.write("exit")
    pyautogui.press('enter')
    keyboard.send('f9')
    message.set("")
    message.set("http://oppwrp01hdqww:5000/NoOffersdashboard/Home")



StoreNum_Label = Label(root, text="Store Number: ")
StoreNum_Input = Entry(root, width=20, borderwidth=5)

Password_Label = Label(root, text="Password: ")
Password_Input = Entry(root, width=20, borderwidth=5)

Start_Button = Button(root, text="Start Script", command=WDipad_steps)

Yes_Button = Button(root,text="Yes-Reset", command=page_number)
No_Button = Button(root, text="No-Exit", command=dif_close2)

Button1 = Button(root, text="  1  ", command=num_1)
Button2 = Button(root, text="  2  ", command=num_2)
Button3 = Button(root, text="  3  ", command=num_3)
Button4 = Button(root, text="  4  ", command=num_4)
Button5 = Button(root, text="  5  ", command=num_5)
Button6 = Button(root, text="  6  ", command=num_6)
Button7 = Button(root, text="  7  ", command=num_7)
Button8 = Button(root, text="  8  ", command=num_8)
Button9 = Button(root, text="  9  ", command=num_9)
Button10 = Button(root, text="  10  ", command=num_10)

Close_cc = Button(root, text="Close CC", command=dif_close)
Restart_button = Button(root, text="Restart Process", command=WDipad_steps)

Correct_page_yes = Button(root, text="Correct Page Yes", command=reset_diff)

message = StringVar()
message.set("")
Message_label = Label(root, textvariable=message)

StoreNum_Label.grid(column=0, row=0)
StoreNum_Input.grid(column=1, row=0)
Password_Label.grid(column=0, row=1)
Password_Input.grid(column=1, row=1)
Start_Button.grid(column=0, row=2, columnspan=3)
Yes_Button.grid(column=0 , row=3)
No_Button.grid(column=2, row=3)
Close_cc.grid(column=0, row=10)
Restart_button.grid(column=2, row=10)


Button1.grid(column=0, row=4)
Button2.grid(column=1, row=4)
Button3.grid(column=2, row=4)
Button4.grid(column=0, row=5)
Button5.grid(column=1, row=5)
Button6.grid(column=2, row=5)
Button7.grid(column=0, row=6)
Button8.grid(column=1, row=6)
Button9.grid(column=2, row=6)
Button10.grid(column=1, row=7)

Correct_page_yes.grid(column=0, row=8, columnspan=3)
Message_label.grid(column=0, columnspan=2, row=9)



root.mainloop()
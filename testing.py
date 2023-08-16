#pygui, opencv, keyboard
import pyautogui
import time
import keyboard


def WDipad_steps(store_number):
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
    keyboard.press_and_release('enter')
    time.sleep(3) #presses enter incase the first time logon button comes up

    try:
        e1, e2 = pyautogui.locateCenterOnScreen('imgs/passwordauth.png', confidence=0.7)   #checking if the CC is up 
    except:
        print("CC is down")
        exit()

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
    pyautogui.typewrite('7')  #getting to the command window
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('adx_ipgm:dqstatus -q c:/adx_idt1/EESAFQUE.DAT', interval=.1)  #typing the command to view the queue
    pyautogui.press('enter')
    while True:
        diff_reset = input("Is the queue higher than 0? (y, n): ")   #loop to ask the user if the CC needs to be reset
        if diff_reset == "y":
            reset_dif()
            break
        elif diff_reset == "n":
            dif_close()
            break
        else:
            print("Not a valid input, try again...")

            

def reset_dif():   #function to reset the dif
    print("Resetting the diff...")
    g1, g2 = pyautogui.locateCenterOnScreen('imgs/goback.png', confidence=0.9)   #finding image on screen to make the CC window active again
    g2 = g2 + 25 
    pyautogui.click(g1, g2)
    pyautogui.typewrite("`b", interval=.3)

    if pyautogui.locateCenterOnScreen('imgs/pagenums/page1.png'):
        print("page 1 found")
        keyboard.press('page down')
        keyboard.press('page down')
    elif pyautogui.locateCenterOnScreen('imgs/pagenums/page2.png'):
        print("page 2 found")
        keyboard.press('page down')
    elif pyautogui.locateCenterOnScreen('imgs/pagenums/page3.png'):
        print("page 3 found")
    elif pyautogui.locateCenterOnScreen('imgs/pagenums/page4.png'):
        print("page 4 found")
        keyboard.press('page up')
    elif pyautogui.locateCenterOnScreen('imgs/pagenums/page5.png'):
        print("page 5 found")
        keyboard.press('page up')
        keyboard.press('page up')
    elif pyautogui.locateCenterOnScreen('imgs/pagenums/page6.png'):
        print("page 6 found")    
        keyboard.press('page up')
        keyboard.press('page up')
        keyboard.press('page up')    
    elif pyautogui.locateCenterOnScreen('imgs/pagenums/page7.png'):
        print("page 7 found")
        keyboard.press('page up')
        keyboard.press('page up')
        keyboard.press('page up')
        keyboard.press('page up')
    elif pyautogui.locateCenterOnScreen('imgs/pagenums/page8.png'):
        print("page 8 found")
        keyboard.press('page up')
        keyboard.press('page up')
        keyboard.press('page up')
        keyboard.press('page up')
        keyboard.press('page up')
    elif pyautogui.locateCenterOnScreen('imgs/pagenums/page9.png'):
        print("page 9 found")
        keyboard.press('page up')
        keyboard.press('page up')
        keyboard.press('page up')
        keyboard.press('page up')
        keyboard.press('page up')
        keyboard.press('page up')
    elif pyautogui.locateCenterOnScreen('imgs/pagenums/page10.png'):
        print("page 10 found")   
        keyboard.press('page up')             
        keyboard.press('page up')
        keyboard.press('page up')
        keyboard.press('page up')
        keyboard.press('page up')
        keyboard.press('page up')
        keyboard.press('page up')
    else:
        print("Error finding page number: ")
         
        




def dif_full_close():
    keyboard.send('f3')
    pyautogui.write("exit")
    keyboard.send('enter')
    keyboard.send('f9')





def dif_close():  #function to close the dif 
    print("Closing CC...")
    g1, g2 = pyautogui.locateCenterOnScreen('imgs/goback.png', confidence=0.9)
    g2 = g2 + 25
    pyautogui.click(g1, g2)
    pyautogui.write("exit")
    pyautogui.press('enter')
    keyboard.send('f9')



store_number = input("What is the store number?: ")
password = "af055840"  #changes daily

WDipad_steps(store_number)
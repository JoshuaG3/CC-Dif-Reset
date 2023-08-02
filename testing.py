#pygui, opencv
import pyautogui
import time


def WDipad_steps():
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
    pyautogui.typewrite(storenum)
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
    pyautogui.press('enter') #presses enter incase the first time logon button comes up

    try:
        e1, e2 = pyautogui.locateCenterOnScreen('imgs/passwordauth.png', confidence=0.9)   #checking if the CC is up 
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

    reset_dif()



def reset_dif():
    pyautogui.typewrite('7')  #getting to the command window
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('adx_ipgm:dqstatus -q c:/adx_idt1/EESAFQUE.DAT', interval=.1)  #typing the command to view the queue
    pyautogui.press('enter')



storenum = "2187"
password = "af138722"  #changes daily

WDipad_steps()
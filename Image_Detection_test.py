import pyautogui
import time
import keyboard

store_number = ("2509")
password = ("af541382")
Username = ("5000")


def WDipad_steps():  #Opens WDIpad, enters the store num, clicks SSH and clicks CC
    try:
        a1, a2 = pyautogui.locateCenterOnScreen('imgs/testwdimg.png', confidence=0.9)   
        pyautogui.click(a1, a2) #clicks logo
    except:
        print("WDipad is not opened")
    time.sleep(1)

    try:
        b1, b2 = pyautogui.locateCenterOnScreen('imgs/locationnumberimg.png', confidence=0.9) 
    except:
        print("WDipad issue")
    b1 = b1 + 120
    pyautogui.click(b1, b2)
    pyautogui.press('backspace', presses=4)
    pyautogui.typewrite(store_number)
    time.sleep(1)

    try:
        c1, c2 = pyautogui.locateCenterOnScreen('imgs/SSH.png', confidence=0.9) 
    except:
        print("WDipad issue")
    c1 = c1 - 20
    pyautogui.click(c1, c2)
    time.sleep(1)

    try:
        d1, d2 = pyautogui.locateCenterOnScreen('imgs/CCcontroller.png', confidence=0.9)  
    except:
        print("WDipad issue")
    pyautogui.click(d1, d2)
    time.sleep(5)

    logging_into_CC() 




def logging_into_CC():  #Types the username and password into both screens
    keyboard.press_and_release('enter') 
    LookForPasswordAuth = False
    while LookForPasswordAuth == False:
        try:
            e1, e2 = pyautogui.locateCenterOnScreen('imgs/passwordauth.png', confidence=0.7)    
            time.sleep(1)
            LookForPasswordAuth = True
        except:
            time.sleep(1)

    e2 = e2 + 15
    pyautogui.typewrite(Username) 
    time.sleep(1)
    pyautogui.click(e1, e2)
    pyautogui.typewrite(password)  

    f1, f2 = pyautogui.locateCenterOnScreen('imgs/cancel.png', confidence=0.9)  
    f2 = f2 - 25
    pyautogui.click(f1, f2)
    time.sleep(5)

    pyautogui.write(Username, interval=.15)  
    pyautogui.press('enter')
    pyautogui.write(password, interval=.15)
    pyautogui.press('enter')
    time.sleep(3)
    check_dif()




def check_dif():  #Goes to the command screen and types the command to see the queue 
    time.sleep(2)
    pyautogui.typewrite('7') 
    time.sleep(1) 
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('adx_ipgm:dqstatus -q c:/adx_idt1/EESAFQUE.DAT', interval=.1)  
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.typewrite("`b", interval=.5)
    time.sleep(1)
    find_page_number()






def find_page_number():  #Finds what page it is on then changes it to page 3
    time.sleep(2)
    if pyautogui.locateOnScreen('test_images/page1.png', confidence=0.99):
        print("page 1")
        keyboard.press('page down')
        time.sleep(.5) 
        keyboard.press('page down')
        test_page_verify()
    elif pyautogui.locateOnScreen('test_images/page2.png', confidence=0.99):
        print("page 2")
        keyboard.press('page down')
        test_page_verify()
    elif pyautogui.locateOnScreen('test_images/page3.png', confidence=0.99):
        print("page 3")
        test_page_verify()
    elif pyautogui.locateOnScreen('test_images/page4.png', confidence=0.99):
        print("page 4")
        keyboard.press('page up')
        test_page_verify()
    elif pyautogui.locateOnScreen('test_images/page5.png', confidence=0.99):
        print("page 5")
        keyboard.press('page up')
        time.sleep(.5) 
        keyboard.press('page up')
        test_page_verify()
    elif pyautogui.locateOnScreen('test_images/page6.png', confidence=0.99):
        print("page 6")
        keyboard.press('page up')
        time.sleep(.5) 
        keyboard.press('page up')
        time.sleep(.5) 
        keyboard.press('page up')
        test_page_verify()
    elif pyautogui.locateOnScreen('test_images/page7.png', confidence=0.99):
        print("page 7")
        keyboard.press('page up')
        time.sleep(.5) 
        keyboard.press('page up')
        time.sleep(.5) 
        keyboard.press('page up')
        time.sleep(.5) 
        keyboard.press('page up')
        test_page_verify()
    elif pyautogui.locateOnScreen('test_images/page8.png', confidence=0.99):
        print("page 8")
        keyboard.press('page up')
        time.sleep(.5) 
        keyboard.press('page up')
        time.sleep(.5) 
        keyboard.press('page up')
        time.sleep(.5) 
        keyboard.press('page up')
        time.sleep(.5) 
        keyboard.press('page up')
        test_page_verify()
    elif pyautogui.locateOnScreen('test_images/page9.png', confidence=0.99):
        print("page 9")
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
        test_page_verify()
    elif pyautogui.locateOnScreen('test_images/page10.png', confidence=0.99):
        print("page 10")
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
        test_page_verify()
    else:
        print("None were found")




def test_page_verify():  #verifies on correct page
    time.sleep(2)
    if pyautogui.locateOnScreen('test_images/DifService.png', confidence=0.99):
        print("On correct page")
        time.sleep(2)
        #closing_cc()   #when ready change this to  reset_diff()
    else:
        print("NOT ON RIGHT PAGE")


def reset_diff():  #Resets the dif, waits then restarts it
    keyboard.send('f8') 
    time.sleep(1)
    pyautogui.write("y")
    keyboard.send('enter')
    print("waiting 30 seconds")
    time.sleep(20)
    print("10 more seconds")
    time.sleep(10)
    keyboard.send('f7') 
    closing_cc()



def closing_cc():  #Logs off and closes the CC
    time.sleep(5)
    keyboard.send('f3')
    time.sleep(1)
    pyautogui.write("exit")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    keyboard.send('f9')


WDipad_steps() 
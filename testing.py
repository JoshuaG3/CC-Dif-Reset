#pygui, opencv
import pyautogui
import time

storenum = "2187"
password = "af138722"  #changes daily

a1, a2 = pyautogui.locateCenterOnScreen('imgs/testwdimg.png', confidence=0.9)   #finding WDIpad logo on the taskbar
pyautogui.click(a1, a2) #clicks logo
time.sleep(1)

b1, b2 = pyautogui.locateCenterOnScreen('imgs/locationnumberimg.png', confidence=0.9) #finding and clicking in the location number
b1 = b1 + 120
pyautogui.click(b1, b2)
pyautogui.press('backspace', presses=4)
pyautogui.typewrite(storenum)
time.sleep(1)

c1, c2 = pyautogui.locateCenterOnScreen('imgs/SSH.png', confidence=0.9) #clicking on the SSH button
c1 = c1 - 20
pyautogui.click(c1, c2)
time.sleep(1)

d1, d2 = pyautogui.locateCenterOnScreen('imgs/CCcontroller.png', confidence=0.9)  #clicks the CC Controller button
pyautogui.click(d1, d2)
time.sleep(5)

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

pyautogui.typewrite('7')  #getting to the command window
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('adx_ipgm:dqstatus -q c:/adx_idt1/EESAFQUE.DAT', interval=.1)  #typing the command to view the queue
pyautogui.press('enter')
#pygui, opencv
import pyautogui
import time

storenum = "2187"

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

e1, e2 = pyautogui.locateCenterOnScreen('imgs/logoimg.png', confidence=0.9)  #working on clicking on first ok button even if its not there
e1 = e1 + 597
e2 = e2 - 11
pyautogui.click(e1, e2)
time.sleep(5)

#try:
 #   e1, e2 = pyautogui.locateCenterOnScreen('imgs/logoimg.png', confidence=0.9)
  #  e2 = e2 - 100
   # e1 = e1 - 200
    #pyautogui.click(e1, e2)
    #f1, f2 = pyautogui.locateCenterOnScreen('imgs/passwordauth.png', confidence=0.9)
    #pyautogui.click(f1, f2)
#except:
 #   print("CC is offline")

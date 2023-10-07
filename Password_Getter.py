from selenium import webdriver
import time
import pyperclip
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
import pyautogui
from cryptography.fernet import Fernet
import os

os.chdir(r"C:\Users\gouldj\Desktop\Programming Projects\CC automation")

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


try:  #opens the website
    driver.set_page_load_timeout(1)
    driver.get("http://shdpro/Passwords/POS/POS_Daily_Passwords.asp") 
except TimeoutException as ex:
    pass
    isrunning = 0
    print("Exception has been thrown. " + str(ex))
    print("Website Error")
    driver.close() 

time.sleep(3)

#copies the password and saves into variable
a1, a2 = pyautogui.locateCenterOnScreen('imgs/5000img.png', confidence=.9)
a1 -= 46
a2 += 24
pyautogui.click(a1, a2)
pyautogui.dragTo(287, 268, button='left')
time.sleep(.5)
pyautogui.hotkey('ctrl', 'c')
password = pyperclip.paste()



#generate key and write it in a file
key = Fernet.generate_key()
f = open("refKey.txt", "wb")
f.write(key)
f.close()

#encrypt the password and write it in a file
refKey = Fernet(key)
mypwdbyt = bytes(password, 'utf-8') # convert into byte
encryptedPWD = refKey.encrypt(mypwdbyt)
f = open("encryptedPWD.txt", "wb")
f.write(encryptedPWD)
f.close()





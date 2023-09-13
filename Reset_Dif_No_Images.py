import pyautogui
import time

#have WDIpad in the bottom right corner of middle screen
password = ("af087037")
store_num = ("121")


def log_in(password, store_num):
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


log_in(password, store_num)
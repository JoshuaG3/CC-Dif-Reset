import pyautogui
import time
import keyboard

store_number = (2337)
store_num_string = str(store_number)
password = ("af757488")
Username = ("5000")

stores = [2, 3, 5, 7, 8, 12, 18, 19, 25, 28, 30, 32, 40, 51, 54, 60, 67, 68, 70, 77, 81, 84, 85, 86, 93, 94, 96, 103, 104, 106,
            108, 112, 115, 121, 123, 129, 135, 138, 140, 142, 144, 151, 153, 159, 163, 166, 168, 169, 171, 174, 176, 177, 179,
            180, 182, 184, 186, 190, 191, 195, 196, 197, 198, 199, 201, 203, 210, 212, 213, 214, 226, 231, 233, 235, 236, 237,
            239, 242, 243, 246, 247, 249, 250, 251, 252, 254, 262, 267, 270, 271, 274, 280, 283, 286, 287, 290, 291, 292, 304,
            305, 306, 308, 309, 311, 317, 318, 319, 324, 328, 330, 331, 333, 336, 343, 349, 352, 353, 355, 357, 358, 359, 361, 
            364, 366, 369, 370, 371, 373, 378, 381, 384, 385, 386, 387, 388, 396, 397, 388, 396, 397, 398, 407, 411, 412, 426,
            428, 433, 435, 436, 437, 439, 442, 443, 435, 436, 437, 439, 442, 443, 445, 446, 447, 448, 451, 456, 457, 458, 461,
            464, 473, 478, 479, 481, 483, 487, 488, 493, 494, 496, 498, 500, 501, 504, 506, 507, 509, 510, 511, 517, 526, 527,
            528, 533, 535, 538, 541, 543, 548, 549, 551, 552, 555, 556, 558, 560, 566, 570, 572, 577, 579, 580, 590, 591, 595,
            599, 606, 607, 608, 609, 611, 612, 619, 630, 631, 632, 639, 640, 644, 648, 649, 652, 655, 656, 657, 658, 662, 664,
            671, 672, 681, 683, 684, 687, 697, 698, 701, 702, 705, 708, 710, 711, 713, 720, 721, 726, 728, 729, 736, 737, 741, 
            743, 745, 750, 751, 757, 761, 767, 768, 773, 777, 1329, 1333, 1404, 1405, 1411, 1412, 1426, 1430, 1432, 1439, 1440,
            1443, 1444, 1448, 1449, 1461, 1463, 1472, 1478, 1479, 1489, 1500, 1501, 1502, 1504, 1511, 1513, 1537, 1576, 1577, 
            1581, 1583, 1588, 1590, 1601, 1616, 1617, 1627, 1630, 1631, 1639, 1654, 1655, 1665, 1658, 1661, 1662, 1667, 1671, 
            1682, 1688, 1689, 1690, 1692, 1694, 1697, 1710, 1711, 1712, 1715, 1716, 1717, 2187, 2203, 2206, 2207, 2210, 2215, 
            2219, 2220, 2223, 2225, 2229, 2230, 2234, 2237, 2238, 2244, 2246, 2247, 2249, 2252, 2258, 2261, 2263, 2266, 2269, 
            2271, 2273, 2274, 2278, 2288, 2304, 2306, 2307, 2309, 2311, 2313, 2315, 2318, 2320, 2325, 2326, 2327, 2328, 2329, 
            2331, 2333, 2335, 2336, 2337, 2342, 2343, 2348, 2349, 2354, 2355, 2364, 2366, 2367, 2380, 2388, 2394, 2398, 2400, 
            2404, 2409, 2411, 2413, 2415, 2421, 2422, 2423, 2425, 2427, 2429, 2430, 2433, 2435, 2437, 2439, 2441, 2443, 2444,
            2445, 2448, 2450, 2454, 2455, 2456, 2459, 2461, 2462, 2465, 2468, 2472, 2474, 2475, 2477, 2480, 2484, 2487, 2488,
            2491, 2495, 2499, 2501, 2503, 2505, 2507, 2509, 2511, 2515, 2517, 2519, 2521, 2523, 2527, 2529, 2531, 2533, 2545,
            2548, 2550, 2556, 2557, 2558, 2560, 2562, 2564, 2566, 2567, 2568, 2570, 2571, 2626, 2799]



def WDipad_steps_non_liquor():  #Opens WDIpad, enters the store num, clicks SSH and clicks CC
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
    pyautogui.typewrite(store_num_string)
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




def Wdipad_steps_liquor():
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
    pyautogui.typewrite(store_num_string)
    time.sleep(1)

    try:
        d1, d2 = pyautogui.locateCenterOnScreen('imgs/CCcontrollerLiquor.png', confidence=0.9)  
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
    time.sleep(3)

    pyautogui.write(Username, interval=.15)  
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(password, interval=.15)
    pyautogui.press('enter')
    time.sleep(3)
    find_page_number()





def find_page_number():  #Finds what page it is on then changes it to page 3
    pyautogui.typewrite("`b", interval=.5)
    time.sleep(2)
    if pyautogui.locateOnScreen('test_images/page1.png', confidence=0.99):
        print("page 1")
        for i in range(2):  
            keyboard.press('page down')
            time.sleep(.5)
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
        for i in range(2):  
            keyboard.press('page up')
            time.sleep(.5)
        test_page_verify()
    elif pyautogui.locateOnScreen('test_images/page6.png', confidence=0.99):
        print("page 6")
        for i in range(3):  
            keyboard.press('page up')
            time.sleep(.5)
        test_page_verify()
    elif pyautogui.locateOnScreen('test_images/page7.png', confidence=0.99):
        print("page 7")
        for i in range(4):  
            keyboard.press('page up')
            time.sleep(.5)
        test_page_verify()
    elif pyautogui.locateOnScreen('test_images/page8.png', confidence=0.99):
        print("page 8")
        for i in range(5):  
            keyboard.press('page up')
            time.sleep(.5)
        test_page_verify()
    elif pyautogui.locateOnScreen('test_images/page9.png', confidence=0.99):
        print("page 9")
        for i in range(6):  
            keyboard.press('page up')
            time.sleep(.5)
        test_page_verify()
    elif pyautogui.locateOnScreen('test_images/page10.png', confidence=0.99):
        print("page 10")
        for i in range(7):  
            keyboard.press('page up')
            time.sleep(.5)
        test_page_verify()
    else:
        print("None were found")




def test_page_verify():  #verifies on correct page
    time.sleep(2)
    if pyautogui.locateOnScreen('test_images/DifService.png', confidence=0.99):
        print("On correct page")
        time.sleep(2)
        closing_cc()   #when ready change this to  reset_diff()
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
    print("Closing the CC")
    time.sleep(5)
    keyboard.send('f3')
    time.sleep(1)
    keyboard.send('f9')
    time.sleep(2)
    g1, g2 = pyautogui.locateCenterOnScreen('imgs/goback.png', confidence=0.9)
    g1 = g1 + 482
    g2 = g2 - 48
    pyautogui.click(g1, g2)
    time.sleep(.5)
    h1, h2 = pyautogui.locateCenterOnScreen('imgs/OkButton.png', confidence=0.9)
    pyautogui.click(h1, h2)
    time.sleep(.5)
    a1, a2 = pyautogui.locateCenterOnScreen('imgs/testwdimg.png', confidence=0.9)   
    pyautogui.click(a1, a2)



if store_number in stores:
    WDipad_steps_non_liquor()
else:
    Wdipad_steps_liquor()
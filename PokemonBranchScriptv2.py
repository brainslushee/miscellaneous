import string
import pyautogui
import time

pkmnIndex = 0
#Change the second number for number of pokemon
for num in range (0, 52):
    ##Click add a subtopic
    pyautogui.click(366, 263)
    time.sleep(1)
    ##Click Excel tab
    pyautogui.click(268, 10)
    ##Click first entry
    pyautogui.click(138, 929)
    pyautogui.press('down')
    pyautogui.hotkey('ctrl', 'c')
    ##Click Mr Owl tab
    pyautogui.click(76, 8)
    ##Click Topic Name
    pyautogui.click(383, 391)
    pyautogui.hotkey('ctrl', 'v')
    ##Click Submit
    pyautogui.click(382, 543)
    time.sleep(2)
    ##Click edit
    pyautogui.click(1899, 366)
    time.sleep(2)

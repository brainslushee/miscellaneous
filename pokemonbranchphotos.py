import string
import pyautogui
import time

pkmnIndex = 0

for num in range (0, 156):
    ##Click Excel tab
    pyautogui.click(268, 10)
    ##Click first entry
    pyautogui.click(138, 929)
    pyautogui.press('down')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(87, 7)
    for num in range (0, 2):
        pyautogui.click(600, 45)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(1636, 302)
    time.sleep(1)
    pyautogui.click(622, 197)
    time.sleep(1)
    pyautogui.click(381, 238)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.click(762, 510)
    time.sleep(1)
    pyautogui.click(385, 292)
    time.sleep(1)

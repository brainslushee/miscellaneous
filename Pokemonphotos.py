import string
import pyautogui
import time

pkmnIndex = 0

for num in range (0, 52):
    ##Click Excel tab
    pyautogui.click(268, 10)
    pyautogui.click(138, 929)
    pyautogui.press('down')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(489, 7)
    time.sleep(1)
    pyautogui.rightClick(714, 708)
    time.sleep(1)
    pyautogui.click(755,746)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.click(768, 502)
    time.sleep(1)
    pyautogui.click(1356, 261)

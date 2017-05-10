import string
import pyautogui
import time

pkmnIndex = 0

for num in range (0, 135):
    ##Click Excel tab
    pyautogui.click(268, 10)
    ##Click first entry
    for num in range (0, 16):
        pyautogui.press('pageup')
    ##Click first entry
    pyautogui.click(135, 236)
    for num in range (0, pkmnIndex):
        pyautogui.press('down')
    pkmnIndex += 1
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(87, 7)
    for num in range (0, 2):
        pyautogui.click(600, 45)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(1636, 302)
    time.sleep(1)
    #Edit Topic Title & Description
    pyautogui.click(492, 196)
    time.sleep(1)
    ##Click Pokedex Tab
    pyautogui.click(489, 7)
    for num in range (0, 3):
        pyautogui.click(1262, 485)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(1417, 307)
    #Remove Accents
    pyautogui.click(654, 8)
    for num in range (0, 3):
        pyautogui.click(545, 202)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.click(548, 366)
    time.sleep(2)
    for num in range (0, 3):
        pyautogui.click(544, 453)
    pyautogui.hotkey('ctrl', 'c')
    #Return to Mr. Owl
    pyautogui.click(87, 7)
    pyautogui.click(390, 275)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.click(423, 320)
    time.sleep(1)

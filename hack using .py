import pyautogui
import time
pyautogui.FAILSAFE = False
while True:
    time.sleep(10)
    for i in range(0, 100):
        pyautogui.moveTo(1, i * 5)
    for i in range(0, 3):
        pyautogui.press('harshil')

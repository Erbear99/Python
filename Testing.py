import keyboard
import pyautogui
pyautogui.PAUSE = 0.002
toggle = False
changed = False
while True:
    if keyboard.is_pressed('q') and keyboard.is_pressed('shift') and not changed:
        changed = True
        toggle = not toggle
        print('toggled')
    if not keyboard.is_pressed('q') and keyboard.is_pressed('shift') and changed:
        changed = False
    if toggle:
        pyautogui.click()

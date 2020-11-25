# Python 3.7 
# To install with pip, run: pip install pyautogui
# PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen. To disable this fail-safe, set pyautogui.
# FAILSAFE to False. DISABLING FAIL-SAFE IS NOT RECOMMENDED.

import pyautogui

pyautogui.moveRel(0, 50, duration=4)
pyautogui.moveRel(50, 0, duration=4)
# pyautogui.hotkey("ctrl", "a")
pyautogui.mouseUp(20, 10, button='right')
# pyautogui.alert(text='Alert', title='Alert', button='OK')



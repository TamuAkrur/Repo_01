import pyautogui
from datetime import datetime
import os
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        # today = date.today()
        now = datetime.now()
        xyz = now.strftime('%H:%M')
        print("Today's date:", xyz)
        if xyz == "10:26":
            os.system('shutdown -s -t 0')
        else:
            pass
except KeyboardInterrupt:
    print('\n')


import pywhatkit
import time
import pyautogui
import datetime




for i in range(0,5):
    HOUR = datetime.datetime.now().hour  # the current hour
    MINUTE = datetime.datetime.now().minute  # the current minute
    pywhatkit.sendwhatmsg('+917585848226','Hello Mote',HOUR,MINUTE+1,30)
    import keyboard as k

    pyautogui.click(1050, 950)
    time.sleep(2)
    k.press_and_release('enter')

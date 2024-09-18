import pyautogui
import pydirectinput

import threading
import logging
import time

log = logging.getLogger(__name__)

def map():
    while True:
        woods_img = pyautogui.locateOnScreen('images/groundzero.png', confidence=0.7)
        if woods_img is not None:
            logging.info("Selecting Ground Zero")
            pydirectinput.click(woods_img.left + 20, woods_img.top + 20)
            time.sleep(1)
            ready_img = pyautogui.locateOnScreen('images/ready.png', confidence=0.7)
            pydirectinput.click(ready_img.left + 20, ready_img.top + 20)
            

def run():
    map_thread = threading.Thread(target=map)
    map_thread.start()
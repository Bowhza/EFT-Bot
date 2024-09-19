import pyautogui
import pydirectinput

import threading
import logging
import time

log = logging.getLogger(__name__)

# Alias for the ImageNotFoundException so you dont need to type it out every time.
ImageNotFound = pyautogui.ImageNotFoundException

def map():
    while True:
        try:
            streets_img = pyautogui.locateOnScreen('images/streets.png', confidence=0.7)
            if streets_img is not None:
                logging.info("Selecting Streets of Tarkov")
                pydirectinput.click(streets_img.left + 20, streets_img.top + 20)
                time.sleep(1)
                ready_img = pyautogui.locateOnScreen('images/ready.png', confidence=0.7)
                if ready_img is not None:
                    pydirectinput.click(ready_img.left + 20, ready_img.top + 20)
        except ImageNotFound:
            pass

def run():
    map_thread = threading.Thread(target=map)
    map_thread.start()

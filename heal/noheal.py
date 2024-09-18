import pyautogui
import pydirectinput

import threading
import logging
import time

log = logging.getLogger(__name__)

def heal():
    while True:
        if pyautogui.locateOnScreen('images/healskip.png', grayscale=True, confidence=0.75) != None:
            pydirectinput.click(1056, 574)
            logging.info("heal skip detected")
            time.sleep(1.5)

        elif pyautogui.locateOnScreen('images/dead.png', confidence=0.75) != None:
            logging.info("Died or MIA")
            next_img = pyautogui.locateOnScreen('images/next.png', grayscale=True, confidence=0.7)
            for x in range(5):
                pydirectinput.click(next_img.left + 20, next_img.top + 20)
                time.sleep(1)
                


def run():
    heal_thread = threading.Thread(target=heal)
    heal_thread.start()
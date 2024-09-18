import pyautogui
import pydirectinput

import threading
import logging
import time

log = logging.getLogger(__name__)

def heal():
    while True:
        if pyautogui.locateOnScreen('images/healskip.png', grayscale=True, confidence=0.9) != None:
            pydirectinput.click(1056, 574)
            logging.info("heal skip detected")
            time.sleep(1.5)

        elif pyautogui.locateOnScreen('images/dead.png', grayscale=False, confidence=0.75) != None:
            logging.info("Died or MIA")
            next_img = pyautogui.locateOnScreen('images/next.png', grayscale=True, confidence=0.7)
            for x in range(4):
                pydirectinput.click(next_img.left + 20, next_img.top + 20)
                time.sleep(1)
                
            apply_button = pyautogui.locateOnScreen('images/apply.png', grayscale=True, confidence=0.7)
            pydirectinput.click(apply_button.left + 20, apply_button.top + 20)
            time.sleep(1)

            pydirectinput.click(next_img.left + 20, next_img.top + 20)


def run():
    heal_thread = threading.Thread(target=heal)
    heal_thread.start()
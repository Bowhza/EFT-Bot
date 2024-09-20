import pyautogui
import pydirectinput

import threading
import logging
import time

log = logging.getLogger(__name__)

# Alias for the ImageNotFoundException, so you don't need to type it out every time.
ImageNotFound = pyautogui.ImageNotFoundException


def heal():
    while True:
        try:
            if pyautogui.locateOnScreen('images/dead.png', grayscale=False, confidence=0.6) is not None:
                logging.info("Died or MIA")
        except ImageNotFound:
            pass
        
        try:
            next_img = pyautogui.locateOnScreen('images/next.png', grayscale=True, confidence=0.7)
            if next_img is not None:
                for _ in range(4):
                    pydirectinput.click(next_img.left + 20, next_img.top + 20)
                    time.sleep(1)
            
            general_health = pyautogui.locateOnScreen('images/general_health.png', grayscale=True, confidence=0.7)
            if general_health is not None:
                pydirectinput.click(general_health.left + 20, general_health.top + 20)
                time.sleep(1)
                apply_button = pyautogui.locateOnScreen('images/apply.png', grayscale=True, confidence=0.7)
                if apply_button is not None:
                    pydirectinput.click(apply_button.left + 20, apply_button.top + 20)
                    time.sleep(1)
                pydirectinput.click(next_img.left + 20, next_img.top + 20)
        except ImageNotFound:
            pass    

        time.sleep(1)

import pyautogui
import pydirectinput
import threading
import logging
import time

log = logging.getLogger(__name__)

# Alias for the ImageNotFoundException so you dont need to type it out every time.
ImageNotFound = pyautogui.ImageNotFoundException


def run_map(map_name):
    
    while True:
        try:
            map_img = pyautogui.locateOnScreen(f"images/{map_name}.png", confidence=0.7)
            if map_img is not None:
                logging.info(f"Selecting {map_name.capitalize()}")
                pydirectinput.click(map_img.left + 20, map_img.top + 20)
                time.sleep(1)
                ready_img = pyautogui.locateOnScreen('images/ready.png', confidence=0.7)
                if ready_img is not None:
                    pydirectinput.click(ready_img.left + 20, ready_img.top + 20)
        except ImageNotFound:
            pass


def run(map_name):
    map_thread = threading.Thread(target=run_map, args=map_name)
    map_thread.start()

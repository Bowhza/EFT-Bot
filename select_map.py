import pyautogui
import pydirectinput
import threading
import logging
import time
from tools.image_scale import locate_image_on_screen

log = logging.getLogger(__name__)

# Alias for the ImageNotFoundException, so you don't need to type it out every time.
ImageNotFound = pyautogui.ImageNotFoundException


def run_map(map_name, scale_factor=1):
    while True:
        try:
            map_img = locate_image_on_screen(f"{map_name}.png", scale_factor, confidence=0.7)
            if map_img is not None:
                logging.info(f"Selecting {map_name.capitalize()}")
                pydirectinput.click(map_img.left + 20, map_img.top + 20)
                time.sleep(1)
                ready_img = locate_image_on_screen('ready.png', scale_factor, confidence=0.7)
                if ready_img is not None:
                    pydirectinput.click(ready_img.left + 20, ready_img.top + 20)
        except ImageNotFound:
            pass

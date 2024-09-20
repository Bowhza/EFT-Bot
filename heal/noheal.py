import pyautogui
import pydirectinput
import logging
import time

from tools.image_scale import locate_image_on_screen

log = logging.getLogger(__name__)

# Alias for the ImageNotFoundException, so you don't need to type it out every time.
ImageNotFound = pyautogui.ImageNotFoundException


def heal(scale_factor=1):
    while True:
        try:
            if locate_image_on_screen('dead.png', scale_factor, confidence=0.75) is not None:
                logging.info("Died or MIA")
                next_img = locate_image_on_screen('next.png', scale_factor, confidence=0.7)
                for x in range(5):
                    if next_img is not None:
                        pydirectinput.click(next_img.left + 20, next_img.top + 20)
                        time.sleep(1)
        except ImageNotFound:
            pass

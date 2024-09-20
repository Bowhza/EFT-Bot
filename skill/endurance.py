import pyautogui
import pydirectinput
import logging
import time
import threading
import keyboard
from tools.image_scale import locate_image_on_screen
from stopwatch import Stopwatch

# Stopwatch with 2 decimal place accuracy
stopwatch = Stopwatch(2)
stopwatch.stop()

# Raid Counter
raid_counter = 0

log = logging.getLogger(__name__)

# Alias for the ImageNotFoundException, so you don't need to type it out every time.
ImageNotFound = pyautogui.ImageNotFoundException


def _restart_game():
    while True:
        time.sleep(21600)
        pause_event.wait()
        logging.info('Restarting game')

        pydirectinput.keyUp('shift')
        pydirectinput.keyUp('w')
        pydirectinput.keyDown('alt')
        pydirectinput.keyDown('f4')
        pydirectinput.keyUp('alt')
        pydirectinput.keyUp('f4')


def game(scale_factor):
    while True:
        try:
            if locate_image_on_screen("terminated.png", scale_factor) is not None:
                pause_event.wait()
                logging.info("Game Crashed/Terminated")
                no_button = locate_image_on_screen("no.png", scale_factor)
                if no_button is not None:
                    logging.info("Clicking No Button")
                    pyautogui.click(no_button.left, no_button.top)
        except ImageNotFound:
            pass

        try:
            if locate_image_on_screen("launcher.png", scale_factor, confidence=0.5) is not None:
                pause_event.wait()

                logging.info('Game Crashed or launching')
                yes = locate_image_on_screen("yes.png", scale_factor)
                if yes is not None:
                    time.sleep(1)
                    pyautogui.click(yes)

                play = locate_image_on_screen("play.png", scale_factor, confidence=0.8)
                if play is not None:
                    time.sleep(2)
                    pyautogui.click(play)

                time.sleep(20)
        except ImageNotFound:
            pass

        try:
            if pyautogui.locateOnScreen('images/game.png', grayscale=True, confidence=0.95) is not None:
                pause_event.wait()
                game = pyautogui.locateOnScreen('images/game.png')
                if game is not None:
                    pyautogui.click(game)
                    logging.info("Launching game")
                    time.sleep(1)
        except ImageNotFound:
            pass
        
        try:
            if pyautogui.locateOnScreen('images/exit.png', grayscale=True, confidence=0.7) is not None:
                pause_event.wait()
                time.sleep(0.5)
                no2_button = pyautogui.locateOnScreen('images/no2.png', confidence=0.8)
                if no2_button is not None:
                    pyautogui.click(no2_button)
                    logging.info("False exit, returning to main menu")
        except ImageNotFound:
            pass

        try:
            eft_menu = locate_image_on_screen("eftmenu.png", scale_factor, confidence=0.7)
            if eft_menu is not None:
                pause_event.wait()
                pydirectinput.click(eft_menu.left, eft_menu.top)
                logging.info("In main menu")
                time.sleep(0.5)
        except ImageNotFound:
            pass
                        
        try:
            pmc_menu = pyautogui.locateOnScreen('images/pmc.png', confidence=0.7)
            if pmc_menu is not None:
                pause_event.wait()
                pydirectinput.click(pmc_menu.left + 20, pmc_menu.top + 20)
                time.sleep(0.5)
                next_button = pyautogui.locateOnScreen('images/next.png', confidence=0.7)
                if next_button is not None:
                    pydirectinput.click(next_button.left + 20, next_button.top + 20)
                    time.sleep(0.5)
                    logging.info("Entering map selection")
        except ImageNotFound:
            pass

        try:
            if pyautogui.locateOnScreen('images/reconnecting.png', grayscale=True, confidence=0.7) is not None:
                pause_event.wait()
                logging.info("Connection lost")
                time.sleep(0.2)
                reconnecting_button = pyautogui.locateOnScreen('images/reconnecting.png', confidence=0.7)
                if reconnecting_button is not None:
                    pydirectinput.click(reconnecting_button.left, reconnecting_button.top)
        except ImageNotFound:
            pass

        try:
            if pyautogui.locateOnScreen('images/matching.png', grayscale=True, confidence=0.7) is not None:
                pause_event.wait()
                if not stopwatch.running:
                    logging.info("Matching and starting countdown.")
                    stopwatch.start()

                if stopwatch.duration >= 240:
                    logging.info("Matching time exceded 4 minutes 30 seconds. Exiting matching and requeuing.")
                    back_button = pyautogui.locateOnScreen('images/back.png', grayscale=True, confidence=0.7)
                    if back_button is not None:
                        stopwatch.stop()
                        stopwatch.reset()
                        pyautogui.click(back_button.left, back_button.top)
        except ImageNotFound:
            pass
    
        try:
            if pyautogui.locateOnScreen('images/deploy_wait.png', grayscale=True, confidence=0.6) is not None:
                pause_event.wait()
                global raid_counter
                logging.info("Deploying")
                stopwatch.stop()
                stopwatch.reset()
                raid_counter += 1
                logging.info(f"Raid Counter: {raid_counter}")
                time.sleep(10)
        except ImageNotFound:
            pass

        try:
            if pyautogui.locateOnScreen('images/lowstam.png', grayscale=True, confidence=0.9) is not None:
                pause_event.wait()
                logging.info("Stamina low, waiting to recover")
                time.sleep(20)
        except ImageNotFound:
            pass

        try:
            if pyautogui.locateOnScreen('images/bush.png', grayscale=True, confidence=0.9) is not None:
                pause_event.wait()
                logging.info("Bush detected, attempting to move away")
                pydirectinput.keyDown('w')
                time.sleep(3)
                pydirectinput.keyUp('w')
        except ImageNotFound:
            pass
        
        try:
            if pyautogui.locateOnScreen('images/ingame.png', grayscale=True, confidence=0.45) is not None:
                pause_event.wait()
                logging.info("In Game")
                pydirectinput.moveTo(5, 540)
                pydirectinput.keyDown('w')
                time.sleep(0.2)
                pydirectinput.keyDown('shift')
                time.sleep(10)
                pydirectinput.keyUp('shift')
                pydirectinput.keyUp('w')
                time.sleep(1)
                pydirectinput.moveTo(965, 540)
                time.sleep(1.3)
                pydirectinput.keyDown('w')
                time.sleep(0.2)
                pydirectinput.keyDown('shift')
                time.sleep(10)
                pydirectinput.keyUp('shift')
                pydirectinput.keyUp('w')
                time.sleep(1.3)
        except ImageNotFound:
            pass


def _wait_deploy():
    while True:
        try:
            pause_event.wait()
            if pyautogui.locateOnScreen('images/deploying.png', grayscale=True, confidence=0.7) is not None:
                logging.info("Deploying soon")
                time.sleep(300)
                pydirectinput.click(956, 1015)
        except ImageNotFound:
            pass


threads = set()
pause_event = threading.Event()
pause_event.set()


def toggle_pause():
    if pause_event.is_set():
        logging.info("Pausing bot.")
        pause_event.clear()
    else:
        logging.info("Resuming bot.")
        pause_event.set()


def run(scale_factor=1):
    restart_game_thread = threading.Thread(target=_restart_game, name="RestartGameThread")
    game_thread = threading.Thread(target=game, name="GameThread", args=[scale_factor])
    wait_deploy_thread = threading.Thread(target=_wait_deploy, name="WaitDeployThread")

    threads.add(restart_game_thread)
    threads.add(game_thread)
    threads.add(wait_deploy_thread)

    for thread in threads:
        thread.start()

    keyboard.on_press_key("q", lambda x: toggle_pause())

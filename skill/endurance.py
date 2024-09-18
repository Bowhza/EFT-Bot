import pyautogui
import pydirectinput

import threading
import logging
import time
import keyboard
from stopwatch import Stopwatch
# Stopwatch with 2 decimal place accuracy
stopwatch = Stopwatch(2)
stopwatch.stop()

# Raid Counter
raid_counter = 0

log = logging.getLogger(__name__)

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
        
def game():
    while True:
        if pyautogui.locateOnScreen('images/terminated.png', grayscale=True, confidence=0.7) is not None:
            pause_event.wait()
            logging.info("Game Crashed/Terminated")
            no_button = pyautogui.locateOnScreen('images/no.png', grayscale=True, confidence=0.7)
            if no_button is not None:
                logging.info("Clicking No Button")
                pyautogui.click(no_button.left, no_button.top)

        elif pyautogui.locateOnScreen('images/launcher.png', grayscale=True, confidence=0.5) != None:
            pause_event.wait()

            logging.info('Game Crashed or launching')
            yes = pyautogui.locateOnScreen('images/usererroryes.png')
            if yes is not None:
                time.sleep(1)
                pyautogui.click(yes)
            
            play = pyautogui.locateOnScreen('images/play.png', confidence=0.8)
            if play is not None:
                time.sleep(2)
                pyautogui.click(play)
            
            time.sleep(20)

        elif pyautogui.locateOnScreen('images/game.png', grayscale=True, confidence=0.95) != None:
            pause_event.wait()
            game = pyautogui.locateOnScreen('images/game.png')
            if game is not None:
                pyautogui.click(game)
                logging.info("Launching game")
                time.sleep(1)
        
        elif pyautogui.locateOnScreen('images/exit.png', grayscale=True, confidence=0.7) != None:
            pause_event.wait()
            time.sleep(0.5)
            no2_button = pyautogui.locateOnScreen('images/no2.png', confidence=0.8)
            if no2_button is not None:
                pyautogui.click(no2_button)
                logging.info("False exit, returning to main menu")

        eft_menu = pyautogui.locateOnScreen('images/eftmenu.png', grayscale=True, confidence=0.7)
        if eft_menu is not None:
            pause_event.wait()
            pydirectinput.click(eft_menu.left, eft_menu.top)
            logging.info("In main menu")
            time.sleep(0.5)
                        
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


        # elif pyautogui.locateOnScreen('images/leaving.png', grayscale=True, confidence=0.8) != None:
        #     pause_event.wait()
        #     logging.info("leaving match time limit was exceeded")
        #     time.sleep(5)

        # elif pyautogui.locateOnScreen('images/ac-connectionlost.png', grayscale=True, confidence=0.7) != None:
        #     pause_event.wait()
        #     logging.info("anti cheat connection lost game must restart")
        #     pydirectinput.click(962, 580)
        #     time.sleep(0.5)
    
        # elif pyautogui.locateOnScreen('images/connectionlost.png', grayscale=True, confidence=0.7) != None:
        #     logging.info("Connection lost")
        #     pydirectinput.click(962, 580)
        #     time.sleep(0.5)

        elif pyautogui.locateOnScreen('images/reconnecting.png', grayscale=True, confidence=0.7) != None:
            pause_event.wait()
            logging.info("Connection lost")
            time.sleep(0.2)
            reconnecting_button = pyautogui.locateOnScreen('images/reconnecting.png', confidence=0.7)
            if reconnecting_button is not None:
                pydirectinput.click(reconnecting_button.left, reconnecting_button.top)

        # elif pyautogui.locateOnScreen('images/warningconect.png', grayscale=True, confidence=0.7) != None:
        #     pause_event.wait()
        #     logging.info("Connection lost, attempting to reconnect")
        #     time.sleep(1)
        #     pydirectinput.click(958, 901)

        elif pyautogui.locateOnScreen('images/matching.png', grayscale=True, confidence=0.7) != None:
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
    
        elif pyautogui.locateOnScreen('images/deploy_wait.png', grayscale=True, confidence=0.6) != None:
            pause_event.wait()
            global raid_counter
            logging.info("Deploying")
            stopwatch.stop()
            stopwatch.reset()
            raid_counter += 1
            logging.info(f"Raid Counter: {raid_counter}")
            time.sleep(10)

        elif pyautogui.locateOnScreen('images/lowstam.png', grayscale=True, confidence=0.9) != None:
            pause_event.wait()
            logging.info("Stamina low, waiting to recover")
            #prevent any bot
            time.sleep(20)

        # elif pyautogui.locateOnScreen('images/failedtofindraid.png', grayscale=True, confidence=0.8) != None:
        #     pause_event.wait()
        #     logging.info("error failed to find raid, trying again")
        #     time.sleep(1)
        #     pydirectinput.click(958, 567)

        elif pyautogui.locateOnScreen('images/bush.png', grayscale=True, confidence=0.9) != None:
            pause_event.wait()
            logging.info("Bush detected, attempting to move away")
            #run avoid bush
            pydirectinput.keyDown('w')
            time.sleep(3)
            pydirectinput.keyUp('w')
        
        elif pyautogui.locateOnScreen('images/ingame.png', grayscale=True, confidence=0.45) != None:
            pause_event.wait()
            #run afk bot
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

def _wait_deploy():
    while True:
        pause_event.wait()
        if pyautogui.locateOnScreen('images/deploying.png', grayscale=True, confidence=0.7) != None:
            logging.info("Deploying soon")
            time.sleep(300)
            pydirectinput.click(956, 1015)

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

def run():        
    restart_game_thread = threading.Thread(target=_restart_game, name="RestartGameThread")
    heal_thread = threading.Thread(target=game, name="HealThread")
    wait_deploy_thread = threading.Thread(target=_wait_deploy, name="WaitDeployThread")

    threads.add(restart_game_thread)
    threads.add(heal_thread) 
    threads.add(wait_deploy_thread)

    for thread in threads:
        thread.start()

    keyboard.on_press_key("q", lambda x: toggle_pause())
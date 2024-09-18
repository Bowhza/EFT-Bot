import pyautogui
import pydirectinput

import threading
import logging
import time

log = logging.getLogger(__name__)

def _restart_game():
    while True:

        time.sleep(21600)
        logging.info('Restarting game')

        pydirectinput.keyUp('shift')
        pydirectinput.keyUp('w')
        pydirectinput.keyDown('alt')
        pydirectinput.keyDown('f4')
        pydirectinput.keyUp('alt')
        pydirectinput.keyUp('f4')
        
def game():
    while True:

        if pyautogui.locateOnScreen('images/launcher.png', grayscale=True, confidence=0.8) != None:
            logging.info('Game Crashed or launching')
            yes = pyautogui.locateOnScreen('images/usererroryes.png')
            time.sleep(1)
            pyautogui.click(yes)
            time.sleep(3)
            location = pyautogui.locateOnScreen('images/play.png')
            time.sleep(2)
            pyautogui.click(location)
            time.sleep(20)

        elif pyautogui.locateOnScreen('images/game.png', grayscale=True, confidence=0.95) != None:
            game = pyautogui.locateOnScreen('images/game.png')
            logging.info("Launching game")
            time.sleep(1)
            pyautogui.click(game)
        
        elif pyautogui.locateOnScreen('images/exit.png', grayscale=True, confidence=0.7) != None:
            pydirectinput.click(1056, 574)
            logging.info("False exit, returning to main menu")
            time.sleep(0.5)

        elif pyautogui.locateOnScreen('images/eftmenu.png', grayscale=True, confidence=0.7) != None:
            pydirectinput.click(971, 646)
            logging.info("In main menu")
            time.sleep(0.5)
            
        elif pyautogui.locateOnScreen('images/eftmenuhighlight.png', grayscale=True, confidence=0.7) != None:
            pydirectinput.click(971, 646)
            logging.info("In main menu")
            time.sleep(0.5)            

        elif pyautogui.locateOnScreen('images/pmc.png', grayscale=False, confidence=0.7) != None:
            pydirectinput.click(1202, 694)
            logging.info("Entering map selection")
            time.sleep(0.5)
            pydirectinput.click(958, 946)
            time.sleep(0.5)

        elif pyautogui.locateOnScreen('images/pmc2.png', grayscale=False, confidence=0.7) != None:
            pydirectinput.click(1202, 694)
            logging.info("Entering map selection")
            time.sleep(0.5)
            pydirectinput.click(958, 946)
            time.sleep(0.5)

        elif pyautogui.locateOnScreen('images/leaving.png', grayscale=True, confidence=0.8) != None:
            logging.info("leaving match time limit was exceeded")
            time.sleep(5)

        elif pyautogui.locateOnScreen('images/ac-connectionlost.png', grayscale=True, confidence=0.7) != None:
            logging.info("anti cheat connection lost game must restart")
            pydirectinput.click(962, 580)
            time.sleep(0.5)
    
        elif pyautogui.locateOnScreen('images/connectionlost.png', grayscale=True, confidence=0.7) != None:
            logging.info("Connection lost")
            pydirectinput.click(962, 580)
            time.sleep(0.5)

        elif pyautogui.locateOnScreen('images/reconnecting.png', grayscale=True, confidence=0.7) != None:
            logging.info("Connection lost")
            time.sleep(0.2)
            pydirectinput.click(947, 643)

        elif pyautogui.locateOnScreen('images/warningconect.png', grayscale=True, confidence=0.7) != None:
            logging.info("Connection lost, attempting to reconnect")
            time.sleep(1)
            pydirectinput.click(958, 901)
    
        elif pyautogui.locateOnScreen('images/deploy_wait.png', grayscale=True, confidence=0.6) != None:
            logging.info("Deploying soon")
            time.sleep(0.5)

        elif pyautogui.locateOnScreen('images/lowstam.png', grayscale=True, confidence=0.9) != None:
            logging.info("Stamina low waiting to recover")
            #prevent any bot
            time.sleep(20)

        elif pyautogui.locateOnScreen('images/failedtofindraid.png', grayscale=True, confidence=0.8) != None:
            logging.info("error failed to find raid, trying again")
            time.sleep(1)
            pydirectinput.click(958, 567)



def _wait_deploy():
    while True:

        if pyautogui.locateOnScreen('images/deploying.png', grayscale=True, confidence=0.7) != None:
            logging.info("Deploying")
            time.sleep(300)
            pydirectinput.click(956, 1015)


def run():        
    restart_game_thread = threading.Thread(target=_restart_game)
    restart_game_thread.start()

    heal_thread = threading.Thread(target=game)
    heal_thread.start()

    wait_deploy_thread = threading.Thread(target=_wait_deploy)
    wait_deploy_thread.start()
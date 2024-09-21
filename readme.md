> [!Caution]
>
> This bot was made by another person and was abandoned, this repository aims to fix and update the script to run on newer versions of the game. If you encounter any bugs or bad code please create an issue/pull request with changes.

# EFT Skill & Death bot

This a bot for leveling up your endurance, strength, and covert (Still work in progress).
It also inherently is a KD dropper.
It uses image recognitiion to detect images and make clicks for you.
It will run around in-game for you like the little bot you are, enjoy.

> [!Important]
> Works with Python 3.10+
>
> When installing Python you **_MUST_** add it to **_PATH_** via the python installer options.

## Prerequisites

1. Battlestate Games Launcher must be set to keep Launcher window open.

<img src="https://i.imgur.com/bodWnnU.png"/>

2. The in-game setting for **_Quick Slots_** under the game tab must be set to **_Always Shown_**.

<img src="https://i.imgur.com/u4LcCv3.png"/>

_If the you are highlighting items in Visual Studio after stopping the script hit shift and it will stop_.

## How to run the script

1. Run the included `Install-Dependencies.bat` file to install the required dependecies.

2. If your monitor is **NOT 1440p**, run the `image_scale.py` script in the `/tools` direcory to scale the images to your screen resolution.

3. After you have installed all the dependencies, run the file called `script_run.py` to start the bot.

4. Select the settings you want and let the script do its thing.

> Note: **Pressing `Q` toggles pause on the script.**

@ECHO OFF

:: Display the python version
python -V

:: Create a virtual environment
python -m venv .venv

:: Activate the virtual environment
call .venv/Scripts/activate

:: Install the dependencies from the requirements.txt
pip install -r requirements.txt

:: Setup is complete
ECHO You're all setup, enjoy.
PAUSE

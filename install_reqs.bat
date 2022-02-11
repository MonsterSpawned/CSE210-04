@echo off
python3 -m pip install virtualenv
python3 -m virtualenv venv
call %CD%\venv\Scripts\activate.bat
pip install -r requirements.txt
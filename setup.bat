@echo off
pip install virtualenv
virtualenv myvenv
cmd /k "myvenv\Scripts\activate & pip install -r requirements.txt & exit"
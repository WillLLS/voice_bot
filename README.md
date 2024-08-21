# Installation:

### Create a new environment
`python -m venv .venv`  
<br>
Linux   `source .venv/bin/activate`  
Windows `.venv\Scripts\activate.bat`

### Install the dependencies
`pip install -r requirements.txt`

### Setup the working directory
`python setup.py`  

This will create the config file (`config.py`) and fill it with you Telegram API Token's Bot.  
This will also create create the Databse and adding a number (your choice) of Fake users to fill it.

### Run the bot
`python main.py`

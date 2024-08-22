from db import db_creation
import os
# Fill the table with fake profiles
from uuid import uuid4
from random import randint
from tqdm import tqdm 

def is_int_convertible(string):
    try:
        int(string)
        return True
    except:
        return False

if __name__ == "__main__":
    
    if not os.path.exists("config.py"):
        
        print("Please enter your Bot Token. You can get it from the BotFather on Telegram and modify it int the config.py file later.")
        res = input("Bot Token: ")
        
        with open("config.py", "w") as f:
            f.write(f"API_TOKEN = '{res}'")
            
    
    res = input("Please enter the number of fake profiles you want to add in the database: ")
    
    if not is_int_convertible(res):
        print("Please restart using a number.")
        exit()    
    
    for i in tqdm(range(int(res))):
        vocal_count = randint(0, 120)
        db_creation.cur.execute(f"INSERT INTO customers VALUES ('{str(uuid4())[:8]}', 'Fake', 'fake', {vocal_count*5}, {vocal_count}, 0, 0, '{str(uuid4())[:8]}')")
    
    
    
    
       
    db_creation.con.commit()
    db_creation.cur.close()
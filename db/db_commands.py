

from dataclasses import dataclass
from typing import Union


import sqlite3
import os

from uuid import uuid4

def get_db_path():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, 'db', 'database.db')

@dataclass
class customer_t():
    tm_id: str          = ""
    first_name: str     = ""
    username: str       = ""
    balance: int        = 0
    total_vocal: int    = 0
    daily_vocal: int    = 0
    lt: int             = 0
    referal_id: str     = ""
    
    def __iter__(self):
        return iter((self.tm_id, self.first_name, self.username, self.balance, self.total_vocal, self.daily_vocal, self.lt, self.referal_id))

@dataclass
class global_t():
    users: int = 0
    balance: int = 0
    vocaux: int = 0
    
    def __iter__(self):
        return iter((self.users, self.balance, self.vocaux))


class Customer():
    
    def __init__(self) -> None:
        pass
    
    def get(tm_id) -> customer_t:
        con = sqlite3.connect(get_db_path())
        cur = con.cursor()
        query = "SELECT * FROM customers WHERE tm_id = ?"
        cur.execute(query, (tm_id,))
        result = cur.fetchone()
        con.close()
        
        if result:
            return customer_t(*result)
        else:
            return None
    
    def add(info : Union[customer_t, list]) -> None:
        con = sqlite3.connect(get_db_path())
        cur = con.cursor()
        
        if isinstance(info, customer_t):
            info.referal_id = str(uuid4())[:8]
            info = [*info]
            
        elif isinstance(info, list):
            info = info + [str(uuid4())[:8]]         
        
        try:
            query = "INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            cur.execute(query, info)
            con.commit()
            con.close()
            return True
        except Exception as e:
            print(e)
            con.close()
            return False

    def set_daily_vocal(tm_id :str, daily_vocal: int):
        
        try:
            con = sqlite3.connect(get_db_path())
            cur = con.cursor()
            query = "UPDATE customers SET daily_vocal=? WHERE tm_id=?"
            cur.execute(query, (daily_vocal, tm_id,))
            con.commit()
            con.close()
            return True
        except Exception as e:
            print(e)
            return False
        
    def set_total_vocal(tm_id :str, total_vocal: int):
        
        try:
            con = sqlite3.connect(get_db_path())
            cur = con.cursor()
            query = "UPDATE customers SET total_vocal = ? WHERE tm_id = ?"
            cur.execute(query, (total_vocal, tm_id,))
            con.commit()
            con.close()
            return True
        except Exception as e:
            print(e)
            return False
    
    def get_balance(tm_id) -> int:
        con = sqlite3.connect(get_db_path())
        cur = con.cursor()
        query = "SELECT balance FROM customers WHERE tm_id = ?"
        cur.execute(query, (tm_id,))
        result = cur.fetchone()
        con.close()
        
        if result:
            return result[0]
        else:
            return
    
    def set_balance(tm_id :str, balance: int):
        print("[+] Setting balance")

        try:
            con = sqlite3.connect(get_db_path())
            cur = con.cursor()
            query = "UPDATE customers SET balance = ? WHERE tm_id = ?"
            cur.execute(query, (balance, tm_id,))
            con.commit()
            con.close()
            return True
        except Exception as e:
            print(e)
            return False
        
    def set_referals(tm_id :str, referals: int):
        try:
            con = sqlite3.connect(get_db_path())
            cur = con.cursor()
            query = "UPDATE customers SET referals = ? WHERE tm_id = ?"
            cur.execute(query, (referals, tm_id,))
            con.commit()
            con.close()
            return True
        except Exception as e:
            print(e)
            return False
    
    def get_referals(tm_id) -> int:
        con = sqlite3.connect(get_db_path())
        cur = con.cursor()
        query = "SELECT referals FROM customers WHERE tm_id = ?"
        cur.execute(query, (tm_id,))
        result = cur.fetchone()
        con.close()
        
        if result:
            return result[0]
        else:
            return
        

    def get_id_from_referal(referal_id) -> str:
        con = sqlite3.connect(get_db_path())
        cur = con.cursor()
        query = "SELECT tm_id FROM customers WHERE referal_id = ?"
        cur.execute(query, (referal_id,))
        result = cur.fetchone()
        con.close()
        
        if result:
            return result[0]
        else:
            return
        
    def add_balance_referral(tm_id :str, balance: int):
        try:
            con = sqlite3.connect(get_db_path())
            cur = con.cursor()
            query = "UPDATE customers SET balance = balance + ? WHERE tm_id = ?"
            cur.execute(query, (balance, tm_id,))
            con.commit()
            con.close()
            return True
        except Exception as e:
            print(e)
            return False
        
    def get_balance_from_referal(referal_id) -> int:
        con = sqlite3.connect(get_db_path())
        cur = con.cursor()
        query = "SELECT SUM(balance) FROM customers WHERE referal_id = ?"
        cur.execute(query, (referal_id,))
        result = cur.fetchone()
        con.close()
        
        if result:
            return result[0]
        else:
            return
    
    
    
    def set_lt(tm_id :str, lt: int):
            
        try:
            con = sqlite3.connect(get_db_path())
            cur = con.cursor()
            query = "UPDATE customers SET lt = ? WHERE tm_id = ?"
            cur.execute(query, (lt, tm_id,))
            con.commit()
            con.close()
            return True
        
        except Exception as e:
            print(e)
            return False
    
    def is_customer(tm_id) -> bool:
        con = sqlite3.connect(get_db_path())
        cur = con.cursor()
        query = "SELECT * FROM customers WHERE tm_id = ?"
        cur.execute(query, (tm_id,))
        result = cur.fetchone()
        con.close()
        
        if result:
            return True
        else:
            return False
    
    def get_position(tm_id) -> int:
        con = sqlite3.connect(get_db_path())
        cur = con.cursor()
        query = "SELECT COUNT(*) FROM customers WHERE balance > (SELECT balance FROM customers WHERE tm_id = ?)"
        cur.execute(query, (tm_id,))
        result = cur.fetchone()
        con.close()
        
        if result:
            return result[0] + 1
        else:
            return
        
    
    def get_from_position(position) -> customer_t:
        con = sqlite3.connect(get_db_path())
        cur = con.cursor()
        query = "SELECT * FROM customers ORDER BY balance DESC LIMIT 1 OFFSET ?"
        cur.execute(query, (position - 1,))
        result = cur.fetchone()
        con.close()
        
        if result:
            return customer_t(*result)
        else:
            return
    
    def get_total_user() -> int:
        con = sqlite3.connect(get_db_path())
        cur = con.cursor()
        query = "SELECT COUNT(*) FROM customers"
        cur.execute(query)
        result = cur.fetchone()
        con.close()
        
        if result:
            return result[0]
        else:
            return
        
    def get_total_balance() -> int:
        con = sqlite3.connect(get_db_path())
        cur = con.cursor()
        query = "SELECT SUM(balance) FROM customers"
        cur.execute(query)
        result = cur.fetchone()
        con.close()
        
        if result:
            return result[0]
        else:
            return
        
    def get_total_vocal_sent() -> int:
        con = sqlite3.connect(get_db_path())
        cur = con.cursor()
        query = "SELECT SUM(total_vocal) FROM customers"
        cur.execute(query)
        result = cur.fetchone()
        con.close()
        
        if result:
            return result[0]
        else:
            return

    def get_global() -> global_t:
        return global_t(Customer.get_total_user(), Customer.get_total_balance(), Customer.get_total_vocal_sent())
    
class Referals():
        
        def __init__(self) -> None:
            pass
        
        def get_all() -> list:
            con = sqlite3.connect(get_db_path())
            cur = con.cursor()
            query = "SELECT * FROM referals"
            cur.execute(query)
            result = cur.fetchall()
            con.close()
            
            if result:
                return result
            else:
                return []
            
        def add(referal_id, tm_id) -> None:
            con = sqlite3.connect(get_db_path())
            cur = con.cursor()
            query = "INSERT INTO referals VALUES (?, ?)"
            cur.execute(query, (referal_id, tm_id))
            con.commit()
            con.close()
        
        def count_referals(referal_id) -> int:
            con = sqlite3.connect(get_db_path())
            cur = con.cursor()
            query = "SELECT COUNT(*) FROM referals WHERE referal_id = ?"
            cur.execute(query, (referal_id,))
            result = cur.fetchone()
            con.close()
            
            if result:
                return result[0]
            else:
                return 0
         
        def get_referent(tm_id) -> str:
            con = sqlite3.connect(get_db_path())
            cur = con.cursor()
            query = "SELECT referal_id FROM customers WHERE tm_id = ?"
            cur.execute(query, (tm_id,))
            result = cur.fetchone()
            con.close()
            
            if result:
                return result[0]
            else:
                return None
            
        def get_referals(referal_id) -> list:
            con = sqlite3.connect(get_db_path())
            cur = con.cursor()
            query = "SELECT * FROM referals WHERE referal_id = ?"
            cur.execute(query, (referal_id,))
            result = cur.fetchall()
            con.close()
            
            if result:
                return result
            else:
                return []
        
        
if __name__ == "__main__":
    Customer.add(customer_t("123456", "John Doe", "johndoe", 100, 10, 5, 0, 0))
    print(Customer.get("123456"))
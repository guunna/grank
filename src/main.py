import sys
from os.path import dirname
from utils.logger import initialize_logger
from utils.configuration.verify_configuration import verify_configuration
from utils.configuration.verify_credentials import verify_credentials
from scripts.beg import beg
from scripts.dig import dig
from scripts.fish import fish
from scripts.hunt import hunt
from scripts.search import search
from scripts.highlow import highlow
from time import sleep
from utils.logger import register

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
    
    register(log, "DEBUG", "Beginning cooldown between command loop.")
    sleep(39 - (config["cooldowns"]["commands"] * 5))
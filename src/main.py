import sys
from os.path import dirname
from utils.logger import initialize_logger
from utils.configuration.verify_configuration import verify_configuration
from utils.configuration.verify_credentials import verify_credentials
from scripts.basic.beg import beg
from scripts.basic.dig import dig
from scripts.basic.fish import fish
from scripts.basic.hunt import hunt
from time import sleep
from utils.logger import register

if getattr(sys, "frozen", False):
    cwd = dirname(sys.executable)
elif __file__:
    cwd = dirname(__file__)
    
log = initialize_logger(cwd)
   
config = verify_configuration(log, cwd)
credentials = verify_credentials(log, cwd)

commands = config["commands"]
cooldowns = config["cooldowns"]

token = credentials["token"]
channel_id = credentials["channel_id"]

commands_cooldown = cooldowns["commands"]
loop_cooldown = cooldowns["loop"]

while True:
    print("\n")
    if commands["beg"]:
        beg(log, token, channel_id)
        sleep(commands_cooldown)
        
    if commands["dig"]:
        dig(log, token, channel_id)
        sleep(commands_cooldown)
        
    if commands["fish"]:
        fish(log, token, channel_id)
        sleep(commands_cooldown)
        
    if commands["hunt"]:
        hunt(log, token, channel_id)
        sleep(commands_cooldown)
    
    register(log, "DEBUG", f"Beginning {loop_cooldown} second cooldown between command loop.")
    sleep(loop_cooldown)
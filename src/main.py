import sys
from os.path import dirname
from yaml import safe_load
from utils.logger import initialize_logger, register
from utils.console import style
from json import load
from scripts.beg import beg
from scripts.dig import dig
from scripts.fish import fish
from scripts.hunt import hunt
from time import sleep

if getattr(sys, "frozen", False):
    cwd = dirname(sys.executable)
elif __file__:
    cwd = dirname(__file__)
    
log = initialize_logger(cwd)

try:
    config = safe_load(open(f"{cwd}/config.yml", "r"))
    register(log, "DEBUG", "Found `config.yml` and parsed values from it.")
except FileNotFoundError:
    register(log, "ERROR", "Unable to find `config.yml`. Make sure the file is present.")
    _ = input(f"\n{style.Italic and style.Faint}Press ENTER to exit the program...{style.RESET_ALL}")
    exit(1)
    
try:
    credentials = load(open(f"{cwd}/credentials.json", "r"))
    register(log, "DEBUG", "Found `credentials.json` and parsed values from it.")
except FileNotFoundError:
    register(log, "ERROR", "Unable to find `credentials.json`. Make sure the file is present.")
    _ = input(f"\n{style.Italic and style.Faint}Press ENTER to exit the program...{style.RESET_ALL}")
    exit(1)

if "token" not in credentials.keys():
    register(log, "ERROR", "Unable to find value `token` in `credentials.json`. Make sure the value is present.")
    _ = input(f"\n{style.Italic and style.Faint}Press ENTER to exit the program...{style.RESET_ALL}")
    exit(1)
else:
    register(log, "DEBUG", "Verified presence of value `token` in `credentials.json`.")
    
if "channel_id" not in credentials.keys():
    register(log, "ERROR", "Unable to find value `channel_id` in `credentials.json`. Make sure the value is present.")
    _ = input(f"\n{style.Italic and style.Faint}Press ENTER to exit the program...{style.RESET_ALL}")
    exit(1)
else:
    register(log, "DEBUG", "Verified presence of value `channel_id` in `credentials.json`.\n")
    
commands = config["commands"]
cooldowns = config["cooldowns"]

token = credentials["token"]
channel_id = credentials["channel_id"]

commands_cooldown = cooldowns["commands"]
loop_cooldown = cooldowns["loop"]

while True:
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
        
    sleep(loop_cooldown)
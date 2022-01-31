from requests import post
from utils.logger import register
from time import sleep
from requests import get
from json import loads

def dig(log, token, channel_id, logging, timeout, ID, commands, cwd):
    request = post(f"https://discord.com/api/v8/channels/{channel_id}/messages", headers={"authorization": token}, data={"content": "pls dig"})
    
    if request.status_code != 200:
        if logging["warning"]:
            register(log, "WARNING", f"Failed to send command `pls dig`. Status code: {request.status_code} (expected 200).")
        return
    
    if logging["debug"]:
        register(log, "DEBUG", "Successfully sent command `pls dig`.")
        
    latest_message = None
    
    for _ in range(0, timeout):
        sleep(1)
        
        request = get(f"https://discord.com/api/v8/channels/{channel_id}/messages", headers={"authorization": token})
        
        if request.status_code != 200:
            continue

        latest_message = loads(request.text)[0]
        
        if latest_message["author"]["id"] == "270904126974590976" and latest_message["referenced_message"]["author"]["id"] == ID:
            if logging["debug"]:
                register(log, "DEBUG", "Got Dank Memer's response to command `pls dig`.")
            break
        else:
            continue
       
    if latest_message is None or latest_message["author"]["id"] != "270904126974590976":
        if logging["warning"]:
            register(log, "WARNING", f"Timeout exceeded for response from Dank Memer ({timeout} second(s)). Aborting command.")
        return
    elif latest_message["content"].lower() == "you don't have a shovel, you need to go buy one. i'd hate to let you dig with your bare hands.":
        if logging["debug"]:
            register(log, "DEBUG", "User does not have item `shovel`. Buying shovel now.")
        
        if commands["auto_buy"]:
            from scripts.buy import buy
            buy(log, token, channel_id, timeout, logging, "shovel", cwd, ID)
            return
        elif logging["warning"]:
            register(log, "WARNING", "A shovel is required for the command `pls dig`. However, since `auto_buy` is set to false in the configuration file, the program will not buy one. Aborting command.")
            return
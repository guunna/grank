from requests import post
from utils.logger import register
from time import sleep
from requests import get
from json import loads

def hunt(log, token, channel_id, logging, timeout, ID, commands, cwd):
    request = post(f"https://discord.com/api/v8/channels/{channel_id}/messages", headers={"authorization": token}, data={"content": "pls hunt"})
    
    if request.status_code != 200:
        if logging["warning"]:
            register(log, "WARNING", f"Failed to send command `pls hunt`. Status code: {request.status_code} (expected 200).")
        return
    
    if logging["debug"]:
        register(log, "DEBUG", "Successfully sent command `pls hunt`.")
        
    latest_message = None
    
    sleep(2)
    
    for _ in range(0, timeout):
        sleep(1)
        
        request = get(f"https://discord.com/api/v8/channels/{channel_id}/messages", headers={"authorization": token})
        
        if request.status_code != 200:
            continue

        latest_message = loads(request.text)[0]
        
        if latest_message["author"]["id"] == "270904126974590976" and latest_message["referenced_message"]["author"]["id"] == ID:
            if logging["debug"]:
                register(log, "DEBUG", "Got Dank Memer's response to command `pls hunt`.")
            break
        else:
            continue
       
    if latest_message is None or latest_message["author"]["id"] != "270904126974590976":
        if logging["warning"]:
            register(log, "WARNING", f"Timeout exceeded for response from Dank Memer ({timeout} second(s)). Aborting command.")
        return
    elif latest_message["content"].lower() == "you don't have a hunting rifle, you need to go buy one. you're not good enough to shoot animals with your bare hands... i hope":
        if logging["debug"]:
            register(log, "DEBUG", "User does not have item `hunting rifle`. Buying hunting rifle now.")
        
        if commands["auto_buy"]:
            from scripts.buy import buy
            buy(log, token, channel_id, timeout, logging, "hunting", cwd, ID)
            return
        elif logging["warning"]:
            register(log, "WARNING", "A hunting rifle is required for the command `pls hunt`. However, since `auto_buy` is set to false in the configuration file, the program will not buy one. Aborting command.")
            return
from requests import post, get
from utils.logger import register
from time import sleep
from json import loads
from random import choice

def balance(log, token, channel_id, timeout, logging):
    request = post(f"https://discord.com/api/v8/channels/{channel_id}/messages", headers={"authorization": token}, data={"content": "pls bal"})
    
    if request.status_code != 200 and logging["warning"]:
        register(log, "WARNING", f"Failed to send command `pls bal`. Status code: {request.status_code} (expected 200). Aborting command.")
        return
    
    if logging["debug"]:
        register(log, "DEBUG", "Successfully sent command `pls bal`.")
    
    latest_message = None
    
    sleep(2)
    
    for _ in range(0, timeout):
        sleep(1)
        
        request = get(f"https://discord.com/api/v8/channels/{channel_id}/messages", headers={"authorization": token})
        
        if request.status_code != 200:
            continue

        latest_message = loads(request.text)[0]
        
        if latest_message["author"]["id"] == "270904126974590976" and logging["debug"]:
            register(log, "DEBUG", "Got Dank Memer's response to command `pls bal`.")
            break
        else:
            continue
       
    if (latest_message is None or latest_message["author"]["id"] != "270904126974590976") and logging["warning"]:
        register(log, "WARNING", f"Timeout exceeded for response from Dank Memer ({timeout} second(s)). Aborting command.")
        return
        
    return [True, latest_message]
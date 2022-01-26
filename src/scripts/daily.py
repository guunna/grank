from json import load
from requests import post
from utils.logger import register
from datetime import datetime

def daily(log, token, channel_id, logging, cwd):
    data = load(f"{cwd}/data.json") 
    
    if data["daily"] == "None":
        request = post(f"https://discord.com/api/v8/channels/{channel_id}/messages", headers={"authorization": token}, data={"content": "pls daily"})
    
        if request.status_code != 200 and logging["warning"]:
            register(log, "WARNING", f"Failed to send command `pls daily`. Status code: {request.status_code} (expected 200).")
            return
        
        if logging["debug"]:
            register(log, "DEBUG", "Successfully sent command `pls daily`.")
        
        data["daily"] == datetime.now().strftime("%x-%X")
           
        open(f"{cwd}/data.json", "w").write(data)
        
        if logging["debug"]:
            register(log, "DEBUG", "Successfully updated latest command run of `pls daily`.")
    elif (datetime.strptime(datetime.now().strftime("%x-%X"), "%x-%X") - datetime.strptime(data["daily"], "%x-%X")).total_seconds > 23400:
        request = post(f"https://discord.com/api/v8/channels/{channel_id}/messages", headers={"authorization": token}, data={"content": "pls daily"})
    
        if request.status_code != 200 and logging["warning"]:
            register(log, "WARNING", f"Failed to send command `pls daily`. Status code: {request.status_code} (expected 200).")
            return
        
        if logging["debug"]:
            register(log, "DEBUG", "Successfully sent command `pls daily`.")
        
        data["daily"] == datetime.now().strftime("%x-%X")
           
        open(f"{cwd}/data.json", "w").write(data)
        
        if logging["debug"]:
            register(log, "DEBUG", "Successfully updated latest command run of `pls daily`.") 
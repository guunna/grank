from requests import post
from utils.logger import register

def hunt(log, token, channel_id, logging):
    request = post(f"https://discord.com/api/v8/channels/{channel_id}/messages", headers={"authorization": token}, data={"content": "pls hunt"})
    
    if request.status_code != 200:
        if logging["warning"]:
            register(log, "WARNING", f"Failed to send command `pls hunt`. Status code: {request.status_code} (expected 200).")
        return
    
    if logging["debug"]:
        register(log, "DEBUG", "Successfully sent command `pls hunt`.")
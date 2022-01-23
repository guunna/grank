from requests import post
from utils.logger import register

def fish(log, token, channel_id):
    request = post(f"https://discord.com/api/v8/channels/{channel_id}/messages", headers={"authorization": token}, data={"content": "pls fish"})
    
    if request.status_code != 200:
        register(log, "WARNING", f"Failed to send command `pls fish`. Status code: {request.status_code} (expected 200).")
        return
    
    register(log, "DEBUG", "Successfully sent command `pls fish`.")
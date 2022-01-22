from datetime import datetime
from os import makedirs
from utils.console import fore, style

def initialize_logger(cwd):
    try:
        makedirs(f"{cwd}/logs/")
    except FileExistsError:
        pass
    
    return open(f"{cwd}/logs/{datetime.now().strftime('%d-%m-%Y~%H-%M')}.log", "w")

def register(log, level, text):
    print(f"{datetime.now().strftime('[%x-%X]')} - {style.Italic}{fore.Bright_Red if level == 'ERROR' else fore.Bright_Blue if level == 'DEBUG' else fore.Bright_Yellow}[{level}]{style.RESET_ALL} | {text}")
    
    log.write(f"{datetime.now().strftime('[%x-%X]')} - [{level}] | {text}\n")
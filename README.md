<div align="center">
    <h1>Grank</h1>
    <img src="https://styles.redditmedia.com/t5_3ozad/styles/communityIcon_xvlhdypngrq61.png?width=256&s=d8079b417dde76bf9f6015d5dec902e0756e5c4f" alt="Dank Memer Logo">
</div>

<div align="center">
    <a href="https://github.com/didlly">
    <img src="https://img.shields.io/github/license/didlly/grank">
    <img src="https://img.shields.io/github/languages/top/didlly/grank">
    <img src="https://img.shields.io/bitbucket/issues-raw/didlly/grank">
    </a>
    <a href="https://didlly.github.io/grank">
    <img src="https://img.shields.io/website?down_color=lightgrey&down_message=Offline&up_color=blue&up_message=Online&url=https%3A%2F%2Fdidlly.github.io%2Fgrank%2F">
    </a>
</div>

<div align="center">
    <sub>Inspired by <a href="https://github.com/dankgrinder/dankgrinder">this</a> repository. This is a WIP and there will be more functions added in the future.</sub>
</div>

## What is Grank?
<div align="center">
    <img src="https://raw.githubusercontent.com/didlly/grank/main/assets/cover.png" alt="Cover image">
</div>

Grank is a feature-rich script that automatically grinds Dank Memer for you.

## Supported commands (more to be added in the future).
- ```pls beg```
- ```pls dig```
- ```pls fish```
- ```pls hunt```

## Getting Started.

### Setting up the environment.
- Install [Python](https://www.python.org/). Make sure to have the ```Install Pip``` option ticked.
- Download this repository by clicking [this](https://github.com/didlly/grank/archive/refs/heads/main.zip) link. 
- Extract the files, and open a command prompt window in ```/src/```.
- Run ```pip install -r requirements.txt```

### Getting your Discord token and channel ID.
To use Grank, you will have to provide your Discord token and a channel ID. Don't worry - these details are never shared with anyone.

#### How do you get this information?
- [Useful article on how to get your Discord token.](https://discordhelp.net/discord-token)

- [Useful article on how to get a channel ID.](https://docs.statbot.net/docs/faq/general/how-find-id/)

You are now ready to use the program. Run ```src/main.py``` to start the program. You do not have to be have Discord open to run the program, so you can have the program running in the background while you do other things!

## Config file
The ```config.yml``` file is used to change the way the program runs.

### ```commands``` category.
Values in the ```commands``` category tell the program whether or not to run certain commands.

| Name  | Type | Default Value |
| ------------- | ------------- | ------------- |
| ```beg```  | ```Boolean``` | ```True```  |
| ```dig```  | ```Boolean``` | ```True```  |
| ```fish```  | ```Boolean``` | ```True```  |
| ```hunt```  | ```Boolean``` | ```True```  |

### ```cooldowns``` category.
Values in the ```cooldowns``` category tell the program the cooldowns between commands and the loop cooldown.

| Name  | Type | Default Value |
| ------------- | ------------- | ------------- |
| ```commands```  | ```Integer``` | ```1```  |
| ```loop```  | ```Integer``` | ```41```  |

## Disclaimer
This is a self-bot. Self-bots are against Discord's TOS. Automation of Dank Memer commands also breaks Dank Memer's rules. By using this program you acknowledge that I can take no responsibility for actions taken against you if you are caught.
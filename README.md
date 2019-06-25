# pbemonitor

A Discord bot ready to be deployed on Heroku to monitor when the League of Legends PBE server is up. Logging in right when the server goes live allows for fast entry into the long queue caused by the new game mode Teamfight Tactics.

### Prerequisites
- Heroku
- Python 3  
- Requests  
- discord.py

## Setup
Deploy onto Heroku

Set config vars for Heroku:  
- cmd_prefix  
- token
- off_delay
- on_delay

> **cmd_prefix** is the Discord command prefix.  
> **token** is the Discord bot token.  
> **off_delay** is the monitor delay when the server is offline, this number should be low to catch when the server goes live.  
> **on_delay** is the monitor delay when the server is online, I would recommend 300 seconds to catch when the server goes under maintenance.  

## Usage
Start the monitor by using **!start** in the text channel that you want the notification to be in. **!stop** will stop the monitor.

The bot will send a message when the server goes either live or under maintenance.
![Discord Notification](https://i.imgur.com/KLZf071.png)  
When the server goes live, the bot will send a message into the channel.

To check the current server status, look at the bot's status.  
![Bot Status](https://i.imgur.com/SFjZxH3.png)

### Disclaimer
This project was created to integrate a program within Discord using Heroku's services and is not affiliated with any of the services used. It is purely for educational purposes. I am not responsible for anything that happens by using this program. Use at your own risk.

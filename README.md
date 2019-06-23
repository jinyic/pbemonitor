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
- delay

> cmd_prefix is the Discord command prefix.  
> token is the Discord bot token.  
> delay is the monitor delay in seconds

## Usage
Once the PBE server is under maintenance, start the monitor by using the command **!start** in the text channel that you want the notification to be in.  
![Discord Notification](https://i.imgur.com/KLZf071.png)  
When the server goes live, the bot will repeatedly send messages into the text channel. Use **!stop** to stop the notifications.

To check whether the bot is monitoring or not, look at the bot's status.  
![Bot Status](https://i.imgur.com/ogmWgOY.png)

### Disclaimer
This project was created to integrate a program within Discord using Heroku's services and is not affiliated with any of the services used. It is purely for educational purposes. I am not responsible for anything that happens by using this program. Use at your own risk.

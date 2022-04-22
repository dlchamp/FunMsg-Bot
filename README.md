# FunMsg Bot
Monitor a configured channel and randomly send a "fun msg" after a certain amount of messages have been sent without the "activity" expiring.



## Self Hosting

### Dependencies

* Built on the latest [Python3 - 3.9.7](https://www.python.org/downloads/)
* see requirements.txt for Python dependencies
* Python installed with PATH access in Windows

### Getting Started

#### Setting up Discord Bot
1. Login to Discord web - https://discord.com
2. Navigate to Discord Developer Portal - https://discord.com/developers/applications
3. Click *New Application*
4. Give the Appplication a name and *Create*
5. Add image for Discord icon
6. Go to Bot tab and click *Add Bot*
7. Keep the default settings for Public Bot - *checked* and Require OAuth2 Code Grant - *unchecked*
8. Enabled Message Content intents
9. Copy Token
10. Go to OAuth2 tab
11. Under *Scopes* - Check Bot
12. Under *Bot Permissions* - check Send messages, Read Message History, View Channels
13. Copy the generated link and Go to the URL in your browser - Invite Bot to your Discord server


#### Windows Installation and Run
1. Download this repo and extract to a location
2. Open command and navigate inside of bot's directory
3. Open the .env-sample file in a text editor and paste in your copied token, save, and rename the .env-sample to .env
4. Run `python -u main.py`

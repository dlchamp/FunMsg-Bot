# FunMsg Bot
Monitor a configured channel and randomly send a "fun msg" after a certain amount of messages have been sent without the "activity" expiring.


## HEROKU SPECIFIC INSTRUCTIONS


### Discord Bot Token and Server Invitation

1. Login to Discord web - https://discord.com
2. Navigate to Discord Developer Portal - https://discord.com/developers/applications
3. Click *New Application*
4. Give the Appplication a name and *Create*
5. Add image for Discord icon
6. Go to Bot tab and click *Add Bot*
7. Optional - Add image
8. Copy the token and paste it somewhere safe. You will need it later
9. Navigate to OAuth2 Tab > URL Generator
10. Check **BOT** under the SCOPES section
11. In the BOT PERMISSIONS section, check the following:
    - Read Messages/View Channels
    - Send Messages

12. Copy the GENERATED URL link and paste it into your browser or in a discord message. Click the link to invite the bot


### Getting Started
**Github**
1. Login to github
2. Fork this heroku branch of the repo
3. Go into config.py and add your monitor channel ID and edit other config attributes if you wish
4. Make the repo private to prevent unauthorized access to your bot code

**Heroku**
1. Login to Heroku - https://id.heroku.com/login
2. Create a new app - give it a name
3. Settings > Config vars - Reveal Config Vars
4. Replace KEY with `TOKEN` and VALUE with your bot token from above (step 8)
5. Add and head back to Deploy
6. Deployment Method - Connnect with Github
7. Add the forked repo to your Heroku account
8. Select the Heroku branch to deploy
9. Deploy the branch
10. Navigate to Resources tab - Dynos
11. Click Edit icon - enable the worker
12. Save
13. Top right corner - More - View Logs
14. Should see the bot load and print the message line that the bot is online and ready.
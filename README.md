# BDE Bot
Source code of the [BDE Algo](https://bde-algo.info)'s Discord bot.

**DISCLAIMER: This is NOT A LIBRARY, but an implementation based on Pycord, 
suited for our needs.**  
We make it open-source because we are open to contributions !

## Set up

To set up this bot:
- Install the python dependencies with `pip install -r requirements.txt`
- Create a file `secret.py` in the `robot` directory, and add a string variable
  `token` containing your bot token.
  Warning: do not add this file to git. 
  By default, it is excluded (listed in `robot/.gitignore`).

## Run

Once you're done with the setup, launch `main.py` with `python main.py`.

To add your bot to a server, use this link:
https://discord.com/api/oauth2/authorize?client_id=<id>&permissions=<perm>&scope=bot%20applications.commands

In this link, do not forget to replace `<id>` by your application id, 
and `<perm>` by the integer authorization value, 
both of which you can get here: https://discord.com/developers/applications/.

# Usage

Documentation for the currently implemented commands is available in
[COMMANDS_USAGE](./COMMANDS_USAGE.md).

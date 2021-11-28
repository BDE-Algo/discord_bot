# BDE Bot
Source code of the [BDE Algo's Discord](https://discord.gg/4wh9yzm) bot.

**DISCLAIMER: This is NOT a library, but an implementation based on Pycord, 
suited for our needs.**  
We make it open-source because we are open to contributions !

## Set up and run

The easiest way of setting up this bot is with Docker. 
With docker-compose (assuming you already have it installed):
1. Clone the git repository onto your machine
2. `cd` into the cloned directory
3. Create a file `secret.py` in the `robot` folder, 
   and add a string variable `token` containing your Discord bot token
4. Finally, run `docker-compose up -d`

If you can't use docker:
1. Clone the git repository onto your machine
2. Install the python dependencies with `pip install -r requirements.txt`
   (the usage of a dedicated python environment is recommended)
3. Create a file `secret.py` in the `robot` folder, 
   and add a string variable `token` containing your Discord bot token
4. Once you're done with this setup, run `python main.py`.  
   You might want to use `tmux` or `screen` to detach the script from your terminal

## Additional resources

To add your bot to a server, use this link:
https://discord.com/api/oauth2/authorize?client_id=<id>&permissions=<perm>&scope=bot%20applications.commands

In this link, do not forget to replace `<id>` by your application id, 
and `<perm>` by the integer authorization value, 
both of which you can get here: https://discord.com/developers/applications/.

## Usage

Documentation for the currently implemented commands is available in
[COMMANDS_USAGE](./COMMANDS_USAGE.md).

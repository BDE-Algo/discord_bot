# BDE Bot's usage

This little guide will show you how to use the commands this bot supports.

To use a command, prefix it with: `!`. E.g., `!help`

### `help`

Self-explanatory, prints some help text.

### `get_role`

Grants a role to the calling user.

Usage: `!get_role @Role`
- Where `@Role` is a mention of an existing role

### `remove_role`

The exact opposite of `get_role`, 
removes the role from the calling user.

Usage: `!remove_role @Role`
- Where `@Role` is a mention of an existing role

### `clear_channel`

Removes all messages from the current channel, 
except the specified ones.  
You can get the ID of a message by right-clicking on it and selecting "Copy ID".

Usage: `!clear_channel 1234 5678 ...`
- Where `1234` and `5678` are IDs of messages
- The command takes an arbitrary number of IDs, and won't delete those

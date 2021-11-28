"""
BDE Bot
=======

Role management
---------------

For the bot to be able to assign/unassign a role, its role must be above
in the roles hierarchy.
Otherwise said, roles the bot should be able to assign/unassign should be
below its in the listing.

Future work
-----------

- Use logging instead of print
- New commands

Resources
---------

- pycord's API reference: https://docs.pycord.dev/en/master/api.html
- Discord applications: https://discord.com/developers/applications/
"""

from discord import Intents
from discord.role import Role
from discord.ext import commands
from discord.errors import NotFound, Forbidden
from discord.ext.commands.context import Context

from typing import Callable, Any


description = """BDE Algo's bot"""

intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


async def handle(ctx: Context,
                 func: Callable, *,
                 args: tuple = None,
                 kwargs: dict = None,
                 delay: int = 5,
                 exceptions: tuple = (Forbidden, ),
                 success_msg: str = '',
                 error_msg: str = '',
                 react: bool = True,
                 delete: bool = True,
                 ) -> Any:
    """
    Provides utilities for handling methods.
    FIXME: Could be replaced by decorators or other patterns.
    """

    if args is None:
        args = ()

    if kwargs is None:
        kwargs = {}

    try:
        val = await func(*args, **kwargs)
    except exceptions:
        if react:
            await ctx.message.add_reaction('👎')
        print(error_msg)
        val = None  # Define a default value to avoid errors when returning
    else:
        if react:
            await ctx.message.add_reaction('👍')
        print(success_msg)

    if delete:
        await ctx.message.delete(delay=delay)

    return val


@bot.command()
async def usage(ctx):
    """Prints the usage documentation for all commands"""
    # FIXME: generate the doc from the functions' docstrings.
    lnk = 'https://github.com/BDE-Algo/discord_bot/blob/main/COMMANDS_USAGE.md'
    await handle(ctx, func=ctx.channel.send, kwargs={
            'content': f'For the usage documentation, follow this link: {lnk}',
            'delete_after': 10,
        },
    )


@bot.command()
async def get_role(ctx: Context, role: Role) -> None:
    """Acquire a new role"""
    await handle(
        ctx, func=ctx.message.author.add_roles, args=(role, ),
        kwargs={'reason': 'Requested by user'},
        success_msg=f'Added role {role.name!r} to {ctx.author} !'
    )


@bot.command()
async def remove_role(ctx: Context, role: Role) -> None:
    """Revoke a role membership"""
    await handle(
        ctx, func=ctx.message.author.remove_roles, args=(role, ),
        kwargs={'reason': 'Requested by user'},
        success_msg=f'Removed role {role.name!r} from {ctx.author} !'
    )


#@bot.command()
async def update_message(ctx: Context, message_id: int, *new_content) -> None:
    """Updates a message previously sent by this bot"""

    # TODO: check permissions

    message = await handle(
        ctx, func=ctx.channel.fetch_message, args=(message_id, ),
        exceptions=(NotFound, Forbidden)
    )

    if message is None:
        # Couldn't get message
        return

    try:
        print(new_content)
        await message.edit(
            content=' '.join(new_content)
        )
    except (Forbidden, ):
        print(f"Couldn't modify message {message_id!r}")


@bot.command()
async def clear_channel(ctx: Context, *excluded_messages) -> None:
    """Deletes all messages (except specified) from the current channel"""

    if not ctx.channel.permissions_for(ctx.author).manage_messages:
        await ctx.message.add_reaction('👎')
        await ctx.message.delete(delay=5)

    # Convert excluded message ids to int
    try:
        excluded_messages = list(map(int, excluded_messages))
    except ValueError:
        # Got an invalid message id
        return

    async for message in ctx.channel.history():
        if message.id not in excluded_messages:
            try:
                await message.delete()
            except NotFound:
                # Message was delete before we got to it
                pass

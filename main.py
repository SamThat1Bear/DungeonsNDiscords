import discord, random, datetime
from discord.ext import commands

from users import *
from items import *
from constants import *

def log(info):
    with open("log.log", "a") as logger:
        logger.write(f"[{datetime.datetime.now()}] {info}\n")

active_players = []
active_users = []

print(discord.__version__)
log("Starting up...")
intent = discord.Intents().default()
intent.members = True
intent.message_content = True

bot = commands.Bot(intents = intent, command_prefix="!")

@bot.event
async def on_ready(): log(f"Logged in as user {bot.user}")

@bot.command()
async def roll(ctx, n = 6): await ctx.send(f"{random.randint(1, int(n)+1)}")

@bot.command()
async def join(ctx):
    user = ctx.author
    log(f"{user} attempts to join the game...")
    if not user in active_players:
        active_players.append(user)
        await ctx.send(f"User {user} joined the game!")
        log("...attempt successful")

        log("Attempting to create User...")
        try:
            new_user = User(user)
            active_users.append(new_user)
            log("...attempt successful.")
        except:
            log("...user creation failed")
    else:
        await ctx.send("You are already in game.")
        log("...user already in game")

@bot.command()
async def player(ctx):
    log(f"Requested player embed by user {ctx.author}...")
    user = get_user_from_author(active_users, ctx.author)
    if user:
        await ctx.send(embed=user.get_player_embed())
        log("...player embed sent.")
    else:
        await ctx.send("You are not in game yet")
        log("...no user found")

@bot.command()
async def rollforstats(ctx):
    author = ctx.author
    user = get_user_from_author(active_users, author)
    log(f"User {author} attempts to roll for stats...")

    if not user:
        log(f"...no user profile")
        await ctx.send("You are not in the game")
        return
    
    if user.stats:
        log(f"...user already rolled for stats")
        await ctx.send("You have already rolled for stats")
        return

    new_stats = {}
    for stat in PLAYER_STATS:
            new_stats[stat] = random.randint(1, 10)

    rolled_stats_embed = discord.Embed(title="Rolling for stats...")
    new_stats_text = "\n".join([f"{stat.title()}: {value}" for stat, value in new_stats.items()])
    rolled_stats_embed.add_field(name="", value=new_stats_text)

    user.set_rolled_stats(new_stats)

    log(f"...stats have been rolled successfully")
    await ctx.send(embed=rolled_stats_embed)

@bot.command()
async def chooseclass(ctx, class_name):
    author = ctx.author
    user = get_user_from_author(author)
    log(f"User {author} attemps to select a class...")

    if not user:
        log("...no user profile")
        await ctx.send("You are not in the game.")
        return

    if user.player_class:
        log("...class was already selected.")
        await ctx.send("You have selected a class")
        return
    
    class_name = class_name.lower()
    if not class_name in PLAYER_CLASSES["base"]:
        log("...no existing class selected")
        await ctx.send(f"There's no class named {class_name}")
        return
    
    log("...class has been selected successfully")
    user.set_player_class(class_name)
    await ctx.send(f"You class has been selected.")

@bot.command()
async def displayitem(ctx, inventory_slot):
    author = ctx.author
    user = get_user_from_author(author)
    log(f"User {author} attempts to gather item information...")
    if not user:
        log("...no user profile")
        await ctx.send("You are not in the game.")
        return
    try:
        log(f"...gathering item information...")
        print(inventory_slot)
        item: Item = user.get_item_in_slot(int(inventory_slot)-1)
        print(item)
    except (IndexError, ValueError):
        log(f"...no such slot in player inventory")
        await ctx.send("You don't have an item in that slot.")
        return
    except Exception as e:
        log(f"...item information gathering failed ({e})")
        await ctx.send("Problem occured while gathering item information.")
        return
    
    log("...item information gathered successfully, displaying item.")
    item_display_embed = discord.Embed(title=f"Displaying Item: {item}", color=discord.Color(RARITY_COLORS[item.rarity]))
    item_text = "\n".join([f"{stat.title()}: {value}" for stat, value in item.stats.items()])

    item_display_embed.add_field(name=item.item_type.replace("_", " ").title(), value=item_text)

    await ctx.send(embed=item_display_embed)

@bot.command()
async def inventory(ctx):
    author = ctx.author
    user = get_user_from_author(author)
    inventory_text = [f"{index+1}. {item}" for index, item in enumerate(user.get)]


bot.run(ENVIROMENT["API_KEY"])
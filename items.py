import random
from constants import PLAYER_EQUIPMENT, ITEM_NAMES_PATH, PLAYER_STATS, MAINHAND_PER_CLASS, OFFHAND_PER_CLASS, STATS_PER_CLASS

class Item:
    def __init__(self, name, item_type, stats, rarity, sub_type = None) -> None:
        self.name = name
        self.item_type = item_type
        self.sub_type = sub_type
        self.stats = stats
        self.rarity = rarity
    
    def __str__(self): return self.name
    def get_name(self): return self.name

def generate_item(for_user) -> Item:
    base = round(max(for_user.leveling_info["level"], 1))
    player_class = for_user.player_class
    rarities = min(base, 6), min(base+1, 6)
    rarity = random.choices(rarities, (80, 20))[0]
    item_type = random.choice(PLAYER_EQUIPMENT)
    match(item_type):
        case "main_hand": sub_type = random.choice(MAINHAND_PER_CLASS[player_class])
        case "off-hand": sub_type = random.choice(OFFHAND_PER_CLASS[player_class])
        case _: sub_type = None
    name = generate_item_name(rarity, sub_type or item_type)
    stats = generate_stats(rarity, player_class)
    return Item(name, item_type, stats, rarity, sub_type)

def generate_item_name(rarity, type):
    item_level = 0
    postadj = None

    if rarity >= 3: item_level = 1
    if rarity >= 5: item_level = 2

    with open(fr"{ITEM_NAMES_PATH}{item_level}preadjectives.txt") as pre_file:
        preadj = pre_file.read().split("\n")
    if item_level >= 2:
        with open(fr"{ITEM_NAMES_PATH}{item_level}postadjectives.txt") as post_file:
            postadj = post_file.read().split("\n")
    
    pre = random.choice(preadj)
    post = random.choice(postadj) if postadj else None
    name_type = type.replace("_", " ")
    name = f"{pre} {name_type}" + (f" of {post}" if post else "")
    return name.title()

def generate_stats(rarity, player_class):
    stats = {stat: 0 for stat in PLAYER_STATS}
    positive_stats = 3*(rarity//1)
    negative_stats = max(-((rarity-3)//1)**2 + 10, 0)

    for _ in range(positive_stats):
        print(player_class)
        stat_to_chose = random.choices((STATS_PER_CLASS[player_class], PLAYER_STATS), (.6, .4))[0]
        stat = random.choice(stat_to_chose)
        print(stat_to_chose, stat)
        stats[stat] += 1
    
    for _ in range(negative_stats):
        stat_to_chose = random.choices((STATS_PER_CLASS[player_class], PLAYER_STATS), (.2, .8))[0]
        stat = random.choice(stat_to_chose)
        stats[stat] -= 1

    return stats


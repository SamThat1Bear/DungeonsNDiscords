import random

class Item:
    def __init__(self, name, item_type, stats, rarity, sub_type = None) -> None:
        self.name = name
        self.item_type = item_type
        self.sub_type = sub_type
        self.stats = stats
        self.rarity = rarity
    
    def __str__(self): return self.name

def generate_item(for_user) -> Item:
    base = round(max(for_user.leveling_info["level"]))
    rarities = min(base, 6), min(base+1, 6)
    rarity = random.choices(rarities, (80, 20))[0]
    name: str
    item_type: str
    stats: dict
    return Item(name, item_type, stats, rarity)
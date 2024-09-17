from constants import *
from discord import Embed

class User:
    def __init__(self, user) -> None:
        self.user = user
        self.equipment = [None] * 7
        self.player_class = None
        self.stats = {}
        self.inventory = []
        self.leveling_info = {"level": 1, "current_xp": 0, "xp_needed": 15}
        self.wallet = 0
    
    def add_item_to_inv(self, item) -> None:
        self.inventory.append(item)
    
    def equip_item(self, item) -> None:
        item_type = item.type
        try: item_slot = PLAYER_EQUIPMENT.index(item_type)
        except ValueError: item_slot = None
        
        if item_slot:
            old_item = self.equipment[item_slot]
            self.add_item_to_inv(old_item)
            self.equipment[item_slot] = item
            try: self.inventory.remove(item)
            except ValueError: pass
    
    def get_combined_stats(self) -> dict:
        stats = self.stats.copy()
        for equipment in self.equipment:
            for stat, value in equipment:
                stats[stat] = stats.get(stat, 0) + value
        return stats
    
    def add_experience(self, amount) -> None:
        self.leveling_info["current_xp"] += amount
        if self.leveling_info["current_xp"] >= self.leveling_info["xp_needed"]: self.level_up()
    
    def level_up(self) -> None:
        self.leveling_info["current_xp"] -= self.leveling_info["xp_needed"]
        self.leveling_info["xp_needed"] = 15 + self.leveling_info["level"]*10
    
    def get_player_embed(self) -> Embed:
        UNROLLED = "Unrolled"
        UNCHOSEN = "Unchosen"

        chosen_class = self.player_class
        if self.player_class == None: chosen_class = UNCHOSEN
        
        player_embed = Embed(title=f"Your Character: {self.get_name().title()}, the {chosen_class}")
        
        equipment_text = "\n".join([f"{(equipment_type.title())}: {str(self.equipment[index]).title()}".replace("_", " ") for index, equipment_type in enumerate(PLAYER_EQUIPMENT)])
        stat_text = "\n".join([f"{stat.title()}: {self.stats.get(stat, UNROLLED)}" for stat in PLAYER_STATS])
        wallet_text = f"Gold: {self.wallet}"

        player_embed.add_field(name="Equipment", value=equipment_text)
        player_embed.add_field(name="Stats", value=stat_text)
        player_embed.add_field(name="Wallet", value=wallet_text)

        return player_embed
    
    def get_name(self) -> str: return str(self.user).split("#")[0]

    def set_rolled_stats(self, stats) -> None: self.stats = stats
    
    def alter_money(self, value) -> None: self.wallet += value
    
    def set_player_class(self, class_name) -> None: self.player_class = class_name
    
    def get_item_in_slot(self, slot): return self.inventory[slot]
    
    def get_inventory(self) -> list: return self.inventory[:]


def get_user_from_author(active_users, author) -> User|None:
    for user in active_users:
        if user.user == author: return user
    return None

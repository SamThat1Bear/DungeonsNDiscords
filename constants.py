import dotenv

PLAYER_STATS = ["strength", "endurance", "wisdom", "dexterity", "agility", "charisma"]
PLAYER_CLASSES = {"base": ["wizard", "bard", "warrior", "thief"],
                  "secondary_wizard": ["mage", "druid", "sorcerer"],
                  "secondary_bard": ["ranger", "cleric"],
                  "secondary_warrior": ["paladin", "warlock", "barbarian"],
                  "secondary_thief": ["rogue", "monk"]}
PLAYER_EQUIPMENT = ["main_hand", "off-hand", "head_armor", "chest_armor", "leg_armor", "gloves", "boots"]
MAINHAND_EQUIPMENT = ["wand", "instrument", "sword", "dagger", "staff", "artifact", "bow", "longsword", "battle_axe", "claymore", "fighting_staff"]
OFFHAND_EQUIPMENT = ["tome", "spell_book", "talisman", "shield", "potion", "quiver"]
RARITIES = ["common", "uncommon", "rare", "epic", "legendary", "divine", "perfect"]
RARITY_COLORS = [7309199, 4422986, 4995273, 10493670, 15571475, 10230298, 10289138]

MAINHAND_PER_CLASS = {"wizard": ["wand"], "bard": ["instrument"], "warrior": ["sword", "longsword"],
                      "thief": ["dagger"], "mage": ["wand", "artifact"], "druid": ["staff", "artifact"],
                      "sorcerer": ["wand", "staff", "artifact"], "ranger": ["bow", "instrument"], "cleric": ["longsword", "artifact"],
                      "paladin": ["longsword", "artifact"], "warlock": ["battle_axe", "claymore", "sword"], "barbarian": ["claymore", "battle_axe"],
                      "rogue": ["dagger", "bow", "sword"], "monk": ["fighting_staff"]}

OFFHAND_PER_CLASS = {"wizard": ["tome", "spell_book", "talisman"], "bard": ["tome", "talisman", "potion"], "warrior": ["talisman", "shield"],
                     "thief": ["talisman", "potion"], "mage": ["tome", "spell_book", "talisman"], "druid": ["tome", "talisman", "spell_book", "potion"],
                     "sorcerer": ["tome", "talisman"], "ranger": ["talisman", "shield", "quiver"], "cleric": ["talisman", "potion"],
                     "paladin": ["talisman", "shield"], "warlock": ["talisman", "shield"], "barbarian": ["talisman", "shield"],
                     "rogue": ["talisman", "shield", "quiver"], "monk": ["talisman"]}
STATS_PER_CLASS ={"wizard": ["wisdom", "strength"], "bard": ["wisdom", "charisma"], "warrior": ["strength", "endurance"],
                  "thief": ["dexterity", "agility"], "mage": ["widsom", "strength"], "druid": ["wisdom", "dexterity"],
                  "sorcerer": ["wisdom", "endurance"], "ranger": ["dexterity", "agility"], "cleric": ["endurance", "agility"],
                  "paladin": ["dexterity", "strength"], "warlock": ["endurance", "strength"], "barbarian": ["strength", "endurance"],
                  "rogue": ["dexterity", "strength"], "monk": ["strength", "agility"]}
ITEM_NAMES_PATH = r"weapinf/"

ENVIROMENT = dotenv.dotenv_values(".env")
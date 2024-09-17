import dotenv

PLAYER_STATS = ["strength", "endurance", "wisdom", "dexterity", "agility", "charisma"]
PLAYER_CLASSES = {"base": ["wizard", "bard", "warrior", "thief"],
                  "secondary_wizard": ["mage", "druid", "sorcerer"],
                  "secondary_bard": ["ranger", "cleric"],
                  "secondary_warrior": ["paladin", "warlock", "barbarian"],
                  "secondary_thief": ["rogue", "monk"]}
PLAYER_EQUIPMENT = ["main_hand", "off-hand", "head_armor", "chest_armor", "leg_armor", "gloves", "boots"]
MAINHAND_EQUIPMENT = ["wand", "instrument", "sword", "dagger", "staff", "artifact", "bow", "longsword", "battle_axe", "claymore", "fighting_staff"]
OFFHAND_EQUIPMENT = ["tome", "spell_book", "talisman", "shield", "potion"]
RARITIES = ["common", "uncommon", "rare", "epic", "legendary", "divine", "perfect"]
RARITY_COLORS = [7309199, 4422986, 4995273, 10493670, 15571475, 10230298, 10289138]

ENVIROMENT = dotenv.dotenv_values(".env")
# pylint: disable=invalid-name
"""Lambda module for learning sqlite3"""

import os
import sqlite3

###############################################################################
print(f"\n\n" + "#" * 79)
print(f"Assignment - Part 1, Querying a Database")
print(f"#" * 79 + "\n")
###############################################################################

path = os.path.join("file:",
                    os.path.abspath("."),
                    "module1-introduction-to-sql/",
                    "rpg_db.sqlite3")
db = sqlite3.connect(path)
c = db.cursor()

query1 = "SELECT COUNT() FROM charactercreator_character"
chars = c.execute(query1).fetchone()[0]
print(f"There are {chars} total characters.")

print(f"Subclasses:")

query2 = "SELECT COUNT() FROM charactercreator_cleric"
clerics = c.execute(query2).fetchone()[0]
print(f"    Cleric: {clerics}")

query3 = "SELECT COUNT() FROM charactercreator_fighter"
fighters = c.execute(query3).fetchone()[0]
print(f"    Fighter: {fighters}")

query4 = "SELECT COUNT() FROM charactercreator_thief"
thieves = c.execute(query4).fetchone()[0]
print(f"    Thief: {thieves}")

query5 = "SELECT COUNT() FROM charactercreator_necromancer"
necros = c.execute(query5).fetchone()[0]
print(f"    Necromancer: {necros}")

query6 = "SELECT COUNT() FROM charactercreator_mage"
magi = c.execute(query6).fetchone()[0] - necros
print(f"    Mage: {magi}")

query7 = "SELECT COUNT() FROM armory_item"
items = c.execute(query7).fetchone()[0]
print(f"There are {items} total items.")

query8 = "SELECT COUNT() FROM armory_weapon"
weapons = c.execute(query8).fetchone()[0]
print(f"{weapons} items are weapons.")
non_weapons = items - weapons
print(f"{non_weapons} items are non-weapons.")

characters = range(1, 21)
total_items = 0
total_weapons = 0
for character in characters:
    query1 = "SELECT COUNT() " \
             "FROM charactercreator_character_inventory " \
             "WHERE character_id = " + str(character)
    items = c.execute(query1).fetchone()[0]
    total_items += items
    print(f"Character {character} has {items} items.")
    query2 = "SELECT character_id " \
             "FROM charactercreator_character_inventory c " \
             "WHERE character_id = " + str(character) + " AND " \
             "EXISTS(SELECT item_ptr_id " \
             "FROM armory_weapon " \
             "WHERE item_ptr_id = c.item_id)"
    weapons = len(c.execute(query2).fetchall())
    total_weapons += weapons
    print(f"Character {character} has {weapons} weapons.")

ave_items = total_items / 20
ave_weapons = total_weapons / 20
print(f"On average, characters 1-20 have {ave_items} items.")
print(f"On average, characters 1-20 have {ave_weapons} weapons.")

# save and close
db.close()

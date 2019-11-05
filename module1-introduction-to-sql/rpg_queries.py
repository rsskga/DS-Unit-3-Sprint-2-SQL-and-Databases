# pylint: disable=invalid-name
"""Lambda module for learning sqlite3"""

import os
import sqlite3

# select
# t = ("3",)
# c.execute("SELECT * "
#           "FROM charactercreator_character "
#           "WHERE character_id = ?", t)
# print(c.fetchone())

# explicit inner join
# c.execute("SELECT * "
#           "FROM charactercreator_character "
#           "INNER JOIN charactercreator_mage "
#           "ON character_id = character_ptr_id")
# print(c.fetchone())

# implicit inner join
# c.execute("SELECT * "
#           "FROM charactercreator_character, charactercreator_mage "
#           "WHERE character_id = character_ptr_id")
# print(c.fetchone())

# another inner join
# c.execute("SELECT * "
#           "FROM charactercreator_character "
#           "WHERE character_id "
#           "IN (SELECT character_ptr_id FROM charactercreator_mage)")
# print(c.fetchone())

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

query1 = "SELECT character_id FROM charactercreator_character"
chars = len(c.execute(query1).fetchall())
print(f"There are {chars} total characters.")

print(f"Subclasses:")

query2 = "SELECT character_ptr_id FROM charactercreator_cleric"
clerics = len(c.execute(query2).fetchall())
print(f"    Cleric: {clerics}")

query3 = "SELECT character_ptr_id FROM charactercreator_fighter"
fighters = len(c.execute(query3).fetchall())
print(f"    Fighter: {fighters}")

query4 = "SELECT character_ptr_id FROM charactercreator_thief"
thieves = len(c.execute(query4).fetchall())
print(f"    Thief: {thieves}")

query5 = "SELECT mage_ptr_id FROM charactercreator_necromancer"
necros = len(c.execute(query5).fetchall())
print(f"    Necromancer: {necros}")

query6 = "SELECT character_ptr_id FROM charactercreator_mage"
magi = len(c.execute(query6).fetchall()) - necros
print(f"    Mage: {magi}")

# total = clerics + fighters + magi + necros + thieves
# print(f"Total: {total}")

query7 = "SELECT item_id FROM armory_item"
items = len(c.execute(query7).fetchall())
print(f"There are {items} total items.")

query8 = "SELECT item_ptr_id FROM armory_weapon"
weapons = len(c.execute(query8).fetchall())
print(f"{weapons} items are weapons.")
non_weapons = items - weapons
print(f"{non_weapons} items are non-weapons.")

characters = range(1, 21)
total_items = 0
total_weapons = 0
for character in characters:
    query1 = "SELECT item_id " \
             "FROM charactercreator_character_inventory " \
             "WHERE character_id = " + str(character)
    items = len(c.execute(query1).fetchall())
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

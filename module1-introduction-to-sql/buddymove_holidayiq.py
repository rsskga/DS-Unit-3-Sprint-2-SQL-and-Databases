# pylint: disable=invalid-name
"""Lambda module for learning sqlite3 interaction with pandas"""

import os
import sqlite3
import warnings
import pandas as pd

warnings.simplefilter(action="ignore", category=UserWarning)

# label output
print("\n" + "#" * 79)
print("Assignment - Part 2, Making and Populating a Database")
print("#" * 79 + "\n")

# load and evaluate data
csv = os.path.join("file:",
                   os.path.abspath("."),
                   "module1-introduction-to-sql/",
                   "buddymove_holidayiq.csv")

df = pd.read_csv(csv, header=0, names=["user_id",
                                       "sports",
                                       "religious",
                                       "nature",
                                       "theatre",
                                       "shopping",
                                       "picnic"])

print("The dataframe shape is ", df.shape)
print("\nThe sum of null values is: \n" + str(df.isnull().sum()))

# create new database and connection
path = os.path.join("file:",
                    os.path.abspath("."),
                    "module1-introduction-to-sql/",
                    "buddymove_holidayiq.sqlite3")

db = sqlite3.connect(path)
c = db.cursor()

# send df data to sqlite3
df.to_sql("review", con=db, if_exists="replace", index=False,
          dtype={"user_id": "TEXT",
                 "sports": "INTEGER",
                 "religious": "INTEGER",
                 "nature": "INTEGER",
                 "theatre": "INTEGER",
                 "shopping": "INTEGER",
                 "picnic": "INTEGER"})

rows = c.execute("SELECT COUNT() FROM review").fetchone()
print(f"\nThere are {rows} rows.")

sql = "SELECT COUNT() FROM review WHERE nature >= 100 AND shopping >= 100"
users = c.execute(sql).fetchone()
print(f"\nThere are {users} users who have reviewed 100+ Nature & Shopping.")

query = "SELECT AVG(sports), " \
        "AVG(religious), " \
        "AVG(nature), " \
        "AVG(theatre), " \
        "AVG(shopping), " \
        "AVG(picnic) FROM review"

avs = c.execute(query).fetchall()[0]
ave_sp, ave_re, ave_na, ave_th, ave_sh, ave_pi = avs
print(f"\nThe averages are:")
print(f"    sports: {ave_sp}")
print(f"    religious: {ave_re}")
print(f"    nature: {ave_na}")
print(f"    theatre: {ave_th}")
print(f"    shopping: {ave_sh}")
print(f"    picnic: {ave_pi}")
print("\n")

# save and close db
db.commit()
db.close()

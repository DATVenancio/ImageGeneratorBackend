import sqlite3

connexion = sqlite3.connect("images_db.db")
cursor = connexion.cursor()

#codings table
query = "DROP TABLE IF EXISTS image_coding"
cursor.execute(query)

query = '''
CREATE TABLE IF NOT EXISTS image_coding(
    code TEXT,
    label TEXT
);
'''



cursor.execute(query)

connexion.commit()
connexion.close()
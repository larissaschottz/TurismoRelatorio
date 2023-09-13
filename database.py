import sqlite3

def create_database():
    conn = sqlite3.connect("tourism_database.db")
    cursor = conn.cursor()

    # Create Destinations table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Destinations (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Macro TEXT NOT NULL,
        UF TEXT NOT NULL,
        RegiaoTuristica TEXT NOT NULL,
        Municipio TEXT NOT NULL,
        Cluster TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

def insert_destination(macro, uf, regiao_turistica, municipio, cluster):
    conn = sqlite3.connect("tourism_database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Destinations (Macro, UF, RegiaoTuristica, Municipio, Cluster) VALUES (?, ?, ?, ?, ?)",
                   (macro, uf, regiao_turistica, municipio, cluster))
    conn.commit()
    conn.close()

def get_all_destinations():
    conn = sqlite3.connect("tourism_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Destinations")
    destinations = cursor.fetchall()
    conn.close()
    return destinations

# Outras funções, se necessário

if __name__ == "__main__":
    create_database()

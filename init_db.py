import sqlite3

if __name__ == '__main__':
    con = sqlite3.connect("plant.db")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS watering_log")
    cur.execute("CREATE TABLE watering_log(id TEXT PRIMARY KEY, timestamp TIMESTAMP NOT NULL, pump_id TEXT NOT NULL)")
    con.commit()
    con.close()

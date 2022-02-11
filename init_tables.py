import sqlite3

connect = sqlite3.connect('app_db.db')

create_users_table = """CREATE TABLE IF NOT EXISTS users(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_name TEXT NOT NULL);"""
create_message_table = """CREATE TABLE IF NOT EXISTS messages(
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          message TEXT NOT NULL,
                          user_id INTEGER,
                          FOREIGN KEY (user_id) REFERENCES users(id));"""
cursor = connect.cursor()
cursor.execute(create_users_table)
connect.commit()
cursor.execute(create_message_table)
connect.commit()
cursor.close()
connect.close()
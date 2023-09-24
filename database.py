import sqlite3


def create_table(database):
    conn = sqlite3.connect(database)
    print("Opened database successfully")
    conn.execute('''CREATE TABLE HASH_PATH
         (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
         NAME_PATH           TEXT    NOT NULL,
         HASH_VALUE          TEXT    NOT NULL);''')
    print ("Table created successfully")
    conn.close()


def return_id(database,os_path):
    conn = sqlite3.connect(database)
    print("Opened database successfully")
    cursor = conn.execute("""SELECT * FROM HASH_PATH \
             WHERE NAME_PATH = ? """,(os_path,))
    row = cursor.fetchone()
    
    conn.close()
    return str(row[0])


def insert_table(database,os_path,hash_path):
    conn = sqlite3.connect(database)
    print("Opened database successfully")

    conn.execute("""INSERT INTO HASH_PATH (NAME_PATH,HASH_VALUE) \
      VALUES (?,?);""",(os_path, hash_path))
    conn.commit()
    print("Records created successfully")
    conn.close()
    print ("closed database successfully")


def select_table(database):
    conn = sqlite3.connect(database=database)
    print ("Opened database successfully")

    cursor = conn.execute("SELECT ID, NAME_PATH, HASH_VALUE FROM HASH_PATH")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME_PATH = ", row[1])
        print ("HASH_VALUE = ", row[2], "\n")

    print ("Operation done successfully")
    conn.close()


def delete_table(database,id_target):
    conn = sqlite3.connect(database=database)
    print("Opened database successfully")
    conn.execute("""DELETE from HASH_PATH where ID = ?;""",(id_target))
    conn.commit()
    print ("Operation done successfully")
    conn.close()


def drop_table(database):
    conn = sqlite3.connect(database=database)
    print ("Opened database successfully")
    conn.execute("DROP TABLE HASH_PATH;")
    conn.commit()
    print ("Operation done successfully")
    conn.close()


def update_table(database, os_bath, hash_path, id_target):
    conn = sqlite3.connect(database)
    print ("Opened database successfully")
    conn.execute("""UPDATE HASH_PATH \
         set NAME_PATH = ?, HASH_VALUE = ? where ID = ?""",(os_bath, hash_path, id_target))
    conn.commit()
    print ("Operation done successfully")
    conn.close()
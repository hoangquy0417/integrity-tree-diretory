import os
import hashlib
import database
from sys import argv
# function walking the tree either top-down
def list_directory_tree_with_os_walk(starting_directory):
    for path, directories, files in os.walk(starting_directory):
        print(f"Directory: {path}, type: {type(path)}")
        # for directory in directories:
        #     print(f"subdirectory: {directory}")
        database.insert_table('database.db',path,hash_sha256(path.encode()))
        for file in files:
            #print(os.path.join(path,file))
            hash_value = hash_sha256(os.path.join(path,file).encode())
            database.insert_table('database.db',str(os.path.join(path,file)),hash_value)
           


# hash function sha256
def hash_sha256(path_directory):
    hash256 = hashlib.sha256()
    hash256.update(path_directory)
    return hash256.hexdigest()


# GUI menu
def menu(os_path):
    while(True):
        print("WELLCOME TO DICTORY TREE INTERITY!!!")
        print("1.Access to directory tree, hash it save to database")
        print("2.Show table and value hash")
        print("3.Add directory path in table")
        print("4.Delete directory path in table")
        print("5.Edit directory path in value")
        print("6.Exit")
        try:
            select = int(input("Please select number: "))
            if select == 1:
                database.drop_table('database.db')
                database.create_table('database.db')
                list_directory_tree_with_os_walk(os_path)
            elif select == 2:
                database.select_table('database.db')
            elif select == 3:
                path_add = input("Please input path: ")
                hash_path = hash_sha256(path_add.encode())
                database.insert_table("database.db",path_add,hash_path)
            elif select == 4:
                path_delete = input("Please input path: ")
                id_path = database.return_id('database.db',path_delete)
                database.delete_table('database.db',id_path)
            elif select == 5:
                id_update = input("Please input id path: ")
                path_update = input("Please input change: ")
                hash_update = hash_sha256(path_update.encode())
                database.update_table('database.db',path_update,hash_update,id_update)
            elif select == 6:
                break
        except ValueError:
            print("Please press number!!!!!")
            input("Press any key to continue")

    


def main():
    if len(argv) != 0:
        os_path = argv[1]
        menu(os_path)
    #create table 
    #database.create_table('database.db')
    #walking tree directory and hash save database
    #list_directory_tree_with_os_walk('D:\\F8-Band')
    #delete table by id
    #database.delete_table('database.db','2')
    #print table
    #database.select_table('database.db')
    #Update table
    #database.update_table('database.db',' C:\\Users\\Public\\NTUSER','asdasdsdasd','3')
    #database.select_table('database.db')
    #delete table
    #database.drop_table('database.db')
    #database.create_table('database.db')
    #list_directory_tree_with_os_walk('D:\\F8-Band')
    #database.select_table('database.db')
    #return id of name_path 
    # id_test = database.return_id('database.db', 'D:\\F8-Band\\assets')
    # print(id_test)

if __name__ == '__main__':
    main()
import os
import hashlib
import database
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



def main():
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
    id_test = database.return_id('database.db', 'D:\\F8-Band\\assets')
    print(id_test)

if __name__ == '__main__':
    main()
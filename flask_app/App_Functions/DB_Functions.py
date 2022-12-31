
class DB_Functions():

    def create_db_if_none():
        import mysql.connector
        cnx = mysql.connector.connect(user='root', password='sys12345', host='localhost', database='Budget_login_info')

        # Create a cursor
        cursor = cnx.cursor()

        # Create a database
        cursor.execute("CREATE DATABASE IF NOT EXISTS Budget_login_info ")
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTO_INCREMENT, username VARCHAR(255), password varbinary(1024), salt varbinary(1024))")

        cnx.commit()

        # Close the connection
        cnx.close()
    
    def hash_new_password(password):
        import os 
        import hashlib
          # Generate a random salt
        salt = os.urandom(16)
        
        # Hash the password and salt
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        
        # Return the hashed password and salt
        return hashed_password, salt

    def find_user_in_table(username):
        import mysql.connector
        cnx = mysql.connector.connect(user='root', password='sys12345', host='localhost', database='Budget_login_info')
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        result = cursor.fetchone()

        if result:
    # Return the result
            return result
        else:
            return None

    def check_if_pass_eq_hash(username, password):
        
        password_match = False
        
        import mysql.connector
        cnx = mysql.connector.connect(user='root', password='sys12345', host='localhost', database='Budget_login_info')
        cursor = cnx.cursor()

        result = DB_Functions.find_user_in_table(username)

        returned_username = result[1]
        returned_hashed_password = result[2]
        returned_salt = result[3]

        check_password = DB_Functions.hash_existing_password(password, returned_salt)

        if check_password == returned_hashed_password:
            password_match = True
            return password_match


    def hash_existing_password(password, salt):
        import os 
        import hashlib
          # Generate a random salt
        
        # Hash the password and salt
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        
        # Return the hashed password and salt
        return hashed_password
        

    def add_hash_pass_to_db(username, password):
        import mysql.connector

        hashed_password, salt = DB_Functions.hash_new_password(password)

        cnx = mysql.connector.connect(user='root', password='sys12345', host='localhost', database='Budget_login_info')
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO users (username, password, salt) VALUES (%s, %s, %s)", (username, hashed_password, salt))
        cnx.commit()
        cnx.close()

    def adm_hash(admin_code):
        import hashlib
          # Generate a random salt
        salt = b'\x87i\x17s2\x05?\x82\xd5\x8a\xbdA\xe5\x98\xec='
        
        # Hash the password and salt
        hashed_password = hashlib.pbkdf2_hmac('sha256', admin_code.encode(), salt, 100000)
        
        # Return the hashed password and salt
        return hashed_password


password_match, hashed_password = DB_Functions.check_if_pass_eq_hash('test1', 'test1')


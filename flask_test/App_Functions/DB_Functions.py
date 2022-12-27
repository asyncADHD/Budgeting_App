
class DB_Functions():

    def create_db_if_none():
        import mysql.connector
        cnx = mysql.connector.connect(user='root', password='sys12345', host='localhost', database='Budget_login_info')

        # Create a cursor
        cursor = cnx.cursor()

        # Create a database
        cursor.execute("CREATE DATABASE IF NOT EXISTS Budget_login_info ")
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTO_INCREMENT, username VARCHAR(255), password VARCHAR(255), salt VARCHAR(255))")

        cnx.commit()

        # Close the connection
        cnx.close()
    
    def hash_password(password):
        import os 
        import hashlib
          # Generate a random salt
        salt = os.urandom(16)
        
        # Hash the password and salt
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        
        # Return the hashed password and salt
        return hashed_password, salt

    def check_if_pass_eq_hash():
        pass

    def add_hash_pass_to_db(username, password):
        import mysql.connector

        salt, password = DB_Functions.hash_password(password)

        cnx = mysql.connector.connect(user='root', password='sys12345', host='localhost', database='Budget_login_info')
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO users (username, password, salt) VALUES (%s, %s, %s)", (username, hashed_password, salt))
        cnx.commit()
        cnx.close()

hashed_password, salt = DB_Functions.hash_password("password123")

        
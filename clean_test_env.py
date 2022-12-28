import os 
import hashlib
    # Generate a random salt
salt =  b'\x87i\x17s2\x05?\x82\xd5\x8a\xbdA\xe5\x98\xec=' 
password = '4299'

# Hash the password and salt
hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)

print ('\n'*3, salt, "\n"*3)
print ("password = ", hashed_password)

#b'y\x95eF\x829\xfe\x88v\xfdA\x89R\xcd\x18(m\x13\xfb\xc0\xb2\xd19Ho\xc74\x93\x0e^\xe6\xc6'
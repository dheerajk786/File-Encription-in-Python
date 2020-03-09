import os
from cryptography.fernet import Fernet

class function():
        def __init__(self):
            print("yayfunction")
            self.key=Fernet.generate_key()
        def encryption1(self,name):
            print("yay")
            with open('data/encrypteddata/'+name,'rb') as file:
                encoded=file.read()
                print(encoded)

            print("yayfunction")
        
            f=Fernet(self.key)
            encoded=f.encrypt(encoded)
            file=open("encryptedfile/"+"en_"+name,'wb')
            file.write(encoded)
            file.close()
            print(f'key={self.key.decode()}')
            return(self.key.decode())


        def decryption1(self,name,key):
            print("decryption starts 3")
            with open('data/decrypteddata/'+name,'rb') as file:
                 decode=file.read()
            f=Fernet(key)
            decoded=f.decrypt(decode)
            print(decoded)
            file=open('originaldata/'+name.replace("en_",""),'wb')
            file.write(decoded)
            file.close
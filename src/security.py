from  cryptography.fernet import Fernet

class security():
  
    def __init__(self):
      with open('key.txt', 'rb') as filekey:
        self.key = filekey.read()
      self.fernet = Fernet(self.key)

    def encrypt(self, message):
        return self.fernet.encrypt(message.encode())

    def decrypt(self, message):
        return self.fernet.decrypt(message).decode()
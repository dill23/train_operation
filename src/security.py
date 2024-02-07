from  cryptography.fernet import Fernet

class security():
  
    def __init__(self):
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

    def encrypt(self, message):
        return self.fernet.encrypt(message.encode())

    def decrypt(self, message):
        return self.fernet.decrypt(message).decode()
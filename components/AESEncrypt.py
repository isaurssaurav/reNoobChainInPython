from .utils import convert_to_sha256
from Crypto.Cipher import AES
import hashlib


class AESEncrypt:
    key = None
    nonce = {}

    def set_key(self, key):
        try:
            self.key = convert_to_sha256(key)
        except Exception as e:
            print('Error while setting key')
            print(e)

    def encrypt(self, data_str, secret_key):
        try:
            self.set_key(secret_key)
            cipher = AES.new(self.key, AES.MODE_EAX)
            cipher_text = cipher.encrypt(bytes(data_str, 'utf-8'))
            self.nonce[cipher_text] = cipher.nonce
            return cipher_text
        except Exception as e:
            print('Error while encrypting data')
            print(e)

    def decrypt(self, str_to_decrypt, secret_key):
        try:
            self.set_key(secret_key)
            cipher = AES.new(self.key, AES.MODE_EAX, nonce=self.nonce[str_to_decrypt])
            data = cipher.decrypt(str_to_decrypt)
            return data
        except Exception as e:
            print('Error while decrypting data')
            print(e)


from .utils import convert_to_sha256
from Crypto.Cipher import AES
import hashlib


class AESEncryptCBC:
    key = None

    def set_key(self, key):
        try:
            self.key = convert_to_sha256(key)
        except Exception as e:
            print('Error while setting key')
            print(e)

    def encrypt(self, data_str, secret_key):
        try:
            cipher = AES.new(secret_key.encode("utf8"), AES.MODE_CBC,'This is an IV456'.encode("utf8"))
            pad = b' '
            data_byte = data_str.encode('utf-8')
            length = 16 - (len(data_byte)%16)
            data_byte += length * pad
            cipher_text = cipher.encrypt(data_byte)

            return cipher_text
        except Exception as e:
            print('Error while encrypting data')
            print(e)

    def decrypt(self, str_to_decrypt, secret_key):
        try:
            cipher = AES.new(secret_key.encode("utf8"), AES.MODE_CBC,'This is an IV456'.encode("utf8"))
            data = cipher.decrypt(str_to_decrypt)
            return data
        except Exception as e:
            print('Error while decrypting data')
            print(e)


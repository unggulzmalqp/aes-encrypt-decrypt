from Crypto.Cipher import AES
from Crypto.Util import Padding
from base64 import b64encode, b64decode
from dotenv import load_dotenv
import os

load_dotenv()
passphrase = os.getenv('PASSPHRASE')
content = input('Encrypted:')

mode = AES.MODE_ECB
bs = 16

key = passphrase.encode('utf-8')
cipher = AES.new(key, mode)
content = b64decode(content.encode('utf-8'))
decrypted = Padding.unpad(cipher.decrypt(content), bs).decode('utf-8')
print(decrypted)

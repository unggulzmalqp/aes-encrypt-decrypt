from Crypto.Cipher import AES
from Crypto.Util import Padding
from base64 import b64encode, b64decode
from dotenv import load_dotenvs
import os

load_dotenv()
passphrase = os.getenv('PASSPHRASE')
content = input('Plain:')

mode = AES.MODE_ECB
bs = 16

key = passphrase.encode('utf-8')
body = Padding.pad(content.encode('utf-8'), bs)
cipher = AES.new(key, mode)
encrypted = b64encode(cipher.encrypt(body)).decode('utf-8')
print(encrypted)

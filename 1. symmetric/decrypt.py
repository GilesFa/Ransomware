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

with open("thekey.key", "rb") as key:
    secretkey = key.read()
# print(secretkey)

#讀取檔案內容並將其加密，在將加密的內容寫回檔案中
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    # print(contents)
    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)

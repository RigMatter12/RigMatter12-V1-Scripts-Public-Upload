from uuid import uuid4
from base64 import urlsafe_b64encode
from hashlib import sha1
from requests import post
from itertools import cycle
from random import choices

accountid = 31567236
playerid = 276938888
password = "INSERT ACTUAL PASSWORD HERE"
seed2 = "".join(choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",k=5))
levels = "1,128,666,124617122"
listname = "Pasta la vista"
description = "bmpiYmpramhidmprampodmxrbmJqd2FqYWphd2xqYXdrYmphZndia2p1d2Fma2JqdWFmd2xmYWxpamFmbG5qd2Fia3dhbmx3YWp3YWJqd2Fia3dhaXNhaWphbG5ha2JqY3Nhbmphc2lqaHdhZm9paHdhZmliYXdrZmpid3NhanVrYndzYWtjZmlid2FmaWt3c2FoZm93YWJmaWt3YWJmd2FiZmxraWFiZmxpa3dzYWZibG9rYWl3Zm5od2FpaHdhb2lobndha2ViaXdhYmZvYWhuaWx3ZmJhbHdpZmJvd2Fmbm93YWZid2FsZmJpd2Fvd2FqZm93YWpmd2lhaXdhYml3YmFpd2JhZml3aXdhZmh3YWl3YWliaXdhaGZpd2FoZml3YWhmaWFvYWp3"

def generatechk(values):
    def xorcipher(string, key) :
        return "".join(chr(ord(x) ^ ord(y)) for (x, y) in zip(string, cycle(key)))
    key = seed2
    salt = str(accountid)
    string = values+salt
    hashed = sha1(string.encode()).hexdigest()
    xored = xorcipher(hashed, key)
    final = urlsafe_b64encode(xored.encode()).decode()
    return final

payload = {
    "accountID": accountid,
    "binaryVersion": 45,
    "difficulty": 10,
    "gameVersion": 22,
    "gjp2": sha1((password + "mI29fmAnxgTs").encode()).hexdigest(),
    "listDesc": urlsafe_b64encode(description),
    #"listID": 860765,
    "listLevels": levels,
    "listName": listname,
    "listVersion": -1,
    "original": 24,
    "secret": "Wmfd2893gb7",
    "seed": generatechk(levels),
    "seed2": seed2,
    "udid": uuid4(),
    "unlisted": 0,
    "uuid": playerid
}

print(post("https://www.boomlings.com/database/uploadGJLevelList.php",data=payload,headers={"User-Agent":""}).text)
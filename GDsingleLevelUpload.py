from requests import post
from hashlib import sha1
from base64 import urlsafe_b64encode
from uuid import uuid4
from random import choices
from itertools import cycle

def generate_upload_seed(data: str, chars: int = 50) -> str:
    # GD currently uses 50 characters for level upload seed
    if len(data) < chars:
        return data  # not enough data to generate
    step = len(data) // chars
    return data[::step][:chars]

def generate_chk(values) :

    def xorcipher(string, key) :

        return "".join(chr(ord(x) ^ ord(y)) for (x, y) in zip(string, cycle(key)))
    
    values.append("xI25fpAapCQg")

    string = ("").join(map(str, values))

    hashed = sha1(string.encode()).hexdigest()
    xored = xorcipher(hashed, "41274")
    final = urlsafe_b64encode(xored.encode()).decode()

    return final

password = "MyPassword" #replace with password
levelstring = "H4sIAAAAAAAACq2TUc7CQAiEL4QJA2y7jU-ewQNwAK_wH95lpyY-1KjxfyjTLsO3QNLb1bsgQ9MS1tLTWkuAYhQeRp6QS0JVc00kWoWemj3xh5wItc8Q-B2xHSLKw4KPIJZVfwT6aiXj-3dGHDKq_DGQvhunvRzny70s_wU6GkpuF7hoSaMslJAR-b7OaHueX-glV9-Ym5GcmbjEjMxCaaLLaDM6bBWUXSmg2BQjykhx5pw5Z2tBWBAWjeXMudMZFLbvvK_-tJJtCvYpWGd7u2DzQ86QLiY2VjCY45I2nv3Q4_lQRlVt-nwHIYjhqs0DAAA=" #replace with actual Level String


#change values accordingly
data = {
    "gameVersion" : 22,
    "binaryVersion" : 45,
    "accountID": 31567236,
    "audioTrack": -666, #Set to 0 for NewGrounds
    "auto": 0,
    "coins": 9,
    "gjp2": sha1((password+"mI29fmAnxgTs").encode()).hexdigest(),
    "ldm": 1,
    "levelDesc": urlsafe_b64encode(b"Level Uploaded Remotely! Check Stats!").decode(),
    "levelID": 0, #Set to Level ID of Previously updated Level
    "levelInfo": "",
    "levelLength": 5,
    "levelName": "Hello from Python", #Needs to be the same as previously updated Level if not new
    "levelString": levelstring,
    "levelVersion": -69,
    "objects": -999,
    "original": 128,
    "password": 123123, #Works if gameVersion < 22
    "requestedStars": 69,
    "secret": "Wmfd2893gb7",
    "seed": str(choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", k=10)),
    "seed2": generate_chk(generate_upload_seed(levelstring)),
    "songID": 0, #0 for Official Song, NewGrounds ID if not
    "ts": 0,
    "twoPlayer": 1,
    "udid": uuid4(),
    "unlisted": 0,
    "userName": "TheRigMatter176",
    "uuid": 276938888,
    "wt": 999999,
    "wt2": 999999,
}

#uploads the Level
response = post(url="https://www.boomlings.com/database/uploadGJLevel21.php",data=data,headers={"User-Agent":""}).text
print(response) #121922751
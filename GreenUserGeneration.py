from requests import post
from uuid import uuid4 #random UDID (uuid4 is UUIDv4)

#You can only generate 1 Green User per IP per Hour (not 100% exact and may become outdated)
endpoint = "https://www.boomlings.com/database/updateGJUserScore22.php" #updateGJUserScore22.php is used to generate Green Users

payload = { #No AccountID/GJP2 (in 2.1, AccountID and GJP just empty Strings -> "")
    "accBall": 1,
    "accBird": 1,
    "accDart": 1,
    "accExplosion": 1,
    "accGlow": 0,
    "accIcon": 1,
    "accJetpack": 1,
    "accRobot": 1,
    "accShip": 1,
    "accSpider": 1,
    "accSwing": 1,
    "binaryVersion" : 45,
    "coins": 0,
    "color1": 0,
    "color2": 3,
    "color3": 0,
    "demons": 0,
    "diamonds": 0,
    "gameVersion" : 22,
    "icon": 1,
    "iconType": 0,
    "moons": 0,
    "secret": "Wmfd2893gb7",
    "seed": "ARAyXb2tSo",
    "seed2": "WQMAAlAIAgNVAABQUw5VWQYDAAENDQUHU1lWBANQAFABAwQIVAIPAg==", #AccountID set as 0 (if consistent to other Endpoints) but seed2 works as long as Stats remain the same for every UDID
    "special": 0,
    "stars": 0,
    "udid": uuid4(), #Anything can be sent as an UDID but uuid4() is realistic. (WARNING a Green User's UDID is like an Account's Password!)
    "userCoins": 0,
    "userName": "Player", #Username can be any but "Player" is default
    "uuid": 0 #UUID : 0 = New Green User if UDID hasn't been used yet, else return PlayerID of existing Green User. (set to Green User's UUID/UDID if modifying existing one)
} #You need to generate a custom seed2 if you change anything besides the Seed, Username or UDID!

#Response will either be the PlayerID of the new Green User, or the PlayerID of an existing one or -1 if failed or a different Error, like Cloudflare
greenUserUUID = post(url=endpoint,data=payload,headers={"User-Agent": ""}).text

try :

    if int(greenUserUUID) != -1 :
        print(f"Generated Green User -> UDID : {payload["udid"]}, PlayerID/UUID : {greenUserUUID}") #Prints UDID,UUID (same as Password,AccountID for an Account)
        #If success, store the Green User's UDID and UUID. UUID is PlayerID and UDID is the Device ID, which acts as the Green User's Password/Authentication Method!
    else :
        print(f"Failed to generate Green User, Code : {greenUserUUID}")

except ValueError :

    print(f"Failed to generate Green User, Code : {greenUserUUID}")
#End (only 1 Request)

#Example Response if Successful =>
#Generated Green User -> UDID : 8d6e1cda-64eb-4886-a4ed-19c9c4fdf07e, PlayerID/UUID : 300021499

#Example Response if Failed =>
#Failed to generate Green User, Code : -1
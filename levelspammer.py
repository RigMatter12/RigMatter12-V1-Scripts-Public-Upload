from requests import post
from random import randint,choice
from hashlib import sha1
from time import sleep
from base64 import urlsafe_b64encode
from uuid import uuid4

possibleletters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
threadslist = []

youtubernamelist = ["juniper", "mulpan", "evw", "zeronium", "zoink", "npesta", "robtop", "advy", "viprin", "riot", "vortrox", "partition", "lemoncak", "dorami", "tride", "doggie", "aeonair", "moldy", "kaiguy"]
levelnames = ["bloodbath", "sonic wave", "bloodlust", "tidal wave", "grief", "cataclysm", "nine circles"]
songidlist = ["1163222", "467339", "508568", "905108", "889238", "810618", "739991", "709578", "467267", "834447", "759779", "725417", "574484", "473413", "498828", "1299929", "1312401", "1231705", "638150", "598349", "1208034", "1022489", "1020889", "713190", "747953", "1221621", "1217015"]

def getproxies() :

    try :
            
        with open("proxies.txt", "r") as proxies :

            return [line.strip() for line in proxies]
        
    except FileNotFoundError :

        print("Proxy file 'proxies.txt' not found!")

        return False

def getaccounts() :

        try :
                
            with open("accounts.txt", "r") as accountsfile :

                return [line.strip() for line in accountsfile]
            
        except FileNotFoundError :

            print("Proxy file 'accounts.txt' not found!")

            return False

def spamlevel(threadgroup, accountgroup, thread) :

    global possibleletters, levelnames, youtubernamelist, songidlist

    proxy = threadgroup[thread]
    account = accountgroup[thread]

    try :

        randnum = randint(1,10)
        randnum2 = randint(1,5)

        if randnum == 1 :
            item = choice(youtubernamelist) + " challenge"
        elif randnum == 2 :
            item = "wave challenge " + choice(("hard", "easy", "new", "demon"))
        elif randnum == 3 :
            item = "wave challenge " + str(randint(1, 10))
        elif randnum == 4 :
            item = "shitty " + choice(levelnames)
        elif randnum == 5 :
            item = choice(levelnames) + " easy"
        elif randnum == 6 :
            item = choice(levelnames) + " noclip"
        elif randnum == 7 :
            item = "evw impossible 2p2"
        elif randnum == 8 :
            item = "Unnamed " + str(randint(0,20))
        elif randnum == 9 :
            item = choice(("challenge", "impossible", "extreme demon", "top 1"))
        elif randnum == 10 :
            item = "silent " + choice(levelnames)

        if randnum2 == 1 :

            songid = 0
            audiotrack = randint(1, 21)

        else :

            songid = choice(songidlist)
            audiotrack = 0

        username, password, accountID, playerID = account.split(",")

        data = {

            "accountID": accountID,
            "audioTrack": audiotrack,
            "auto": 0,
            "binaryVersion": 45,
            "coins": randint(0,3),
            "gameVersion": 22,
            "gjp2": sha1((password+"mI29fmAnxgTs").encode()).hexdigest(),
            "ldm": randint(0,1),
            "levelDesc": urlsafe_b64encode(b"!!! IMPORTANT !!! Join https://discord.gg/FZm4HuVcaW And Subscribe to RigMatter12 on YouTube!").decode(),
            "levelID": 0,
            "levelInfo": "",
            "levelLength": randint(1,5),
            "levelName": str(item),
            "levelString": "H4sIAAAAAAAACq2X3U_bMBDA_6Ew2Wc7jjXxwCRKiwBpLbSjL1abTKNfiBeQOu2PX5JziCm5SxE8kGv8s8_3ZV_YTFSWSK-FBy_BeOXBGC8lCkCBg9qfSJ96KYTw1ksvTfXIvPCZl_-kr1UIOE6F_LwK16mimoMLjlICvlrfpehDISnfP69Df4VDhnTog4rSr1LU5VayOZMqEZUwKFIUOimf-NvWTwgc32RWiYlyyOon6qnBma6fSKXASTgLcBrgDLCJrKYLFBIF1AJQFaAWhUwhU2iaRmUalWmDy5EphTM1CjRf4X7VWauEq4UMXuA6COZKNL4U32WSJZBAZpJSZ7mJKf_CoFXxYFKuqiJdQleG8HWNQA5J6cVk556Wqx_ni18366W63IwGN9v8cb7NV-enB-tss0xWsfhWvlXBKGWpZjEci3x4nV7t3aZRdbUrHq_EfLG8HY-K6Xx9P81blcHS2JQ7NV3lcLNfzC63owv3PBpsX4rpWN7v7h4O1h1piipU_vx75mQxnK7mE7Negnj5Obh8mgv5UAzH23x9vm-9hEpBot_qlkG3rE3cbR9vZwNRXEz317ejPwUM_o4uHrb57u40pMCUBdaZAllvUe1wIh2BDY8zFivNYi14rHic8tix2PCOGd6xVPI4-J0S2LLYKhJnqqqC4JkgeJMUijdhJ3naw3v2N9DDTQ8P9iuCN9ElueU5E1-IwtuxHKIDQ2HaeKgvFR7TrtWY9gyixFI4PQp3pAX4rAOfdOBzDlHKCdwcNwprHmPUbDe1gqXqCKrf0-r2zg5CEoYtHci2nfThDoM064xmA6HbFBHOhPRTNGUpGSYr2wPXYZaNe0xHQGrOHCkbNyGKM6fGxm2I5PSxsnEjorihLxQbtyKKM9dhzW2Pf0w91vywjN98w7Hpi3Hf8i7zXPyBQnJzHO-47V1cXhRvyovkdK93cfmQ3PG8KQ-S9_hnevxjysfFHysUZ8rL9ZSXO6a8AqfKy5L3EmLyYopx578n0V3Mp45STl-KcWFQONQd5Xco2y4s2tWN8tdhS-4peIsF769gG0iMKYsN71BKh0O0VUxisvPVmG6biMmei5ipcBFVeMcJkRBdcbZNVhgnA4r8IMnvOZlt5KHz0Zys0MDJcgmcrBfk4WqjeY__oWRIHoqC5j3xofh_r2wOUYwUAAA=",
            "levelVersion": randint(1,10),
            "objects": randint(100,100000),
            "original": 0,
            "password": 0,
            "requestedStars": randint(1,10),
            "secret": "Wmfd2893gb7",
            "seed": "xf0NLh8xm0",
            "seed2": "UQIGUgMFAgZTUVVVVFUNBAADVlBRUAEHB1JUCgIDAwQLVVEEBlNSVw==",
            "songID": songid,
            "ts": 0,
            "twoPlayer": 0,
            "udid": uuid4(),
            "unlisted": 0,
            "userName": username,
            "uuid": playerID,
            "wt": randint(10000,100000),
            "wt2": randint(10000,100000)

        }

        try :

            spamrequest = post(
                
                url="https://www.boomlings.com/database/uploadGJLevel21.php",
                data=data,
                headers={"User-Agent":""},
                proxies={"http":proxy,"https":proxy},
            
            )

            if spamrequest.text != "-1" :

                print(f"Uploaded Level : {spamrequest.text}")

            else :

                print(spamrequest.text)
            
        except Exception as Error :

            print(f"There was an Error : {Error}")

    except Exception as Error :

        print(f"There was an Error : {Error}")

if __name__ == "__main__" :

    try :

        while True :

            command = input("Press '0' to exit or '1' to start : ")

            if command == "0" :

                break

            elif command == "1" :

                accounts = getaccounts()
                proxies = getproxies()
                minlength = min(len(accounts), len(proxies))
                accounts = accounts[:minlength]
                proxies = proxies[:minlength]

                while True :

                    try :
                        
                        for index, account in enumerate(accounts) :

                            try :
                                
                                spamlevel(proxies,accounts,index)
                                sleep((3600)/(len(accounts)*5))

                            except :

                                pass

                    except :

                        pass

            else :

                print("Invalid action!")
    
    except Exception as Error :

        print(f"there was an Error : {Error}")
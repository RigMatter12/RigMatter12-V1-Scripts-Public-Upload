from requests import post
from threading import Thread
from random import randint, choices
from hashlib import sha1
from base64 import urlsafe_b64encode
from itertools import cycle
from time import sleep

from GDgetUserInfos import getUserIDs

possibleletters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

likes = 0
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

            print("Account file 'accounts.txt' not found!")

            return False

def distributeproxies(proxies, threads, max) :

    proxygroups = list([] for _ in range(threads))

    for index, proxy in enumerate(proxies[:max]):
            
        proxygroups[index % threads].append(proxy)

    return proxygroups

def distributeaccounts(accounts, threads, max) :

    accountgroups = list([] for _ in range(threads))

    for index, account in enumerate(accounts[:max]):

        accountgroups[index % threads].append(account)

    return accountgroups

def generate_rs() :

    return ("").join(choices(possibleletters, k=10))

def generate_chk(values) :

    def xorcipher(string, key) :

        return "".join(chr(ord(x) ^ ord(y)) for (x, y) in zip(string, cycle(key)))
    
    values.append("ysg6pUrtjn0J")

    string = ("").join(map(str, values))

    hashed = sha1(string.encode()).hexdigest()
    xored = xorcipher(hashed, "58281")
    final = urlsafe_b64encode(xored.encode()).decode()

    return final

def likeThreadFunc(itemID, threadgroups, accountgroups, thread, type, like, special) :

    global likes

    try :

        proxygroup = threadgroups[thread]
        accountgroup = accountgroups[thread]

        if proxies != False :

            for index, account in enumerate(accountgroup) :

                downloadurl = "https://www.boomlings.com/database/likeGJItem211.php"

                udid = "S15" + str(randint(100000, 100000000)) + str(randint(100000, 100000000)) + str(randint(100000, 100000000)) + str(randint(100000, 100000000))
                randomproxy = proxygroup[index]

                userdata = account.split(",")

                if len(userdata) == 4 :

                    username, password, accountID, playerID = account.split(",")

                elif len(userdata) == 2 :

                    username, password = account.split(",")
                    accountID, playerID = getUserIDs(username=username)

                else :

                    username = userdata[0]
                    password = userdata[1]
                    accountID, playerID = getUserIDs(username=username)
                
                gjp = sha1((password + "mI29fmAnxgTs").encode()).hexdigest()
                
                rs = generate_rs()

                chkvalues = [special, itemID, like, type, rs, accountID, udid, playerID]

                proxy = {

                    "http" : randomproxy,
                    "https" : randomproxy,

                }

                headers = {

                    "User-Agent": "",

                }

                data = {
                    
                    "gameVersion" : "22",
                    "binaryVersion" : "42",
                    "gdw" : "0",
                    "itemID" : itemID,
                    "accountID" : accountID,
                    "gjp2" : gjp,
                    "special" : special,
                    "rs" : rs,
                    "type" : type,
                    "like" : like,
                    "udid" : udid,
                    "uuid" : playerID,
                    "chk" : generate_chk(values=chkvalues),
                    "secret" : "Wmfd2893gb7",

                }

                try :

                    if likes >= desiredlikes :

                        return

                    likerequest = post(
                        
                        url=downloadurl,
                        data=data,
                        headers=headers,
                        proxies=proxy,
                    
                    )

                    sleep(1)
                        
                    if likerequest.text != "-1" :
                        
                        likes += 1

                        if int(like) == 0 :

                            print(f"Sent dislike, Current dislikes : {likes}")

                        elif int(like) == 1 :

                            print(f"Sent like, Current likes : {likes}")

                    else :

                        print(f"Error code : {likerequest.text}, Faulty Account : {username}")
                        
                    if likes >= desiredlikes :

                        return

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

                while True :

                    itemID = input("what is the ItemID : ")

                    try :

                        int(itemID)
                        break

                    except ValueError :
                        
                        if not itemID.startswith("-") :

                            print("Invalid ItemID")

                        else :

                            break

                proxies = getproxies()
                accounts = getaccounts()

                maxlen = min(len(accounts), len(proxies))

                if proxies != False and accounts != False :

                    while True :

                        desiredlikes = input(f"How many likes (max {maxlen} for this item!) : ")

                        try :

                            int(desiredlikes)

                            if int(desiredlikes) > maxlen :

                                print("desired likes are greater than the max amount!")

                            elif int(desiredlikes) < 1 :

                                print("too little desired likes!")

                            else :

                                break

                        except ValueError :

                            print("Invalid value")
                    
                    while True :

                        like = input(f"type -> '1' for like or '0' for dislike : ")

                        try :

                            int(like)

                            if int(like) > 1 or int(like) < 0 :

                                print("Invalid type value!")

                            else :

                                break

                        except ValueError :

                            print("Invalid value")

                    while True :

                        type = input(f"type -> '1' for level, '2' for comment, '3' for account post or '4' for list : ")

                        try :

                            int(type)

                            if int(type) < 1 or int(type) > 4 :

                                print("Invalid type!")

                            else :

                                break

                            if int(type) == 4 :

                                if not itemID.startswith("-") :

                                    itemID = "-" + itemID

                        except ValueError :

                            print("Invalid value")

                    if int(type) == 1 or int(type) == 4 :

                        special = "0"

                    elif int(type) == 2 :

                        while True :

                            levelID = input("LevelID of the level in which the comment was posted on : ")

                            try :

                                int(levelID)
                                break

                            except ValueError :

                                print("Invalid input")

                        special = levelID

                    elif int(type) == 3 :

                        while True :
                            
                            targetUsername = input("Target Person's username : ")
                            targetAccountID, targetPlayerID = getUserIDs(username=targetUsername)

                            if targetAccountID != False and targetPlayerID != False :

                                break

                            else :

                                print("Invalid username")

                        special = targetAccountID

                    while True :

                        threads = input(f"How many Threads (max : {maxlen}) : ")

                        try :

                            int(threads)

                            if int(threads) < 1 or int(threads) > maxlen :

                                print("Invalid thread amount")

                            else :

                                break

                        except Exception :

                            print("Invalid input")
                    
                    desiredlikes = int(desiredlikes)
                    proxiegroups = distributeproxies(proxies=proxies, threads=int(threads), max=desiredlikes)
                    accountgroups = distributeaccounts(accounts=accounts, threads=int(threads), max=desiredlikes)

                    for index in range(int(threads)) :
                        
                        thread = Thread(target=likeThreadFunc, args=(itemID,proxiegroups,accountgroups,index,type,like,special))
                        threadslist.append(thread)

                    for thread in threadslist :

                        thread.start()

                    for thread in threadslist :

                        thread.join()
                    
                    threadslist.clear()
                    likes = 0
                
                else :

                    print("Proxies unavailable!")

            else :

                print("Invalid input")
    
    except Exception as Error :

        print(f"there was an Error : {Error}")
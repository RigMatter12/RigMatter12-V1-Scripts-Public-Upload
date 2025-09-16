from requests import post
from threading import Thread
from random import randint
from hashlib import sha1

from GDgetUserInfos import getUserIDs

possibleletters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

demonRates = 0
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

def likeThreadFunc(demonrate, levelID, threadgroups, accountgroups, thread, rates) :

    global demonRates

    try :

        proxygroup = threadgroups[thread]
        accountgroup = accountgroups[thread]

        if proxies != False :

            for index, account in enumerate(accountgroup) :

                downloadurl = "https://www.boomlings.com/database/rateGJDemon21.php"

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

                proxy = {

                    "http" : randomproxy,
                    "https" : randomproxy,

                }

                headers = {

                    "User-Agent": "",

                }

                data = {

                    "accountID": accountID,
                    "gjp2": gjp,
                    "levelID": levelID,
                    "rating": demonrate,
                    "secret": "Wmfp3879gc3",
                    "udid": udid,
                    "uuid": playerID

                }

                try :

                    if demonRates >= rates :

                        return

                    raterequest = post(
                        
                        url=downloadurl,
                        data=data,
                        headers=headers,
                        proxies=proxy,
                    
                    )

                    if raterequest.text == "1" :
                        
                        demonRates += 1

                        print(f"Sent demon rate, Current demon rates : {demonRates}")
                            
                    if demonRates >= rates :

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

                    levelID = input("what is the LevelID : ")

                    try :

                        int(levelID)
                        break

                    except ValueError :
                        
                        print("Invalid levelID")

                proxies = getproxies()
                accounts = getaccounts()

                maxlen = 0

                if len(accounts) > len(proxies) :

                    maxlen = len(proxies)

                else :

                    maxlen = len(accounts)

                if proxies != False and accounts != False :

                    while True :

                        demonrate = input(f"what demon rate (1-5 easy, medium...) : ")

                        try :

                            int(demonrate)

                            if int(demonrate) > 5 or int(demonrate) < 1 :

                                print("invalid demon rate!")

                            else :

                                break

                        except ValueError :

                            print("Invalid value")

                    while True :

                        rates = input(f"How many demon rates (max {len(accounts)} for this item! {maxlen} per hour!) : ")

                        try :

                            int(rates)

                            if int(rates) > maxlen :

                                print("desired demon rates are greater than the max amount!")

                            elif int(rates) < 1 :

                                print("too little desired demon rates!")

                            else :

                                break

                        except ValueError :

                            print("Invalid value")

                    while True :

                        threads = input("How many Threads : ")

                        try :

                            int(threads)
                            break

                        except Exception :

                            print("Invalid input")
                    
                    demonrate = int(demonrate)
                    rates = int(rates)
                    proxiegroups = distributeproxies(proxies=proxies, threads=int(threads), max=rates)
                    accountgroups = distributeaccounts(accounts=accounts, threads=int(threads), max=rates)

                    for index in range(int(threads)) :
                        
                        thread = Thread(target=likeThreadFunc, args=(demonrate,levelID,proxiegroups,accountgroups,index,rates))
                        threadslist.append(thread)
                        thread.start()

                    for thread in threadslist :

                        thread.join()

                    demonRates = 0 
                
                else :

                    print("Proxies unavailable!")

            else :

                print("Invalid input")
    
    except Exception as Error :

        print(f"there was an Error : {Error}")
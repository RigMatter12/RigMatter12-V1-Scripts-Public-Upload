from requests import post
from threading import Thread
from random import randint

views = 0
threadslist = []

def getproxies() :

    try :
            
        with open("proxies.txt", "r") as proxies :

            return [line.strip() for line in proxies]
        
    except FileNotFoundError :

        print("Proxy file 'proxies.txt' not found!")

        return False

def distributeproxies(proxies, threads, max) :

    proxygroups = list([] for _ in range(threads))

    for index, proxy in enumerate(proxies[:max]):

        proxygroups[index % threads].append(proxy)

    return proxygroups

def viewThreadFunc(itemID, threadgroups, thread, mode) :

    global views

    try :

        proxygroup = threadgroups[thread - 1]

        if proxies != False :

            for randomproxy in proxygroup :

                downloadurl = "https://www.boomlings.com/database/downloadGJLevel22.php"
                downloadlisturl = "https://www.boomlings.com/database/getGJLevels21.php"

                udid = "S15" + str(randint(100000, 100000000)) + str(randint(100000, 100000000)) + str(randint(100000, 100000000)) + str(randint(100000, 100000000))

                proxy = {

                    "http" : randomproxy,
                    "https" : randomproxy,

                }

                headers = {

                    "User-Agent": "",

                }

                leveldata = {
                    
                    "levelID" : itemID,
                    "inc" : 1,
                    "extras" : 0,
                    "udid" : udid,
                    "secret" : "Wmfd2893gb7",

                }

                listdata = {

                    "str": itemID,
                    "inc": 1,
                    "type": 25,
                    "udid": udid,
                    "secret": "Wmfd2893gb7",

                }

                try :

                    if int(mode) == 1 :

                        downloadrequest = post(
                            
                            url=downloadurl,
                            data=leveldata,
                            headers=headers,
                            proxies=proxy,
                        
                        )

                    elif int(mode) == 2 :

                        downloadrequest = post(
                            
                            url=downloadlisturl,
                            data=listdata,
                            headers=headers,
                            proxies=proxy,
                        
                        )
                    
                    if views >= desiredviews :

                        return

                    if downloadrequest.text != "-1" :
                        
                        views += 1
                        print(f"Sent View, Current Views : {views}")

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

                    itemID = input("what is the itemID : ")

                    try :

                        int(itemID)
                        break

                    except ValueError :

                        print("Invalid itemID")

                while True :

                    mode = input("what is the mode -> '1' for level, '2' for list : ")

                    try :

                        int(mode)

                        if int(mode) > 2 or int(mode) < 1 :

                            print("Invalid value")

                        else :

                            break

                    except ValueError :

                        print("Invalid mode")

                proxies = getproxies()

                if proxies != False :

                    while True :

                        desiredviews = input(f"How many views (max {len(proxies)} per hour!) : ")

                        try :

                            int(desiredviews)

                            if int(desiredviews) > len(proxies) :

                                print("desired views are greater than the max amount!")

                            elif int(desiredviews) < 1 :

                                print("too little desired views!")

                            else :

                                break

                        except ValueError :

                            print("Invalid value")

                    while True :

                        threads = input(f"How many Threads (max {len(proxies)}) : ")

                        try :

                            int(threads)

                            if int(threads) < 1 or int(threads) > len(proxies) :

                                print("Invalid thread amount")

                            else :

                                break

                        except Exception :

                            print("Invalid input")
                    
                    desiredviews = int(desiredviews)
                    itemID = int(itemID)
                    proxiegroups = distributeproxies(proxies=proxies, threads=int(threads), max=desiredviews)

                    for index, thread in enumerate(range(int(threads))) :
                        
                        thread = Thread(target=viewThreadFunc, args=(itemID,proxiegroups,index,mode))
                        threadslist.append(thread)

                    for thread in threadslist :

                        thread.start()

                    for thread in threadslist :

                        thread.join()

                    threadslist.clear()
                    views = 0
                
                else :

                    print("Proxies unavailable!")

            else :

                print("Invalid input")
    
    except Exception as Error :

        print(f"there was an Error : {Error}")
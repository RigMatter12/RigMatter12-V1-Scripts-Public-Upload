from requests import post
from threading import Thread

reports = 0
threadslist = []

def getproxies() :

    try :
            
        with open("proxies.txt", "r") as proxies :

            return [line.strip() for line in proxies]
        
    except FileNotFoundError :

        print("Proxy file 'proxies.txt' not found!")

        return False

def distributeproxies(proxies, threads) :

    proxygroups = list([] for _ in range(threads))

    for index, proxy in enumerate(proxies):

        proxygroups[index % threads].append(proxy)

    return proxygroups

def viewThreadFunc(levelID, threadgroups, thread) :

    global reports

    try :

        proxygroup = threadgroups[thread - 1]

        if proxies != False :

            for randomproxy in proxygroup :

                downloadurl = "https://www.boomlings.com/database/reportGJLevel.php"

                proxy = {

                    "http" : randomproxy,
                    "https" : randomproxy,

                }

                headers = {

                    "User-Agent": "",

                }

                data = {

                    "levelID": levelID,
                    "secret": "Wmfd2893gb7"
                    
                }

                try :

                    downloadrequest = post(
                        
                        url=downloadurl,
                        data=data,
                        headers=headers,
                        proxies=proxy,
                    
                    )
                    
                    if reports >= desiredreports :

                        return

                    if downloadrequest.text != "-1" :
                        
                        reports += 1
                        print(f"Sent report, Current reports : {reports}")

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

                        print("Invalid LevelID")

                proxies = getproxies()

                if proxies != False :

                    while True :

                        desiredreports = input(f"How many reports (max {len(proxies)} per hour!) : ")

                        try :

                            int(desiredreports)

                            if int(desiredreports) > len(proxies) :

                                print("desired reports are greater than the max amount!")

                            elif int(desiredreports) < 1 :

                                print("too little desired reports!")

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
                    
                    proxiegroups = distributeproxies(proxies=proxies, threads=int(threads))

                    desiredreports = int(desiredreports)
                    levelID = int(levelID)

                    for index, thread in enumerate(range(int(threads))) :
                        
                        thread = Thread(target=viewThreadFunc, args=(levelID,proxiegroups,index))
                        threadslist.append(thread)
                        thread.start()

                    for thread in threadslist :

                        thread.join()

                    views = 0
                
                else :

                    print("Proxies unavailable!")

            else :

                print("Invalid input")
    
    except Exception as Error :

        print(f"there was an Error : {Error}")
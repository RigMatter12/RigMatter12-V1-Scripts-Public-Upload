from requests import get
from json import loads
from threading import Thread

with open("proxies.txt") as proxyfile :

    proxies = [line.strip() for line in proxyfile]

def distributeproxies(proxies,threads,max) :

    proxygroups = list([] for _ in range(threads))

    for index, proxy in enumerate(proxies[:max]):

        proxygroups[index % threads].append(proxy)

    return proxygroups

def getModDownloads(modid) :

    jsonresponse = loads(get(f"https://api.geode-sdk.org/v1/mods/{modid}").text)

    try :

        return jsonresponse["payload"]["download_count"]
    
    except :

        return "FAILED TO GET DOWNLOADS!"

def sendDownloads(modid,modversion,proxygroup) :

    for proxy in proxygroup :

        try:

            get(f"https://api.geode-sdk.org/v1/mods/{modid}/versions/{modversion}/download",proxies={"http":proxy,"https":proxy},timeout=15)
            print("Sent Download!")

        except :

            print("Failed to send Download!")

while True :

    try :

        modid = input("Mod's ID : ").lower()
        modversion = input("Mod's Version : ")

        while True :

            downloadamount = input(f"How many Downloads (max {len(proxies)}) : ")

            try :

                downloadamount = int(downloadamount)

                if downloadamount > len(proxies) or downloadamount < 1 :

                    print("Invalid Download Amount!")

                else :

                    break

            except ValueError :

                print("Download Amount should be a Number!")

        while True :

            threads = input(f"How many Threads (max {downloadamount}) : ")

            try :

                threads = int(threads)
                if threads < 1 or threads > downloadamount :

                    print("Invalid Thread Amount")

                else :

                    break

            except ValueError :

                print("Threads should be a Number!")

        print(f"Mod Downloads : {getModDownloads(modid)}")
        threadlist = [Thread(target=sendDownloads,args=(modid,modversion,proxygroup))for proxygroup in distributeproxies(proxies,threads,downloadamount)]

        for thread in threadlist :

            thread.start()

        for thread in threadlist :

            thread.join()

        print(f"Mod Downloads : {getModDownloads(modid)}")

    except Exception as error :

        print(f"There was an Error : {error}")
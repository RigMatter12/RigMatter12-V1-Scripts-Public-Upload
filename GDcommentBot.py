from requests import post
from threading import Thread
from hashlib import sha1
from base64 import urlsafe_b64encode
from itertools import cycle
from time import sleep
from random import choice, randint

def getaccounts() :

    try :
            
        with open("accounts.txt", "r") as accountsfile :

            return [line.strip() for line in accountsfile]
        
    except FileNotFoundError :

        print("Proxy file 'accounts.txt' not found!")

        return False
    
def getproxies() :

    try :
            
        with open("proxies.txt", "r") as proxies :

            return [line.strip() for line in proxies]
        
    except FileNotFoundError :

        print("Proxy file 'proxies.txt' not found!")

        return False

def generatechk(values):

    def xorcipher(string, key) :

        return "".join(chr(ord(x) ^ ord(y)) for (x, y) in zip(string, cycle(key)))

    key = "29481"
    salt = "xPT6iUrtws0J"

    values.append(salt)

    string = ("").join(map(str, values))

    hashed = sha1(string.encode()).hexdigest()
    xored = xorcipher(hashed, key)
    final = urlsafe_b64encode(xored.encode()).decode()

    return final

def distributegroup(group, threads, max) :

    accountgroups = list([] for _ in range(threads))

    for index, account in enumerate(group[:max]):

        accountgroups[index % threads].append(account)

    return accountgroups

def PostComment(accounts, proxies, encodedmessage, levelid, percentage, thread) :

    commentPosturl = "https://www.boomlings.com/database/uploadGJComment21.php"

    headers = {

        "User-Agent" : ""

    }

    proxygroup = proxies[thread]
    accountgroup = accounts[thread]

    if accounts != False and proxies != False :

        while True :

            for index, account in enumerate(accountgroup) :
                
                try :
                    
                    username, password, accountID, playerID = account.split(",")

                    gjp = sha1((password + "mI29fmAnxgTs").encode()).hexdigest()

                    udid = "S15" + str(randint(100000,100000000)) + str(randint(100000,100000000)) + str(randint(100000,100000000)) + str(randint(100000,100000000))

                    chk = generatechk(values=[username, encodedmessage, levelid, percentage, "0"])

                    randomproxy = proxygroup[index]

                    commentpayload = {

                        "accountID" : accountID,
                        "gjp2" : gjp,
                        "userName" : username,
                        "comment" : encodedmessage,
                        "levelID" : levelid,
                        "percent" : percentage,
                        "chk" : chk,
                        "secret" : "Wmfd2893gb7",
                        "udid" : udid,
                        "uuid" : playerID,

                    }

                    proxy = {

                        "http" : randomproxy,
                        "https" : randomproxy,

                    }
                        
                    try :

                        uploadmessage = post(
                            
                            url=commentPosturl,
                            data=commentpayload,
                            headers=headers,
                            proxies=proxy,
                            timeout=15,
                        
                        )

                        uploadmessage.raise_for_status()
                        posttext = uploadmessage.text

                        try :

                            int(posttext)

                            if posttext != "-1" :

                                print("comment successfully posted!")
                            
                            else :

                                print(f"There was an error with the comment upload! : {posttext}")

                        except :

                            print(f"There was an error with the comment upload! : {posttext}")

                    except Exception as Error :

                        print(f"Error : {Error}")

                    sleep(15 / (len(accountgroup)))

                except Exception as Error :
                    
                    print(f"Error : {Error}")

                if loop == -1 :

                    break
            
            if loop == False or loop == -1 :

                break

if __name__ == "__main__" :

    while True :

        command = input("Select action -> '0' close program, '1' post comments : ")

        if command == "0" :

            break

        elif command == "1" :

            try :

                getdailyweeklyurl = "https://www.boomlings.com/database/downloadGJLevel22.php"

                headers = {

                    "User-Agent": ""

                }

                def getdailyweekly(choice) :

                    data = {

                        "levelID": choice,
                        "secret": "Wmfd2893gb7"

                    }

                    req = post(url=getdailyweeklyurl, data=data, headers=headers)

                    return req.text.split(":", 2)[1]
                
                while True :
                
                    destinationtype = input("Do you want to comment on a level or list? '1' for level, '2' for list : ")

                    if destinationtype == "1" :

                        levelid = input("put the level ID here ('-1' for daily, '-2' for weekly, '-3' for event) : ")

                        if levelid.lower() == "-1" :

                            levelid = getdailyweekly(choice=-1)

                        elif levelid.lower() == "-2" :

                            levelid = getdailyweekly(choice=-2)

                        elif levelid.lower() == "-3" :

                            levelid = getdailyweekly(choice=-3)

                        break

                    elif destinationtype == "2" :

                        levelid = input("put the List ID here : ")

                        if not levelid.startswith("-") :

                            levelid = "-" + levelid
                        
                        break

                    else :

                        print("Invalid input!")

                print("(max length 150 character, 15 second cooldown per comment, add ^^ in the middle of banned words to bypass filter)")

                while True :

                    message = input("Write the message for your comment : ")

                    if len(message.replace("^^","^")) > 150 :
                        
                        print("Message exceeds 150 Characters!")

                    else :

                        break

                while True :

                    percentage = input("how much Percent do you want? (0 for none) : ")

                    try :

                        
                        percentage = int(percentage)

                        if percentage > 100 or percentage < 0 :

                            print("Percentage has to be between 0 and 100!")

                        else :

                            break

                    except ValueError :

                        print("Invalid percent!")
                
                while True :

                    loop = input("loop? 'y' for yes, 'n' for no, '-1' for only 1 comment using first account (15 seonds delay per message per account minimum!) : ")

                    if loop.lower() == "y" :

                        loop = True
                        break

                    elif loop.lower() == "n" :

                        loop = False
                        break

                    elif loop == "-1" :

                        loop = -1
                        break

                    else :

                        print("Invalid input!")
                
                bytemessage = message.replace("^^", "\u200B")
                encodedmessage = urlsafe_b64encode(bytemessage.encode()).decode()
                
                accounts = getaccounts()
                proxies = getproxies()

                proxies.remove(proxies[0])

                max = min(len(accounts),len(proxies))

                if loop != -1 :

                    while True :

                        threads = input(f"How many Threads? (max : {max}) : ")

                        try :
                            
                            threads = int(threads)
                            break

                        except ValueError :

                            print("Threads has to be a Number!")

                else :

                    threads = 1

                accountgroups = distributegroup(accounts,threads,max)
                proxygroups = distributegroup(proxies,threads,max)

                threadlist = []

                for index in range(threads) :

                    threadlist.append(Thread(target=PostComment,args=(accountgroups,proxygroups,encodedmessage,levelid,percentage,index)))   

                for thread in threadlist :

                    thread.start()

                for thread in threadlist :

                    thread.join() 

            except Exception as error :

                print(f"There was an Error : {error}")

        else :

            print("Invalid command!")
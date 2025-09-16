from requests import post
from hashlib import sha1
from itertools import cycle
from base64 import urlsafe_b64encode
from threading import Thread
from time import sleep
from random import randint

def xorcipher(string, key) :

    return "".join(chr(ord(x) ^ ord(y)) for (x, y) in zip(string, cycle(key)))

def getaccounts() :

    try :
            
        with open("accounts.txt", "r") as accountsfile :

            return [line.strip() for line in accountsfile]
        
    except FileNotFoundError :

        print("Account file 'accounts.txt' not found!")

        return False
    
def getproxies() :

    try :
            
        with open("proxies.txt", "r") as proxies :

            return [line.strip() for line in proxies]
        
    except FileNotFoundError :

        print("Proxy file 'proxies.txt' not found!")

        return False

def distributegroup(group, threads, max) :

    accountgroups = list([] for _ in range(threads))

    for index, account in enumerate(group[:max]):

        accountgroups[index % threads].append(account)

    return accountgroups

def SendMessage(accounts, proxies, encodedsubject, encodedbody, targetaccountid, thread) :

    messagesendurl = "https://www.boomlings.com/database/uploadGJMessage20.php"

    headers = {

        "User-Agent": ""

    }

    proxygroup = proxies[thread]
    accountgroup = accounts[thread]

    if accounts != False and proxies != False :

        while True :

            for index, account in enumerate(accountgroup) :
                
                try :
                    
                    username, password, accountID, playerID = account.split(",")

                    udid = "S15" + str(randint(100000, 100000000)) + str(randint(100000, 100000000)) + str(randint(100000, 100000000)) + str(randint(100000, 100000000))

                    gjp = sha1((password + "mI29fmAnxgTs").encode()).hexdigest() 

                    randomproxy = proxygroup[index]

                    commentpayload = {

                        "accountID": accountID,
                        "gjp2": gjp,
                        "toAccountID": targetaccountid,
                        "subject": encodedsubject,
                        "body": encodedbody,
                        "udid" : udid,
                        "uuid" : playerID,
                        "secret": "Wmfd2893gb7",

                    }

                    proxy = {

                        "http" : randomproxy,
                        "https" : randomproxy,

                    }
                        
                    try :

                        uploadmessage = post(
                            
                            url=messagesendurl,
                            data=commentpayload,
                            headers=headers,
                            proxies=proxy,
                            timeout=5,
                        
                        )

                        uploadmessage.raise_for_status()
                        posttext = uploadmessage.text

                        if posttext != "-1" :

                            print("message successfully sent!")
                        
                        else :

                            print(f"There was an error with the messsage sending! : {posttext}")

                    except Exception as Error :

                        print(f"Error : {Error}")

                    if loop :

                        sleep(15 / (len(accountgroup)))

                except Exception as Error :
                    
                    print(f"Error : {Error}")

                if loop == -1 :

                    break
            
            if loop == False or loop == -1 :

                break

def SendFriendRequest(accounts, proxies, encodedmessage, targetaccountid, thread) :

    messagesendurl = "https://www.boomlings.com/database/uploadFriendRequest20.php"

    headers = {

        "User-Agent": ""

    }

    proxygroup = proxies[thread]
    accountgroup = accounts[thread]

    if accounts != False and proxies != False :

        for index, account in enumerate(accountgroup) :
            
            try :
                
                username, password, accountID, playerID = account.split(",")

                udid = "S15" + str(randint(100000, 100000000)) + str(randint(100000, 100000000)) + str(randint(100000, 100000000)) + str(randint(100000, 100000000))

                gjp = sha1((password + "mI29fmAnxgTs").encode()).hexdigest() 

                randomproxy = proxygroup[index]

                commentpayload = {

                    "accountID": accountID,
                    "gjp2": gjp,
                    "toAccountID": targetaccountid,
                    "comment": encodedmessage,
                    "udid" : udid,
                    "uuid" : playerID,
                    "secret": "Wmfd2893gb7",

                }

                proxy = {

                    "http" : randomproxy,
                    "https" : randomproxy,

                }
                    
                try :

                    uploadmessage = post(
                        
                        url=messagesendurl,
                        data=commentpayload,
                        headers=headers,
                        proxies=proxy,
                        timeout=5,
                    
                    )

                    uploadmessage.raise_for_status()
                    posttext = uploadmessage.text

                    if posttext != "-1" :

                        print("friend request successfully sent!")
                    
                    else :

                        print(f"There was an error with the friend request sending! : {posttext}")

                except Exception as Error :

                    print(f"Error : {Error}")

                if loop == -1 :

                    break

            except Exception as Error :
                
                print(f"Error : {Error}")

if __name__ == "__main__" :

    while True :
        
        try :

            command = input("Select action -> '0' close program, '1' send message, '2' send friend request : ")

            if command == "0" :

                break

            elif command == "1" :

                while True :

                    recieveraccoundId = input("put the person's Account ID here : ")
                    
                    try :

                        int(recieveraccoundId)
                        break

                    except ValueError :

                        print("Account ID has to be a Number!")

                print(f"Subject : max length 35 characters\nBody : max length 200 character\n15 second cooldown per message, add ^^ in the middle of banned words to bypass filter (SUBJECT ONLY!)")

                while True :

                    messagesubject = input("Write the subject for your message : ")

                    if len(messagesubject.replace("^^","^")) > 35 :
                        
                        print("Subject exceeds 35 Characters!")

                    else :

                        break

                while True :

                    messagebody = input("Write the body for your message : ")

                    if len(messagebody) > 200 :
                        
                        print("Body exceeds 200 Characters!")

                    else :

                        break
                
                while True :

                    loop = input("loop? 'y' for yes, 'n' for no, '-1' for only 1 message using first account (15 seonds delay per message per account minimum!) : ")

                    if loop.lower() == "y" :

                        loop = True
                        break

                    elif loop.lower() == "n" :

                        loop = False
                        break

                    elif loop.lower() == "-1" :

                        loop = -1
                        break

                    else :

                        print("Invalid input!")

                bytemessagesubject = messagesubject.replace("^^", "\u200B")
                encodedmessagesubject = urlsafe_b64encode(bytemessagesubject.encode()).decode()

                xormessagebody = xorcipher(messagebody, "14251").encode()
                encodedmessagebody = urlsafe_b64encode(xormessagebody).decode()
                
                accounts = getaccounts()
                proxies = getproxies()

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

                    threadlist.append(Thread(target=SendMessage,args=(accountgroups,proxygroups,encodedmessagesubject,encodedmessagebody,recieveraccoundId,index)))

                for thread in threadlist :

                    thread.start()

                for thread in threadlist :

                    thread.join() 

            elif command == "2" :
                
                while True :

                    recieveraccoundId = input("put the person's Account ID here : ")
                    
                    try :

                        int(recieveraccoundId)
                        break

                    except ValueError :

                        print("Account ID has to be a Number!")

                print(f"Message : max length 140 character\n1 friend request per account, add ^^ in the middle of banned words to bypass filter")

                while True :

                    message = input("Write the message for your friend request (optional, leave black for none) : ")

                    if len(message.replace("^^","^")) > 200 :
                        
                        print("Message exceeds 200 Characters!")

                    else :

                        break

                while True :

                    loop = input("loop? 'y' for 1 iteration , 'n' for only 1 friend request using first account (1 friend request per account per target!) : ")

                    if loop.lower() == "y" :

                        loop = True
                        break

                    elif loop.lower() == "n" :

                        loop = -1
                        break

                    else :

                        print("Invalid input!")

                accounts = getaccounts()
                proxies = getproxies()

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

                bytemessage = message.replace("^^", "\u200B")
                encodedmessage = urlsafe_b64encode(bytemessage.encode()).decode()
                
                accountgroups = distributegroup(accounts,threads,max)
                proxygroups = distributegroup(proxies,threads,max)

                threadlist = []

                for index in range(threads) :

                    threadlist.append(Thread(target=SendFriendRequest,args=(accountgroups,proxygroups,encodedmessage,recieveraccoundId,index)))   

                for thread in threadlist :

                    thread.start()

                for thread in threadlist :

                    thread.join() 

            else :

                print("Invalid command!")
        
        except Exception as error :

            print(f"There was an Error : {error}")
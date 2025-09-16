from requests import post

def getUserIDs(username) :

    try :

        headers = {

            "User-Agent": "",

        }

        data = {

            "secret": "Wmfd2893gb7",
            "str": username,

        }

        req = post('http://www.boomlings.com/database/getGJUsers20.php', data=data, headers=headers)

        playerdata = req.text.split(":")

        playerID = playerdata[3]
        accountID = playerdata[21]

        return accountID, playerID
    
    except Exception as Error :

        print(f"there was an Error : {Error}")

def getdailyweekly(choice) :

        data = {

            "levelID": choice,
            "secret": "Wmfd2893gb7"

        }

        headers = {

            "User-Agent": "",

        }

        req = post(url="https://www.boomlings.com/database/downloadGJLevel22.php", data=data, headers=headers)

        return req.text.split(":", 2)[1]
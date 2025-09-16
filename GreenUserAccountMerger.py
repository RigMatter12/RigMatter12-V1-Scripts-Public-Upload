#299d4d74-3f5c-4dec-84fb-b127e7ee4abf,279194029 Device ID , Player ID of Green User to be transfered into an Account. (Example)
#Imported Libraries for the Request and GJP2 Hashing :
from requests import post
from hashlib import sha1

#Account Username/Password. (Must be Activated and Green upon lookup. This means you can't log into it in Game beforehand!)
userName = "USERNAME"
password = "PASSWORD"

udid = "UDID" #Decive ID of Green Users with Player ID to be transfered to Account.

playerID = "PLAYERID" #Player ID of Green User. Will be transfered to Account after FIRST Login!
accountID = "ACCOUNTID" #Not yet assigned Account ID (?uid=accountID&actcode=... from Activation Link)

#PHP Endpoint and URL-Encoded Payload for Login :
loginphp = "https://www.boomlings.com/database/accounts/loginGJAccount.php"
data = f"userName={userName}&gjp2={sha1((password+"mI29fmAnxgTs").encode()).hexdigest()}&udid={udid}&secret=Wmfv3899gc9"

try :
    #Request for Login/Merging Process from Green User to Account (Empty User-Agent Header so Cloudflare doesn't get triggered, Content-Type, and Cookie "gd=1;" because the Client has it) :
    response = post(loginphp,data=data,headers={"User-Agent":"","Content-Type":"application/x-www-form-urlencoded","Cookie":"gd=1;"}).text
    if "," in response :
        if response == f"{accountID},{playerID}" :
            #If successful :
            print(f"Green User has been Successfully merged to Account : {userName}!")
        else :
            #If mismatch between Account/Green User :
            print(f"Warning! Login successful but IDs don't match up!\nOld Account/Player IDs : {accountID},{playerID}\nNew Account/Player IDs : {response}")
    else :
        #Unexpected Response :
        print(f"Request Failed, Error Code : {response}")
except Exception as error :
    #Exception Triggered :
    print(f"There was an Error : {error}")
#End of Code.
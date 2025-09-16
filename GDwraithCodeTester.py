from requests import post
while True:
    if post("https://www.boomlings.com/database/getGJSecretReward.php",data={"rewardKey":input("Type in a wraith code : ").replace(" ",""),"udid":"1","chk":"g6f2zAAwHCgMG","secret":"Wmfd2893gb7"},headers={"User-Agent":""}).content.decode()!="-1":
        print("Code Works!")
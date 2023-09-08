from utils import Flags
from modules import GoogleDork
from modules import Attack

LOG_MESSAGE_VLAUE_ERR = "[ERORR]  IN VLAUE : this message shown when you are passed Not valid vlaue as arguemnt"
LOG_MESSAGE_NET_ERR = "[ERORR] IN YOU CONNECTION : this message shown if you interNet Connection Faild "

flags = Flags()

target = flags.getTargetUrl()

category = flags.getCategory()

payload = flags.getPayloads()

Dork = GoogleDork()
blackBox = Attack()

print(f"{category}  {payload}  {target}")
print("[*] starting ... this maybe take some time ")


url = "https://www.exploit-db.com/google-hacking-database/"

print("[*] getting the Rsponse from Google Hacking DB ... " , end="")

jsonResponseFromGoogleHackingDb = Dork.getJsonResponseFromWebsite(url)

print("Ok")

resault = []

if type(target) is list:
    listOfTarget = flags.loadFile(target)
    for target in listOfTarget:
        if category == "all":
            if payload > 10 and payload != "all" : # 10 because the default number of payloads is 10
                output = blackBox.attackSpcificPayloadAllCategory(
                    jsonResponseFromGHDB=jsonResponseFromGoogleHackingDb,
                    target=target,
                    payload=payload,
                )
            elif payload == "all" :
                output = blackBox.attackAllPayloadAllCategory(
                    jsonResponseFromGHDB=jsonResponseFromGoogleHackingDb,
                    target=target
                )

        elif category != "all":
            if payload > 10 and payload != "all" : # 10 because the default number of payloads is 10
                output = blackBox.attackSpcificPayloadSpcificCategory(
                    jsonResponseFromGHDB=jsonResponseFromGoogleHackingDb,
                    category=category,
                    payload=payload,
                    target=target
                )
            elif payload == "all" :
                output = blackBox.attackAllPaylaodSpcificCategroy(
                    jsonResponseFromGHDB=jsonResponseFromGoogleHackingDb,
                    category=category,
                    target=target,
                )

elif type(target) is str:
    if category == "all":
        if payload > 10 and payload != "all" : # 10 because the default number of payloads is 10
            output = blackBox.attackSpcificPayloadAllCategory(
                jsonResponseFromGHDB=jsonResponseFromGoogleHackingDb,
                target=target,
                payload=payload,
            )
        elif payload == "all" :
            output = blackBox.attackAllPayloadAllCategory(
                jsonResponseFromGHDB=jsonResponseFromGoogleHackingDb,
                target=target
            )

    elif category != "all":
        if payload > 10 and payload != "all" : # 10 because the default number of payloads is 10
            output = blackBox.attackSpcificPayloadSpcificCategory(
                jsonResponseFromGHDB=jsonResponseFromGoogleHackingDb,
                category=category,
                payload=payload,
                target=target
            )
        elif payload == "all" :
            output = blackBox.attackAllPaylaodSpcificCategroy(
                jsonResponseFromGHDB=jsonResponseFromGoogleHackingDb,
                category=category,
                target=target,
            )

else:
    print("[ERROR] TYPE_ERR : the Target url is NOT string Or file")







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

                    listOfDorkFromGHDB = Dork.getSpcificNumberOfDorksFromGoogleHackingDB(
                        jsonResponse  = jsonResponseFromGoogleHackingDb,
                        numberOfDorks = payload
                        )
                
                    listOfQuery = blackBox.setListOfQuery(listOfDorkFromGHDB , target)

                    listOfValideQuery = blackBox.validateListOfQuery(
                        listOfQuery = listOfQuery
                        )

                    for query in listOfValideQuery:
                        resault = blackBox.getListOfVulnURL(
                                query=query
                                )
                    
                    print("========the resault=========")

                    for query in resault:
                        print(query)


                elif payload == "all" :

                    listOfDorkFromGHDB = Dork.getAllDorksFromGoogleHackingDb(
                        jsonResponse = jsonResponseFromGoogleHackingDb
                    )

                    listOfQuery = blackBox.setListOfQuery(listOfDorkFromGHDB , target)

                    listOfValideQuery = blackBox.validateListOfQuery(
                        listOfQuery = listOfQuery
                        )

                    for query in listOfValideQuery:
                        resault = blackBox.getListOfVulnURL(
                                query=query
                                )
                    
                    print("========the resault=========")
                    for query in resault:
                        print(query)

            elif category != "all":

                if payload > 10 and payload != "all" : # 10 because the default number of payloads is 10

                    print(f"[*] getting Categor {category} from Google Hackin Response ... " , end="")
                    listOfDorkFromGHDB = Dork.getDorksFromGoogleHackingDbByCategory(
                        jsonResponse = jsonResponseFromGoogleHackingDb,
                        category = category  
                    )
                    print("Ok")
                    
                    listOfDorkFromList = Dork.getSpacificNumberOfDorkFromList(
                        listOfDork   = listOfDorkFromGHDB,
                        numberOfDork = payload
                    )
                    print(listOfDorkFromList)

                    listOfQuery = blackBox.setListOfQuery(listOfDorkFromList , target)

                    listOfValideQuery = blackBox.validateListOfQuery(
                        listOfQuery = listOfQuery
                        )

                    for query in listOfValideQuery:
                        blackBox.getListOfVulnURL(
                                query=query
                                )

                
                elif payload == "all" :

                    listOfDorkFromGHDB = Dork.getDorksFromGoogleHackingDbByCategory(
                        jsonResponse = jsonResponseFromGoogleHackingDb,
                        category = category  
                    )

                    listOfQuery = blackBox.setListOfQuery(listOfDorkFromGHDB , target)

                    listOfValideQuery = blackBox.validateListOfQuery(
                        listOfQuery = listOfQuery
                        )

                    for query in listOfValideQuery:
                        resault = blackBox.getListOfVulnURL(
                                query=query
                                )
                    
                    print("========the resault=========")
                    for query in resault:
                        print(query)



elif type(target) is str:
    
    if category == "all":

        if payload > 10 and payload != "all" : # 10 because the default number of payloads is 10

            listOfDorkFromGHDB = Dork.getSpcificNumberOfDorksFromGoogleHackingDB(
                 jsonResponse  = jsonResponseFromGoogleHackingDb,
                 numberOfDorks = payload
                )
        
            listOfQuery = blackBox.setListOfQuery(listOfDorkFromGHDB , target)

            listOfValideQuery = blackBox.validateListOfQuery(
                listOfQuery = listOfQuery
                )

            for query in listOfValideQuery:
                resault = blackBox.getListOfVulnURL(
                        query=query
                        )
            
            print("========the resault=========")

            for query in resault:
                print(query)


        elif payload == "all" :

            listOfDorkFromGHDB = Dork.getAllDorksFromGoogleHackingDb(
                jsonResponse = jsonResponseFromGoogleHackingDb
            )

            listOfQuery = blackBox.setListOfQuery(listOfDorkFromGHDB , target)

            listOfValideQuery = blackBox.validateListOfQuery(
                listOfQuery = listOfQuery
                )

            for query in listOfValideQuery:
                resault = blackBox.getListOfVulnURL(
                        query=query
                        )
            
            print("========the resault=========")
            for query in resault:
                print(query)

    elif category != "all":

        if payload > 10 and payload != "all" : # 10 because the default number of payloads is 10

            print(f"[*] getting Categor {category} from Google Hackin Response ... " , end="")
            listOfDorkFromGHDB = Dork.getDorksFromGoogleHackingDbByCategory(
                jsonResponse = jsonResponseFromGoogleHackingDb,
                category = category  
            )
            print("Ok")
            
            listOfDorkFromList = Dork.getSpacificNumberOfDorkFromList(
                listOfDork   = listOfDorkFromGHDB,
                numberOfDork = payload
            )
            print(listOfDorkFromList)

            listOfQuery = blackBox.setListOfQuery(listOfDorkFromList , target)

            listOfValideQuery = blackBox.validateListOfQuery(
                listOfQuery = listOfQuery
                )

            for query in listOfValideQuery:
                blackBox.getListOfVulnURL(
                        query=query
                        )

        
        elif payload == "all" :

            listOfDorkFromGHDB = Dork.getDorksFromGoogleHackingDbByCategory(
                jsonResponse = jsonResponseFromGoogleHackingDb,
                category = category  
            )

            listOfQuery = blackBox.setListOfQuery(listOfDorkFromGHDB , target)

            listOfValideQuery = blackBox.validateListOfQuery(
                listOfQuery = listOfQuery
                )

            for query in listOfValideQuery:
                resault = blackBox.getListOfVulnURL(
                        query=query
                        )
            
            print("========the resault=========")
            for query in resault:
                print(query)


else:
    print("[ERROR] TYPE_ERR : the Target url is NOT string Or file")







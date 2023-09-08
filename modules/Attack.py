
from yagooglesearch import SearchClient
import re
from .GoogleDork import GoogleDork

URL_NEED_IGNORE= [
    "https://www.kb.cert.org",
    "https://www.exploit-db.com/",
    "https://twitter.com/ExploitDB/",
    ]


class Attack():
    def __init__(self) -> None:
        self.Dork = GoogleDork()
        self.resault = []

    def setQuery(self , targetWebsite , dork):

        return f"site:{targetWebsite} {dork}"
    

    def setListOfQuery(self , listOfDork , targetWebsite):
         
        listOfQuery = []

        for dork in listOfDork:

            query = self.setQuery(targetWebsite , dork)
            listOfQuery.append(query)
            
        return listOfQuery


    def validateQuery(self , query):
        if len(query.split(" ")) > 32:
                    validQuery = " ".join(query.split(" ")[0:32])

                    if query.endswith('"'):
                        validQuery = f'{validQuery}"'

                    query = validQuery

        return query
    

    def validateListOfQuery(self, listOfQuery):
        
        listOfValideQuery = []

        for query in listOfQuery:

            validQuery = self.validateQuery(query)

            listOfValideQuery.append(validQuery)

        return listOfValideQuery


    def getListOfVulnURL(self ,query):

        client = SearchClient(
            query,
            tbs="li:1",
            max_search_result_urls_to_return=100,
            minimum_delay_between_paged_results_in_seconds=12,
            http_429_cool_off_time_in_minutes=45,
            http_429_cool_off_factor=1.5,
            verbosity=5,
            verbose_output=False,
        )
        client.assign_random_user_agent()

        urls = client.search()

        return urls


    def ignoreURLS(self , listOfURL):
        for url in listOfURL:
            
            for ignore_url in URL_NEED_IGNORE:

                if re.search(ignore_url, url, re.IGNORECASE):

                    print(f"Removing {ignore_url} false positive URL: {url}")
                    listOfURL.remove(url)

        return listOfURL


    def attackSpcificPayloadAllCategory(self, 
                                        jsonResponseFromGHDB, 
                                        target,
                                        payload):
        
        listOfDorkFromGHDB = self.Dork.getSpcificNumberOfDorksFromGoogleHackingDB(
                 jsonResponse  = jsonResponseFromGHDB,
                 numberOfDorks = payload
                )
        listOfQuery = self.setListOfQuery(listOfDorkFromGHDB , target)
        listOfValideQuery = self.validateListOfQuery(
                listOfQuery = listOfQuery
                )
        for query in listOfValideQuery:
                self.resault = self.getListOfVulnURL(
                        query=query
                        )
        
        self.resault = self.ignoreURLS(self.resault)
        return self.resault


    def attackAllPayloadAllCategory(self,
                                    jsonResponseFromGHDB,
                                    target):
        
        listOfDorkFromGHDB = self.Dork.getAllDorksFromGoogleHackingDb(
                jsonResponse = jsonResponseFromGHDB
            )
        listOfQuery = self.setListOfQuery(listOfDorkFromGHDB , target)
        listOfValideQuery = self.validateListOfQuery(
                listOfQuery = listOfQuery
                )
        for query in listOfValideQuery:
                self.resault = self.getListOfVulnURL(
                        query=query
                        )
        
        self.resault = self.ignoreURLS(self.resault)
        return self.resault
    

    def attackSpcificPayloadSpcificCategory(self, 
                                            jsonResponseFromGHDB,
                                            category,
                                            payload, 
                                            target):
        
        listOfDorkFromGHDB = self.Dork.getDorksFromGoogleHackingDbByCategory(
                jsonResponse = jsonResponseFromGHDB,
                category = category  
            )            
        listOfDorkFromList = self.Dork.getSpacificNumberOfDorkFromList(
                listOfDork   = listOfDorkFromGHDB,
                numberOfDork = payload
            )
        listOfQuery = self.setListOfQuery(listOfDorkFromList , target)
        listOfValideQuery = self.validateListOfQuery(
                listOfQuery = listOfQuery
                )
        
        for query in listOfValideQuery:
            self.resault = self.getListOfVulnURL(
            query=query
                    )
            
        self.resault = self.ignoreURLS(self.resault)

        return self.resault


    def attackAllPaylaodSpcificCategroy(self,
                                        jsonResponseFromGHDB, 
                                        category,
                                        target):
            
            listOfDorkFromGHDB = self.Dork.getDorksFromGoogleHackingDbByCategory(
                jsonResponse = jsonResponseFromGHDB,
                category = category  
            )
            listOfQuery = self.setListOfQuery(listOfDorkFromGHDB , target)
            listOfValideQuery = self.validateListOfQuery(
                listOfQuery = listOfQuery
                )
            for query in listOfValideQuery:
                self.resault = self.getListOfVulnURL(
                query=query
                        )
            
            self.resault = self.ignoreURLS(self.resault)

            return self.resault
    

    def OUTPUT_(self, output:list):
        if output:
            for item in output:
                print(f"-> {item}")

        else:
            print("[ SAD ] No output To be printed...")
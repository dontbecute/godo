
from yagooglesearch import SearchClient
import re

URL_NEED_IGNORE= [
    "https://www.kb.cert.org",
    "https://www.exploit-db.com/",
    "https://twitter.com/ExploitDB/",
    ]


class Attack():

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


    def OUT_reault(self , listOfVulnURL):
         
        if listOfVulnURL:
              for url in listOfVulnURL:
                   print(url)

        else:
            print("[ BAD NEWS ] WE_ARE_EMPTY : This site maybe good we are NOT Founding ANY valide dork against it")

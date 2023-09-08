from bs4 import BeautifulSoup
import requests

class GoogleDork():
    def __init__(self) -> None:
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "deflate, gzip, br",
            "Accept-Language": "en-US",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0",
            "X-Requested-With": "XMLHttpRequest",
            }
    
    def getJsonResponseFromWebsite(self , url):
        response = requests.get(
                url,
                headers=self.headers,
                )

        jsonResponse = response.json()


        return jsonResponse

    def getAllDorksFromGoogleHackingDb(self , jsonResponse):

        dorks = []

        for item in jsonResponse['data']:
            
            dork = item['url_title']
            dork = BeautifulSoup(dork, "html.parser").get_text()
            dorks.append(dork)

        return dorks


    def getDorksFromGoogleHackingDbByCategory(self , jsonResponse, category):
        dorks = []

        for item in jsonResponse['data']:
            
            if item['category']['cat_title'] == category:
                
                dork = item['url_title']
                dork = BeautifulSoup(dork, "html.parser").get_text()
                dorks.append(dork)

        return dorks
    
    def getSpcificNumberOfDorksFromGoogleHackingDB(self , jsonResponse , numberOfDorks):

        dorks = []

        for item in jsonResponse['data']:
            dork = item['url_title']
            dork = BeautifulSoup(dork, "html.parser").get_text()
            dorks.append(dork)
            
            if len(dorks) >= numberOfDorks:
                    break

        return dorks
    


    def getSpacificNumberOfDorkFromList(self , listOfDork , numberOfDork):
        
        RETURNED_Dorks = []

        for dork in listOfDork:

            RETURNED_Dorks.append(dork)

            if len(RETURNED_Dorks) >= numberOfDork:
                break


        return RETURNED_Dorks
    
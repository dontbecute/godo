
from urllib.parse import urlparse
import argparse
from .startScreen import START_

CATEGORY_MAPPING = {
    "1": "Footholds",
    "2": "Files Containing Usernames",
    "3": "Sensitive Directories",
    "4": "Web Server Detection",
    "5": "Vulnerable Files",
    "6": "Vulnerable Servers",
    "7": "Error Messages",
    "8": "Files Containing Juicy Info",
    "9": "Files Containing Passwords",
    "10": "Sensitive Online Shopping Info",
    "11": "Network Or Vulnerability Data",
    "12": "Pages Containing Login Portals",
    "13": "Various Online Devices",
    "14": "Advisories And Vulnerabilites",
    "15": "all",
}

CRED = '\033[91m'

class Flags():
    def __init__(self) -> None:
                
        self.parser = argparse.ArgumentParser(description=""" Google Dork Tool :  godo   1.0  ✨🍰✨ """)

        self.parser.add_argument("-t", "--target", required=True, help="Specify the target URL or file with a list of hosts")
        
        self.parser.add_argument("-p", "--payload",
                                 default=10,
                                 help="Specify the number of payloads to use")
        
        self.parser.add_argument("-C", "--category",
                                 default= "all", 
                                 help="""Specify the category for Google Dork DB one of this value:
                                    "footholds": "1",
                                    "files-Containing-Usernames": "2",
                                    "sensitive-Directories": "3",
                                    "web-server-detection": "4",
                                    "vulnerable-files": "5",
                                    "vulnerable-servers": "6",
                                    "error-messages": "7",
                                    "Files Containing Juicy Info": "8",
                                    "files-Containing passwords": "9",
                                    "sensitive-online-shopping info": "10",
                                    "Network-or-vulnerability-data": "11",
                                    "pages-Containing-login-portals": "12",
                                    "Various-Online-Devices": "13",
                                    "advisories-and-vulnerabilites": "14",
                                    "all": "15",
                                 """)
        
        self.args = self.parser.parse_args()


    def getTargetUrl(self):
        
        target = self.args.target
        
        return self.validateTarget(target)


    def validateTarget(self , target):
        if self.isUrl(target):
            return target
        
        elif self.isInputFile(target):
            target = self.loadFile(target)
            return target
        else:
            print(CRED + """[ERROR] VALUE_ERR : you are passed not valide URL you need to pass it with scheme && netloc 
                        https://www.example.com""" + CRED)
            exit(1)


    def isUrl(self , url):
            
        result = urlparse(url)

        if result.scheme and result.netloc:
            return True

        else:
            return False


    def IsListOfUrl(self , listOfUrl : list) -> bool:
        for url in listOfUrl:
            
            if self.isUrl(url):
                continue
            else:
                return False

        return True    


    def isInputFile(self , file : str) -> bool:
        try:
            with open(file , "r") as fileRead:
                fileRead.read()
                return True
        except:
            return False


    def loadFile(self , file : str) -> list:
        try:
            with open(file , 'r') as fileRead:
                
                lines = fileRead.readlines()
                
                if self.IsListOfUrl(lines):
                    
                    return lines
                else: 
                    exit(1)
        except:
            print("[ERROR] LOAD_ERR : error while loading targets file Maybe It's contain Not valide Url Or it's Not readable file")
            exit(1)




    def getCategory(self):
        category = self.args.category
        
        return self.validateCategory(category)


    def validateCategory(self , category):
        if category.isdigit() and 1 <= int(category) <= 15:
            selected_category = CATEGORY_MAPPING[category]

            return selected_category
        else:   
            if category in CATEGORY_MAPPING.values():
                selected_category = category
                return selected_category
            
            else:
                print(CRED + f"[ERROR] VALUE_ERR : Invalid category choice: {self.args.category}. Choose from {', '.join(CATEGORY_MAPPING.keys())}." + CRED)
                exit(1)


    def getPayloads(self):

        payload = self.args.payload

        return self.validatePayload(payload)
    

            
    def validatePayload(self , payload):
        if payload == "all":
            return payload
        
        return self.convertToNum(payload)
            

    def convertToNum(self , paylaod) -> int:
        try:
            payload = int(paylaod)
                    
            return payload
        except:
            print(f"[ERROR] VALUE_ERR : your passed to payload should be an Interger ( Number )")
            exit(1)


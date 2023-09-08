# godo - brute force Google Dorks


## Introduction

`godo` automates Google searching for potentially vulnerable web pages and applications on the Internet.  It replaces manually performing Google dork searches with a web GUI browser.

`godo` tool for brute force google dork against Websites


## What are Google dorks?

Offensive Security maintains the Google Hacking Database (GHDB) found here:
<https://www.exploit-db.com/google-hacking-database>.  It is a collection of Google searches, called dorks, that can be
used to find potentially vulnerable boxes or other juicy info that is picked up by Google's search bots.


## Installation

 - Clone the git repository 
    ```bash
    https://github.com/dontbecute/godo.git
    ```
 
 - install the requirements.

    ```bash
    cd pagodo
    ```
 - if you using venv 
 
    ```bash
    virtualenv -p python3.7 .venv  # If using a virtual environment.
    source .venv/bin/activate
    ```

 - install req from the file 
    
    ```bash
    pip install -r requirements.txt
    ```

## godo run main.py 

- to start the tool you can use some of this example 

    ```bash
    python3 main.py -t (you target URL) -C (category form GHDB) -p (number of payload you need)
    ```
    - the `all` when you passed to -C the tool will try all Dorks on GHDB
    - the `all` when passed to -p the tool will try all payloads on GHDB OR all payloads you choise form category
    

- Dork categories:

    ```python
    categories = {
        1: "Footholds",
        2: "File Containing Usernames",
        3: "Sensitives Directories",
        4: "Web Server Detection",
        5: "Vulnerable Files",
        6: "Vulnerable Servers",
        7: "Error Messages",
        8: "File Containing Juicy Info",
        9: "File Containing Passwords",
        10: "Sensitive Online Shopping Info",
        11: "Network or Vulnerability Data",
        12: "Pages Containing Login Portals",
        13: "Various Online devices",
        14: "Advisories and Vulnerabilities",
    }
    ```


## FROM THE FUTURE

Performing 7300+ search requests to Google as fast as possible will simply not work. Google will rightfully detect it as a bot and block your IP for a set period of time. One solution is to use a bank of HTTP(S)/SOCKS proxies and pass them to GODO in `ATTACK.PY` file 

Well, this tool is not a complete thing yet. I will work on adding many features later. Some of these features will be

* Save results
* Bypass Google ban
* Add a proxy
* Add timers


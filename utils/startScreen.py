START_ = """
        Google Dork Tool :  godo   1.0  ✨🍰✨ 

                                        flag                   values                                        

        - target                        -t | --target          "  your target url  "   

        - google dork payloads          -p | --payloads        "  number of payloads you need to Try  " 
                                                                        -- you can use all --

        - category :                    -C | --Category         footholds , files Containing Usernames , 
                                                                sensitive Directories , web server detection 
                                                                vulnerable files , vulnerable servers , 
                                                                error messages , files Containing juicy Info , 
                                                                files Containing passwords ,  
                                                                sensitive online shopping info , Network or vulnerability data
                                                                pages Containing login portals , 
                                                                Various Online Devices , advisories and vulnerabilites , 
                                                                        --you can use "all" as value --

        - save                          

        -help                           -h | --help             printing this message
        

        
    Note: the Category you can using it by number in pre order so you can make it 1 , 2 ,3 , 4 ...etc 

                                    python3 main.py -t https://m.example.com/ -C 5 -p all (thats mean vulnerable files will be used)
                                    
                                    [*] here the script will send the request to google dork db with category param with num 5 
                                    and re execute step 1 using all payloads returned 
                                    if the -p 10 will execute step 1 for 10 payloads 
                                    ...
                                    ...
                                    etc 
                                    
    Or you can use it dirctly like : 
                                    python3 main.py -t https://m.example.com/ --vulnerable-files -p all

    some example:
            python3 main.py -t https://example.com/ -p all
            python3 main.py -t hosts.txt -p all
            python3 main.py -t https://example.com/ --vulnerable-files || -C 5 -p all 

    """


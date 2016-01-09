````


 _______  __   __  _______  ______   _______  __    _          _______  _______  _______ 
|       ||  | |  ||       ||      | |   _   ||  |  | |        |  _    ||       ||       |
|  _____||  |_|  ||   _   ||  _    ||  |_|  ||   |_| |        | |_|   ||   _   ||_     _|
| |_____ |       ||  | |  || | |   ||       ||       |        |       ||  | |  |  |   |  
|_____  ||       ||  |_|  || |_|   ||       ||  _    |        |  _   | |  |_|  |  |   |  
 _____| ||   _   ||       ||       ||   _   || | |   | _____  | |_|   ||       |  |   |  
|_______||__| |__||_______||______| |__| |__||_|  |__||_____| |_______||_______|  |___|  


Shodan_bot is a quickly programmed query tool for Shodan based largely on the documentation
for the Shodan python library (shodan.readthedocs.org).

The tool will allow a user to upload a Shodan API key and search by either query string
or host IP.  The IPs and ports, separated by a :, from a query will print into the host.txt
file and the ports, banner and service information for a host search will print into a query.txt
file. 

Before running for the first time an API key must be inserted into the code on the following line:
SHODAN_API_KEY = <insert API Key here>
Without an API key the search will not function.  
To get an API key sign up for a free Shodan account at shodan.io


usage: shodan_bot.py [-h] [--query] [--host]

optional arguments:
  -h, --help  show this help message and exit
  --key KEY   Input Shodan Key Here
  --query     Search Shodan for Term
  --host      Search Shodan for Host


When query or host are selected the user is met with a prompt for their search.  

example:  python shodan_bot.py --query

dependencies:
shodan (python library)
Shodan account

To get shodan library just type:
easy_install shodan
````
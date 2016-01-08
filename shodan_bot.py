import shodan
import argparse


print """


 _______  __   __  _______  ______   _______  __    _    _______  _______  _______ 
|       ||  | |  ||       ||      | |   _   ||  |  | |  |  _    ||       ||       |
|  _____||  |_|  ||   _   ||  _    ||  |_|  ||   |_| |  | |_|   ||   _   ||_     _|
| |_____ |       ||  | |  || | |   ||       ||       |  |       ||  | |  |  |   |  
|_____  ||       ||  |_|  || |_|   ||       ||  _    |  |  _   | |  |_|  |  |   |  
 _____| ||   _   ||       ||       ||   _   || | |   |  | |_|   ||       |  |   |  
|_______||__| |__||_______||______| |__| |__||_|  |__|  |_______||_______|  |___|  


"""
print ""
print ""

parser = argparse.ArgumentParser()
parser.add_argument('--key', help = "Input Shodan Key Here")
parser.add_argument('--query', help = "Search Shodan for Term", action = 'store_true')
parser.add_argument('--host', help = "Search Shodan for Host", action = 'store_true')


args = parser.parse_args()
key = args.key
query = args.query
host = args.host

if args.key:

	SHODAN_API_KEY = key
	api = shodan.Shodan(SHODAN_API_KEY)

if args.query:
	query = raw_input('[+] Please Input Search String: ')

	try:

		results = api.search(query)

		print 'Results found %s' % results['total']

		for result in results['matches']:
			print 'IP: %s' % result['ip_str']
			print result['data']
			print ''

	except shodan.APIError, e:
		print 'Error: %s' % e

if args.host:
	host = api.host(raw_input('[+] Please Input Host: '))

	print """
		IP: %s
		Organization: %s
		Operating System: %s
	""" % (host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a'))

	for item in host['data']:
		print """
			Port: %s
			Banner: %s

		""" % (item['port'], item['data'])
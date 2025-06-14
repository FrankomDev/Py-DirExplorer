import argparse
import validators
import requests

def attack(url, wrdlst):
    if validators.url(url):
        with open (wrdlst, 'r') as file:
            for line in file:
                line = line[:-1]
                if requests.get(url+'/'+line).status_code == 200:
                    print('FOUND: /'+line)
    else:
        print('Url is incorrect!')

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--url", help = "attack url")
parser.add_argument("-w", "--wordlist", help = "wordlist")

args = parser.parse_args()

if args.wordlist:
    if args.url:
        attack(args.url, args.wordlist)
    else:
        print("Use '-u' to add url")

elif args.url:
    if args.wordlist:
        attack(args.url, args.wordlist)
    else:
        print("Use '-w' to add wordlist")
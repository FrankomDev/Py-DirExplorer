import argparse
import validators
import requests

def attack(url, wrdlst, type):
    if type == 'dir':
        if validators.url(url):
            with open (wrdlst, 'r') as file:
                for line in file:
                    line = line[:-1]
                    if requests.get(url+'/'+line).status_code == 200:
                        print('FOUND: /'+line)
        else:
            print('Url is incorrect!')
    elif type == 'dns':
        if validators.url(url):
            if url[4] == 's':
                pre = 'https://'
                domain = url[8:]
            else:
                pre = 'http://'
                domain = url[7:]
            with open (wrdlst, 'r') as file:
                for line in file:
                    line = line[:-1]
                    try:
                        r = requests.get(pre+line+'.'+domain)
                        r.raise_for_status()
                        if r.status_code == 200:
                            print('FOUND: '+line+'.'+domain)
                    except:
                        pass
        else:
            print('Url is incorrect!')
    else:
        print('Attack type is icorrect!')

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--url", help = "attack url")
parser.add_argument("-w", "--wordlist", help = "wordlist")
parser.add_argument("-a", "--attack", help = "attack type (dir/dns)")

args = parser.parse_args()

if args.attack:
    if args.wordlist:
        if args.url:
            attack(args.url, args.wordlist, args.attack)
        else:
            print("Use '-u' to add url")
    elif args.url:
        if args.wordlist:
            attack(args.url, args.wordlist, args.attack)
        else:
            print("Use '-w' to add wordlist")
else:
    print("Use '-a' to select attack type")
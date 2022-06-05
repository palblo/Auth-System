import requests, os

def auth():
    os.system('cls')
    url = 'https://pastebin.com/raw/zkgMJRa8'
   
    r = requests.get(url)
    
    keys =  r.text.split('\r\n')

    if r.status_code == 200:
        key = input('License key: ')
    
        if key in keys:
            print('\nValid key')
            main()
        else:
            print('\nInvalid key')
            auth()
    else:
        print(f'Invalid url (Code : {r.status_code})')

def main():
    #YOUR CODE HERE
    input()

auth()
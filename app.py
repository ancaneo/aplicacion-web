from fastapi import FastAPI, status
from configparser import ConfigParser
import requests

app = FastAPI()

parser = ConfigParser()
parser.read('system.conf')

endpoint = parser.get('DEV', 'endpoint')
user = parser.get('DEV', 'user')
password = parser.get('DEV', 'password')
url = endpoint + str('?q=ingestiondate:[NOW-1DAY TO NOW] AND producttype:SLC&rows=100&start=0&format=json')


print(url)
print(endpoint)

@app.get('/', status_code=status.HTTP_200_OK)
def get_info():
    
    copernico = requests.get(url, auth=(user, password))
    
    if copernico.status_code == status.HTTP_200_OK:
        
        return copernico.json()
    
    else:
        return copernico.status_code
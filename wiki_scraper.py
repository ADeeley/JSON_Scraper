import requests
import json

URL = 'https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=jsonfm&formatversion=2&titles=List%20of%20best-selling%20fiction%20authors&format=json'

"""
Pulls the Json from the Wikipedia API (Currently hardcoded with bestsellers.)
"""
def getJSON(URL):
    response = requests.get(URL)
    print('Status: ', response.status_code)
    print('Encoding: ', response.encoding)
    return response.json()

data = getJSON(URL)

print(data['batchcomplete'])
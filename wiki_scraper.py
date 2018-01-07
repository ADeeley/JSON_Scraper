import requests
import json

URL = 'https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=jsonfm&formatversion=2&titles=List%20of%20best-selling%20fiction%20authors&format=json'

"""
Pulls the Json from the Wikipedia API (Currently hardcoded with bestsellers.)
"""
def getJSON(URL):
    response = requests.get(URL)
    assert response.status_code == 200
    return response.json()

def main():
    data = getJSON(URL)
    print(data['batchcomplete'])

if __name__ == '__main__':
    main()
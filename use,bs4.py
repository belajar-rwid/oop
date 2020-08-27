import requests
from bs4 import BeautifulSoup

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success!!{response.status_code}')
        #print(f'Content{response.text}')
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f'hasil pamggilan {url}')
        print(f'Titlel: {soup.title.string}')
    else:
        print(f'Woops, ada kesalahhan requests  {response.status_code}')

except Exception as e:
    print('There is an error', {e})
print('Program ended')

''''
import requests

source = 's_ats'
key = '4d5fbfd8e00047d6931ede2d301c3caa'
url = 'https://data.egov.kz/api/v4/s_ats/data?apiKey=4d5fbfd8e00047d6931ede2d301c3caa'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
r = requests.get(url, headers=headers, verify=False)
print()
print(r)
'''

import requests

url = "https://data.egov.kz/api/v4/s_ats/data"

headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

params = {'apiKey':'4d5fbfd8e00047d6931ede2d301c3caa'}
response = requests.request(method='POST', url=url, headers=headers, params=params, verify=False)

print(response.text.encode('utf8'))
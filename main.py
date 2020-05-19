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

url = "https://data.egov.kz/api/v4/s_ats/data?apiKey=4d5fbfd8e00047d6931ede2d301c3caa"

headers = {
  'Content-Type': 'application/json',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

response = requests.request(method='GET', url=url, headers=headers)

print(response.json())
import requests
import json
import pandas as pd
import time

def save_to_csv(list, file_name):
  out = open(file_name, 'w')
  df = pd.DataFrame(list)
  df.to_csv(out)
  out.close()

source = 's_pb'
key = '4d5fbfd8e00047d6931ede2d301c3caa'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

c=1
i=0
step = 10000
result = list()
while i < 4055895:
  if c%39==0:
    time.sleep(70)
  url = 'https://data.egov.kz/api/v4/'+source+'/data?apiKey='+key+'&source={"from": '+str(i)+', "size": '+str(step)+'}'
  resp_list = requests.get(url, headers=headers, verify=False).json()
  result.extend(resp_list)
  print(len(result))
  i=i+step
  c=c+1
save_to_csv(result, source+'.csv')  

'''
resp_list_item = resp_list[0]
for idx, item in enumerate(resp_list, start=1):
  print(idx)
  for key in resp_list_item.keys():
    print(key+": "+resp_list_item[key])
  print('------------------------------')
'''
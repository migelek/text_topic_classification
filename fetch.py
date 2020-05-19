import requests

res = requests.get('https://sd-master.test.superdesk.org/contentapi/items')
res.status_code
# should be 401

res = requests.get('https://sd-master.test.superdesk.org/contentapi/items', headers={'Authorization': 'EbLwHCxKEbUW/cSdDtLxlKp+UEKtnam1xjbAmEtHNNtPGFspK1iRWw=='})
res.status_code
# should be 200

res.json()

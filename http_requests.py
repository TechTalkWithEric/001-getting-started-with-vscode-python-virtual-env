import requests

print('http requests')

payload = dict(key1='value1', key2='value2')
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)

if r.status_code != 200:
    print(f'something went wrong, please try again. status code {r.status_code}')

else:
    print('success')


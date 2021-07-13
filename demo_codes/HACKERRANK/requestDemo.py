import requests

def site(URL):
    code=requests.get(url=URL)
    return code




ans=site('http://www.google.com')
print(ans.text)
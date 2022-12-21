# HackTheBox-Emdee Five For Life

<img src="https://imgur.com/38Q4TnW.png"/>

We are presented with this html page having a string and told to encrpyt it with MD5 but when we try to submit it after encrpyting we get a message "Too Slow"

<img src="https://imgur.com/Cqov6VD.png"/>

Intercepting the request with `Burp Suite` and found that we have to make a POST request to send the MD5 hash

<img src="https://i.imgur.com/iOW0886.png"/>

Also the string is generated randomly so we need to script it and the best language for this is python so I used python libraries `requests` , `hashlib` and `BeautifulSoup`

```python
import hashlib
import requests
from bs4 import BeautifulSoup

# Persists cookies across all requests
request = requests.session()
# URL For the challenge page
url = "http://159.65.25.97:31667"
page = request.get(url)

soup = BeautifulSoup(page.content,"html.parser")
# Saving the string to be encrpyted
string_to_encrpyt = soup.select('h3')[0].text

# Caluclating hash of the string
MD5 = hashlib.md5(string_to_encrpyt.encode('utf-8')).hexdigest()

# POST data to send
data = {'hash' :MD5}

# Sending data as POST request
response = request.post(url,data)
print(response.text)
```

<img src="https://i.imgur.com/UOndl6L.png"/>

We got the flag !!!
# TryHackMe-OhSINT

> Abdullah Rizwan | 11 th September , 07 : 44 PM


This is a OSINT box where we have to analyze information only through image provided to us.


This is the image from which we have to extract data from.
<img src="https://imgur.com/BzGUlrw.png" />

I ran `exiftool` to see information of the image and found a name `OWoodflint`

<img src="https://imgur.com/rbwGIkc.png" />

1. What is this users avatar of?

<img src="https://imgur.com/He8utTL.png" />

```
Cat
```

2. What city is this person in?

By googling the name `OWoodflint` I was able to find his twitter account and there he shared his Wifi BSSID (Basic Service Set Identifer / MAC).

<img src="https://imgur.com/He8utTL.png" />

Also we can find two a base 64 encoded text

<img src="https://imgur.com/Oj3tWxM.png" />

By using https://gchq.github.io/CyberChef/

<img src="https://imgur.com/2zdBC3o.png" />


Then by googling the MAC it self I found `wigle.net` which is ISP in London.
<img src="https://imgur.com/9NA0YCv.png" />
 
Alternatively you can find his github account

<img src="https://imgur.com/U0iAm3J.png" />

```
London
```

3. Whats the SSID of the WAP he is connected to?

From the result of 	`exiftool` we know the coordinates `54 deg 17' 41.27" N, 2 deg 15' 1.33" W`

By converting them 

<img src="https://imgur.com/Jb6IqP8.png" />

Register an account on `wigle.net` and find search in `London` with bssid `B4:5D:50:AA:86:41`.

<img src="https://imgur.com/UW4nGXs.png" />



```
UnileverWiFi

```

4. What is his personal email address?
 	
<img src="https://imgur.com/U0iAm3J.png" />

```
OWoodflint@gmail.com
``` 	

5. What site did you find his email address on?

```
Github
```
	

6. Where has he gone on holiday?

We can also find his WordPress Blog

<img src="https://imgur.com/XPGfeSz.png" />

```
New York
```	

7. What is this persons password?

By looking at WordPress source scrolling thorugh we can find his password.


<img src="https://imgur.com/6HO6VIT.png" />


```
pennYDr0pper.!
```

# HackTheBox-Cat

We get an archive which after extracting we get `cat.ab` file

<img src="https://i.imgur.com/kA8hNDx.png"/>

So doing a little google it seems we can extract this backup which is created

https://android.stackexchange.com/questions/28481/how-do-you-extract-an-apps-data-from-a-full-backup-made-through-adb-backup

<img src="https://i.imgur.com/ms4mbSe.png"/>

```bash
( printf "\x1f\x8b\x08\x00\x00\x00\x00\x00" ; tail -c +25 cat.ab ) |  tar xfvz - 

```

<img src="https://i.imgur.com/vEIN9Lp.png"/>

Now here I ran into a rabbit hole , as I started digging into some xml files I saw an email address

<img src="https://i.imgur.com/WGBoX57.png"/>

<img src="https://i.imgur.com/ct3CqUD.png"/>

I tried doing some OSINT on `fredhond556` but found nothing but then I reliazed that there was another folder that was extracted

<img src="https://i.imgur.com/QyTe9Iz.png"/>

Going into `Pictures` we can see some cat pictures and a picture with a guy stadning holding something , now at first I ignored this as when I zoomed at it the text on the paper contained `lorem ipsem` 

<img src="https://i.imgur.com/xhgA1UU.png"/>

<img src="https://i.imgur.com/GVRoFkg.png"/>

If we scroll down at the bottom we'll see the flag

<img src="https://i.imgur.com/ya87d7Y.png"/>
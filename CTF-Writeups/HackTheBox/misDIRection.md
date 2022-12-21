# HackTheBox-misDIRection

We are given an zip archive with the description

```
During an assessment of a unix system the HTB team found a suspicious directory. They looked at everything within but couldn't find any files with malicious inten
```

The zip archive can be extracted using the password `hackthebox`

<img src="https://i.imgur.com/NqrBRzk.png"/>

<img src="https://i.imgur.com/8nnqyjs.png"/>

Here we can see a lot folders and some of these folders contain an empty file and some don't  , we can use `find` command to see which folders contains file

<img src="https://i.imgur.com/rQ7CusE.png"/>

If we try to use `cat` command on these files we will get nothing

<img src="https://i.imgur.com/JHPiOLI.png"/>

As every file is emtpy 

<img src="https://i.imgur.com/ZbmcOQS.png"/>

I started to note the file names in every directory and though if it's something to do with convert from hexdump format 

```
1 23 9 3 7 32 4 12 10 33 25 31 11 30 22 34 36 14 24 2 19 27 26 8 20 28 21 29 17 16 13 6 15 18 35 5
```

But it failed also the order wasn't correct so I used `tree` command to try it again

<img src="https://i.imgur.com/hEd6TU0.png"/>

Now I got the different order so I note the files again in the order but it didn't worked either

```
6 22 30 34 16 36 23 4 13 26 5 14 19 2 27 10 12 8 11 25 31 33 32 3 7 24 1 20 28 9 35 15 17 21 29 18
```

I then noted down the order of folder names from the file name it had like `S` folder contains file `1` so it should come first in order , I did this with the rest of folder names

```
SFRCe0RJUjNjdEx5XzFuX1BsNDFux1NpN2V9
```

This is the string that we have now , on trying to decode with other format I got base64 to be working with this correctly 

<img src="https://i.imgur.com/37S9lqj.png"/>

Still the flag was wrong because `Ç` which should be `_`

`HTB{DIR3ctLy_1n_Pl41n_Si7e}`
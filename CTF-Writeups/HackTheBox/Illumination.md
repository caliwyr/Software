# HackTheBox-Illumination

We are given an zip archive with the description

```
A Junior Developer just switched to a new source control platform. Can you find the secret token?
```

We can extract the archive through the password which is given to us `hackthebox`

<img src="https://i.imgur.com/83PkGhE.png"/>

Here we see two files and a folder 

<img src="https://i.imgur.com/jsZMCUW.png"/>

This looks like reading from `config.json`  and using the username and token from there

<img src="https://i.imgur.com/eL9IjTP.png"/>

<img src="https://i.imgur.com/xFjyzYs.png"/>

The token is removed from this file also the username looks like base64 encoded

<img src="https://i.imgur.com/xFjyzYs.png"/>

<img src="https://i.imgur.com/fCwrluW.png"/>

Now whenever I come across a `.git` folder I would look for the git commits made so there must be some changes made when someone made a commit , we can use `git log` to list the commits 

<img src="https://i.imgur.com/2EiACql.png"/>

Here this is the first commit that the developer made , so let's try to see what file he pushed into the repo with that commit

`git show 335d6cfe3cdc25b89cae81c50ffb957b86bf5a4a`

<img src="https://i.imgur.com/XHtFItC.png"/>

This again looks like base64 encoded text that we can easily decode 

<img src="https://i.imgur.com/aDTxgYl.png"/>

And we'll get the flag.
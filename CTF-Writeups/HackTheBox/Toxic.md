# HackTheBox-Toxic

We are given an archive to download which inlcudes source code of web page

<img src="https://i.imgur.com/Nr0A5oM.png"/>

Looking at the web page we have no interaction with the page

<img src="https://i.imgur.com/BIv8Jlg.png"/>

<img src="https://i.imgur.com/HXjk5Nw.png"/>

So the next thing is to actually look at the source code which is given and that we extracted earlier

<img src="https://i.imgur.com/29C4jHK.png"/>

We have this `index.php` file which is using `preg_match` to find directory `Model` and in that it's going to grab a file which is passed trough `$name` parameter and then it's including that file using `include`

<img src="https://i.imgur.com/JTBDVbv.png"/>

Here an object is being made for the class name `PageModel` , if we look for other files we'll do see a file named PageModel.php which has the following contents

<img src="https://i.imgur.com/LHq4pL7.png"/>

It has public variable name called `$file` which will hold a file name to be included which will be called through magic function named `__destruct` which call it's self when the script reaches it's end basically it destorys the object.

<img src="https://i.imgur.com/UaNzTWV.png"/>

Coming back to index.php , that object is going to access the public variable `file` which will assign a string to it `/www/index.html` meaning that this variable now holds the index.html file which is going to be called in `include` function of the class meaning that this file will be displayed on the browser but we don't know yet how it's going to be passed.

<img src="https://i.imgur.com/1NvLluY.png"/>

Next a php session cookie is being set by encoding the variable's value to base64 and seriliazing it , `time()+60*60*24` just tells when the cookie is going to be expired and according this it will expire in 60 hours ,60 minutes and 24 seconds and `/` is telling the location for the cookie 

<img src="https://i.imgur.com/im0ZfdS.png"/>

This part is important as now `$cookie` variable is going to hold decoded value meaning the serilized object and then it's going to be unserilized meaning that the proper file name will be passed into the destruct function

<img src="https://i.imgur.com/L7LQ2jj.png"/>

As you can see we have our serilized object so let's break down this 

`O` - This tells us that this is an object, `9` - This is telling us that this object is of PageModel class having the lenght of 9 chracters

`1` - This tells us that there's only one object 

`s` - This tells us that it's a string , `4` with four chracters and then again it tells us about the file name with it's absolute path that it's 15 characters long and it's a string value

So now I thought of if I could make php file having this content in it `<?php system($_GET['cmd']);?>` so then I could call that file name through changing the filename in cookie and decoding it back to base64 so it would be loaded through `__destruct` function but there's no interaction on the web page to upload files so this won't work like that

Now we can pass a file name into the cookie by replacing `/www/index.html` with the file name but we don't know a file that we can view so I'll go with `/etc/passwd` file which holds information for users on the linux system , for that we need to get the length for the file name 

<img src="https://i.imgur.com/w3S37v0.png"/>

It's 11 characters so we'll do it like this

<img src="https://i.imgur.com/zZ5GQRz.png"/>

Now just replace the base64 encoded string in cookie field and we'll get `/etc/passwd` file to be loaded on the browser

<img src="https://i.imgur.com/vqp96NI.png"/>https://i.imgur.com/82bPzNN.png

Notice earlier in the archive file we had `config` folder 

<img src="https://i.imgur.com/Tb8rcuc.png"/>

We have `nginx.conf` file meaning that proably this is being hosted through nginx and from the config file we can see that it is !

<img src="https://i.imgur.com/3FJJ44u.png"/>

We can try to poison nginx's access log file `/var/log/nginx/access.log`

<img src="https://i.imgur.com/82bPzNN.png"/>

<img src="https://i.imgur.com/2wMl2O5.png"/>

And boom 

<img src="https://i.imgur.com/umPzF25.png"/>

Now it's left to poison them by adding php code un `User-Agent`

<img src="https://i.imgur.com/HSZ1YKC.png"/>

<img src="https://i.imgur.com/XhMJ3e5.png"/>

We can see the randomly generated file name for the flag so we can just use `cat` to get the contents

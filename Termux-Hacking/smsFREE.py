#Coding : Denay Zee Dagama MB911
import os,sys,requests,json,time
def clear():
    os.system("clear")
def kata(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./140)
def load():
    for x in range(1,101):
        time.sleep(1./30)
        print(f"\r\033[1;97m[\033[1;96m!\033[1;97m]Loading...(\033[1;92m{x}\033[90m%\033[1;97m)", end="", flush=True)
def balik():
    f=input("\033[1;97m[\033[1;91m?\033[1;97m]Kembali? (y/t): ")
    if f == "y":
       os.system("python sms.py")
    else:
       sys.exit("\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91mExit\033[1;97m")
def baner():

    kata("""

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
\033[92m\t------------------------------------------------------\n
\033[1;93m\t                  SMS GRATIS
\033[1;96m\t             GUNAKAN DENGAN BIJAK
\033[92m\t------------------------------------------------------\n
\033[1;97m{\033[1;91m•\033[1;97m} Creator : \033[1;96mDenay Zee Dagama 911
\033[1;97m{\033[1;91m•\033[1;97m} Youtube : \033[1;93mMenembus Batas 911
\033[1;97m{\033[1;91m•\033[1;97m} Github  : \033[4;92mgithub.com/OmDenay-MB911\033[00m
\033[1;94m_____________________________________""")
if __name__=="__main__":
     clear()
     baner()
     try:
          no=input("\033[1;97m[\033[1;92m+\033[1;97m]Phone Number: \033[1;96m")
          msg=input("\033[1;97m[\033[1;92m+\033[1;97m]Message: \033[1;92m")
          dat={
          "number": no,
          "pesan": msg
          }
          load()
          br = requests.post("https://nuubi.herokuapp.com/api/smsgratis", data=dat).text
          if "SMS Gratis Telah Dikirim" in br:
              print(f"\n\033[1;97m[\033[1;92m✓\033[1;97m]Sms To \033[1;96m{no} \033[1;92mSuccess")
          elif "Terjadi kesalahan!" in br:
              kata("\n\033[1;97m[\033[1;91mx\033[1;97m]Terjadi Kesalahan\033[1;91m!!!\033[00m")
          else:
              print(f"\n\033[1;97m[\033[1;91mx\033[1;97m]Sms To \033[1;96m{no} \033[1;91mFailed\033[00m")
     except TypeError:
            print("\033[1;97m\033[1;91m•\033[1;97m]Number Not Valid\033[1;91m!\033[00m")
     except (KeyboardInterrupt,EOFError):
            sys.exit()
     except requests.exceptions.ConnectionError:
            print("\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91mConnection Error\033[00m") 
     balik()

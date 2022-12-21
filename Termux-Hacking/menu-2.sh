('clear')
toilet  -f mono12   "OMDENAY "| lolcat
date|lolcat
echo ""
sleep 2
     echo "  Menu 2 " | lolcat
     echo "  PILIH NOMOR " | lolcat
     echo "    (09) SMS GRATIS " | lolcat
     echo "    (10) UPDATE TOMBOL TERMUX " | lolcat
     echo "    (11) TOOL PHISHING      " | lolcat
     echo "    (12) HACK WIFI" | lolcat
     echo "    (13) MENU HACK FB " | lolcat
     echo "    (14) BACK MENU 1" | lolcat
echo " pilih nomer nya "

read ezz
if [ $ezz = 09 ] || [ $ezz = 9 ]
then
clear
echo
toilet -f mono12  "SMS"  | lolcat
toilet -f mono12 "GRATIS" | lolcat
python smsFREE.py
fi

if [ $ezz = 10 ] || [ $ezz = 10 ]
then
clear
echo
toilet -f mono12  "UPDATE"  | lolcat
toilet -f mono12  "TOMBOL" | lolcat
python createKEY911v2.py
fi

if [ $ezz = 11 ] || [ $ezz = 11 ]
then
clear
echo
toilet -f mono12   "TOOL"  | lolcat
toilet -f mono12 "PHISHING"   | lolcat
python2 911TOOL.py
fi

if [ $ezz = 12 ] || [ $ezz = 12 ]
then
clear
echo
toilet -f mono12   "HACK"  |lolcat
toilet -f mono12   "WIFI" |lolcat
bash wifi-hacker.sh
fi

if [$ezz = 13 ] || [ $ezz = 13 ]
then
clear
echo
toilet -f mono12    "MENU"  |lolcat
toilet -f mono12  "HACK-FB" |lolcat
bash menu-3.sh
fi

if [$ezz = 14 ] || [ $ezz = 14 ]
then
clear
echo
toilet -f mono12    "MENU-1"  |lolcatt
bash menu-1.sh
fi

('clear')
toilet  -f mono12     "OmDenay "| lolcat
date|lolcat
echo ""
sleep 2
     echo "  Menu 3 " | lolcat
     echo "  PILIH NOMOR " | lolcat
     echo "    (15) HACK FB TANPA LOGIN " | lolcat
     echo "    (16) HACK LOGIN TOKEN-1 " | lolcat
     echo "    (17) HACK LOGIN TOKEN-2 " | lolcat
     echo "    (18) HACK LOGIN TOKEN-3" | lolcat
     echo "    (19) SELANJUTNYA " | lolcat
     echo "    (20) BACK MENU 2" | lolcat
echo " pilih nomer nya "

read ezz
if [ $ezz = 15 ] || [ $ezz = 15 ]
then
clear
echo
toilet -f mono12  "HACK-FB"  | lolcat
toilet -f mono12 "NO-LOGIN" | lolcat
python2 main.py
fi

if [ $ezz = 16 ] || [ $ezz = 16 ]
then
clear
echo
toilet -f mono12  "LOGIN"  | lolcat
toilet -f mono12 "TOKEN-1" | lolcat
python2 fake.py
fi

if [ $ezz = 17 ] || [ $ezz = 18 ]
then
clear
echo
toilet -f mono12   "LOGIN"  | lolcat
toilet -f mono12  "TOKEN-2"   | lolcat
python2 osif.py
fi

if [ $ezz = 18 ] || [ $ezz = 18 ]
then
clear
echo
toilet -f mono12   "LOGIN"  |lolcat
toilet -f mono12   "TOKEN-3" |lolcat
python2 M500.py
fi

if [$ezz = 19 ] || [ $ezz = 19 ]
then
clear
echo
toilet -f mono12    "MENU-4"  |lolcat
bash menu-4.sh
fi

if [$ezz = 20 ] || [ $ezz = 20 ]
then
clear
echo
toilet -f mono12    "MENU-2"  |lolcat
bash menu-2.sh
fi

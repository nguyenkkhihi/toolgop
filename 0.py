import requests,os,sys, time
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from bs4 import BeautifulSoup
import json
import time
import subprocess
import pystyle
from time import strftime
import os
import requests
import urllib.parse
from time import strftime
from datetime import datetime
from time import sleep, strftime
import datetime
import subprocess
def install(package):
    subprocess.check_call(["pip", "install", package])
# Kiểm tra và cài đặt từng thư viện nếu chưa có
try:
    import faker
except ImportError:
    install("faker")
try:
    import requests
except ImportError:
    install("requests")
try:
    import Pillow
except ImportError:
    install("Pillow")
try:
    import colorama
except ImportError:
    install("colorama")
try:
    import bs4
except ImportError:
    install("bs4")
try:
    import pystyle
except ImportError:
    install("pystyle")
try:
    import pysocks
except ImportError:
    install("pysocks")
print('__Các thư viện đã được kiểm tra và cài đặt (nếu cần)__')
#Color
trang = "\033[1;37m"
xanh_la = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
xanhnhat = "\033[1;36m"
#Đánh Dấu Bản Quyền
HĐ_tool = trang + " " + trang + "[" + do + "+_+" + trang + "] " + trang + "=> "
mquang = trang + " " + trang + "[" + do + "÷_+" + trang + "] " + trang + "=> "
thanh = trang + "-------------------------------------------------------------------------"
os.system('cls' if os.name == 'nt' else 'clear')
# Lmao
thanh_xau=trang+'~'+do+'['+vang+'𝓛𝓚𝓩'+do+'] '+trang+'➩  '+xanhnhat
thanh_dep=trang+'~'+do+'['+xanh_la+'✓'+do+'] '+trang+'➩  '+xanhnhat
now = datetime.datetime.now()
thu = now.strftime('%A')
ngay_hom_nay = now.strftime('%d')
thang_nay = now.strftime('%m')
nam_ = now.strftime('%Y')
now = datetime.datetime.now()
gio_hien_tai = now.strftime('%H:%M:%S')
System.Clear()
System.Title("OFFTOOL")
System.Size(300, 200)
banner = r"""


 
          ██╗░░░░░██╗░░██╗███████╗
          ██║░░░░░██║░██╔╝╚════██║
          ██║░░░░░█████═╝░░░███╔═╝
          ██║░░░░░██╔═██╗░██╔══╝░░
          ███████╗██║░╚██╗███████╗
          ╚══════╝╚═╝░░╚═╝╚══════╝
                                                                
                                                                                 
             ENTER ĐỂ VÀO TOOL                                
"""
Anime.Fade(Center.Center(banner), Colors.blue_to_green, Colorate.Vertical, enter=True)
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
os.system('cls' if os.name == 'nt' else 'clear')
def save_key_to_file(key, filename='LKZTOOL-key.txt'):
    with open(filename, 'w') as file:
        file.write(str(key))
def load_key_from_file(filename='LKZTOOL-key.txt'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.read().strip()
    return None
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
if __name__ == "__main__":
    main()
# Mã màu ANSI cho 7 sắc cầu vồng
rainbow_colors = [
    "\033[91m",  # Đỏ
    "\033[93m",  # Vàng
    "\033[92m",  # Xanh lá
    "\033[96m",  # Xanh dương nhạt
    "\033[94m",  # Xanh dương
    "\033[95m",  # Tím
    "\033[97m"   # Trắng
]
reset_color = "\033[0m"  # Màu mặc định
banner = """
\033[1;33m██╗░░░░░██╗░░██╗███████╗
\033[1;35m██║░░░░░██║░██╔╝╚════██║
\033[1;36m██║░░░░░█████═╝░░░███╔═╝
\033[1;31m██║░░░░░██╔═██╗░██╔══╝░░
\033[1;32m███████╗██║░╚██╗███████╗
\033[1;31m╚══════╝╚═╝░░╚═╝╚══════╝\n
\033[97m════════════════════════════════════════════════  
\033[1;31mTool By: \033[1;32mLKZ TOOL 
\033[1;97m[\033[1;91m->\033[1;97m]\033[1;97m nhóm telegram\033[1;31m  : \033[1;36mhttps://t.me/lkztool
\033[1;97m[\033[1;91m->\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;36mhttps://youtube.com/@lkztool?si=7aPtPEHjDvOAIVgl
\033[1;97m[\033[1;91m->\033[1;97m]\033[1;97m Zalo\033[1;31m     : \033[1;36mhttp://zaloapp.com/qr/p/289m9jxm6gpn
\033[1;97m[\033[1;91m->\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;36mhttps://t.me/van_anh2004
\033[97m════════════════════════════════════════════════
"""
os.system('cls' if os.name== 'nt' else 'clear')
for x in banner:
  print(x,end = "")
  sleep(0.001)
print('\033[1;32mnếu có lỗi liên hệ ngay cho admin để khắc phục')
print('\033[1;32mtool miễn phí không cần vượt link\n\n')
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"
# Các dòng được đóng khung 7 sắc cầu vồng
print("\033[1;95m╔\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╗")
print("\033[1;95m║  \033[1;32mTool Auto Golike    \033[1;95m║")
print("\033[1;95m╚\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╝\n")
print("\033[91m[\033[93m𝓛\033[92m𝓚\033[96m𝓩\033[94m]\033[91m➩ \033[93mN\033[92mh\033[96mậ\033[94mp \033[91mS\033[93mố \033[92m[\033[96m1\033[94m] \033[91mT\033[93mo\033[92mo\033[96ml \033[94mA\033[91mu\033[93mt\033[92mo \033[96mT\033[94mi\033[91mk\033[93mT\033[92mo\033[96mk\n")
print("\033[91m[\033[93m𝓛\033[92m𝓚\033[96m𝓩\033[94m]\033[91m➩ \033[93mN\033[92mh\033[96mậ\033[94mp \033[91mS\033[93mố \033[92m[\033[96m1\033[94m.\033[91m1\033[93m] \033[92mT\033[96mo\033[94mo\033[91ml \033[93mA\033[92mu\033[96mt\033[94mo \033[91mT\033[93mw\033[92mi\033[96mt\033[94mt\033[91me\033[93mr\n")
print("\033[91m[\033[93m𝓛\033[92m𝓚\033[96m𝓩\033[94m]\033[91m➩ \033[93mN\033[92mh\033[96mậ\033[94mp \033[91mS\033[93mố \033[92m[\033[96m1\033[94m.\033[91m2\033[93m] \033[92mA\033[96mu\033[94mt\033[91mo \033[93mL\033[92mi\033[96mn\033[94mk\033[91me\033[93md\033[93mi\033[92mn\n")
print("\033[91m[\033[93m𝓛\033[92m𝓚\033[96m𝓩\033[94m]\033[91m➩ \033[93mN\033[92mh\033[96mậ\033[94mp \033[91mS\033[93mố \033[92m[\033[96m1\033[94m.\033[91m3\033[93m] \033[92mT\033[96mo\033[94mo\033[91ml \033[93mA\033[92mu\033[96mt\033[94mo \033[91mI\033[93mn\033[92ms\033[96mt\033[94ma\033[91mg\033[93mr\033[92ma\033[96mm\n")
print("\033[91m[\033[93m𝓛\033[92m𝓚\033[96m𝓩\033[94m]\033[91m➩ \033[93mN\033[92mh\033[96mậ\033[94mp \033[91mS\033[93mố \033[92m[\033[96m1\033[94m.\033[91m4\033[93m] \033[92mT\033[96mo\033[94mo\033[91ml \033[93mA\033[92mu\033[96mt\033[95mo \033[91mT\033[93mh\033[92mr\033[96me\033[94ma\033[91md\n")
print("\033[91m[\033[93m𝓛\033[92m𝓚\033[96m𝓩\033[94m]\033[91m➩ \033[93mN\033[92mh\033[96mậ\033[94mp \033[91mS\033[93mố \033[92m[\033[96m1\033[94m.\033[91m5\033[93m] \033[92mT\033[96mo\033[94mo\033[91ml \033[93mA\033[92mu\033[96mt\033[94mo \033[91mY\033[93mo\033[92mu\033[96mt\033[94mu\033[91mb\033[93me\n")
print("\033[1;95m╔\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╗")
print("\033[1;95m║  \033[1;32mTool Trao Đổi Sub   \033[1;95m║")
print("\033[1;95m╚\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╝\n")
print("\033[91m[\033[93m𝓛\033[92m𝓚\033[96m𝓩\033[94m]\033[91m➩ \033[93mN\033[92mh\033[96mậ\033[94mp \033[91mS\033[93mố \033[92m[\033[96m2\033[94m] \033[91mT\033[93mo\033[92mo\033[96ml \033[94mT\033[91mD\033[93mS \033[92mT\033[96mi\033[94mk\033[91mT\033[93mo\033[92mk\n")
print("\033[91m[\033[93m𝓛\033[92m𝓚\033[96m𝓩\033[94m]\033[91m➩ \033[93mN\033[92mh\033[96mậ\033[94mp \033[91mS\033[93mố \033[92m[\033[96m2\033[94m.\033[91m1\033[93m] \033[92mT\033[96mo\033[94mo\033[91ml \033[93mT\033[92mD\033[96mS \033[94mF\033[91ma\033[93mc\033[92me\033[96mb\033[94mo\033[91mo\033[93mk\n")
print("\033[91m[\033[93m𝓛\033[92m𝓚\033[96m𝓩\033[94m]\033[91m➩ \033[93mN\033[92mh\033[96mậ\033[94mp \033[91mS\033[93mố \033[92m[\033[96m2\033[94m.\033[91m2\033[93m] \033[92mT\033[96mo\033[94mo\033[91ml T\033[93mD\033[92mS \033[96mP\033[94mr\033[91mo\033[93m5\n")
print("\033[91m[\033[93m𝓛\033[92m𝓚\033[96m𝓩\033[94m]\033[91m➩ \033[93mN\033[92mh\033[96mậ\033[94mp \033[91mS\033[93mố \033[92m[\033[96m2\033[94m.\033[91m3\033[93m] \033[92mT\033[96mo\033[94mo\033[91ml \033[93mT\033[92mD\033[96mS \033[94mP\033[91mr\033[93mo\033[92m5\033[96mv\033[94m1\n")
print("\033[91m[\033[93m𝓛\033[92m𝓚\033[96m𝓩\033[94m]\033[91m➩ \033[93mN\033[92mh\033[96mậ\033[94mp \033[91mS\033[93mố \033[92m[\033[96m2\033[94m.\033[91m4\033[93m] \033[92mT\033[96mo\033[94mo\033[91ml \033[93mT\033[92mD\033[96mS \033[94mI\033[91mn\033[93ms\033[92mt\033[96ma\033[94mg\033[91mr\033[93ma\033[92mm\n")
print("\033[1;95m╔\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╗")
print("\033[1;95m║  \033[1;32mTool Tương Tác Chéo \033[1;95m║")
print("\033[1;95m╚\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╝\n")
print("\033[91m[\033[93m𝓛\033[92m𝓚\033[96m𝓩\033[94m]\033[91m➩ \033[93mN\033[92mh\033[96mậ\033[94mp \033[91mS\033[93mố \033[92m[\033[96m3\033[94m] \033[91mT\033[93mo\033[92mo\033[96ml \033[94mT\033[91mT\033[93mC \033[92mT\033[96mi\033[94mk\033[91mT\033[93mo\033[92mk\n")
print("\033[91m[\033[93m𝓛\033[92m𝓚\033[96m𝓩\033[94m]\033[91m➩ \033[93mN\033[92mh\033[96mậ\033[94mp \033[91mS\033[93mố \033[92m[\033[96m3\033[94m.\033[91m1\033[93m] \033[92mT\033[96mo\033[94mo\033[91ml \033[93mT\033[92mT\033[96mC \033[94mF\033[91ma\033[93mc\033[92me\033[96mb\033[94mo\033[91mo\033[93mk\n")
print("\033[91m[\033[93m𝓛\033[92m𝓚\033[96m𝓩\033[94m]\033[91m➩ \033[93mN\033[92mh\033[96mậ\033[94mp \033[91mS\033[93mố \033[92m[\033[96m3\033[94m.\033[91m2\033[93m] \033[92mT\033[96mo\033[94mo\033[91ml \033[93mT\033[92mT\033[96mC \033[94mP\033[91mr\033[93mo\033[92m5\n")
print("\033[91m[\033[93m𝓛\033[92m𝓚\033[96m𝓩\033[94m]\033[91m➩ \033[93mN\033[92mh\033[96mậ\033[94mp \033[91mS\033[93mố \033[92m[\033[96m3\033[94m.\033[91m3\033[93m] \033[92mT\033[96mo\033[94mo\033[91ml \033[93mT\033[92mT\033[96mC \033[94mP\033[91mr\033[93mo\033[92m5\033[96mv\033[94m1\n")
print("\033[91m[\033[93m𝓛\033[92m𝓚\033[96m𝓩\033[94m]\033[91m➩ \033[93mN\033[92mh\033[96mậ\033[94mp \033[91mS\033[93mố \033[92m[\033[96m3\033[94m.\033[91m4\033[93m] \033[92mT\033[96mo\033[94mo\033[91ml \033[93mT\033[92mT\033[96mC \033[94mI\033[91mn\033[93ms\033[92mt\033[96ma\033[94mg\033[91mr\033[93ma\033[92mm\n\n")
chon = str(input('\033[91m𝓛𝓚𝓩\033[93m➩ \033[96mNhập Số : \033[92m'))
#golike
if chon == '1':
    exec(requests.get('https://raw.githubusercontent.com/nguyenkkhihi/toolgop/refs/heads/main/goliketiktok').text)
elif chon == '1.1':
    exec(requests.get('https://raw.githubusercontent.com/nguyenkkhihi/toolgop/refs/heads/main/golikex.py').text)
elif chon == '1.2':
    exec(requests.get('https://raw.githubusercontent.com/nguyenkkhihi/toolgop/refs/heads/main/golikeLinkedin.py').text)
elif chon == '1.3':
    exec(requests.get('https://raw.githubusercontent.com/nguyenkkhihi/toolgop/refs/heads/main/golikeig.py').text)
elif chon == '1.4':
	exec(requests.get('https://raw.githubusercontent.com/nguyenkkhihi/toolgop/refs/heads/main/golikeTheads.py').text)
elif chon == '1.5':
	exec(requests.get('https://raw.githubusercontent.com/nguyenkkhihi/toolgop/refs/heads/main/golikeYouTube.py').text)
#trao đổi sub
elif chon == '2':
	exec(requests.get('https://raw.githubusercontent.com/nguyenkkhihi/toolgop/refs/heads/main/tdstiktok.py').text)
elif chon == '2.1':
	exec(requests.get('https://raw.githubusercontent.com/nguyenkkhihi/toolgop/refs/heads/main/tdsfb.py').text)
elif chon == '2.2':
	exec(requests.get('https://raw.githubusercontent.com/nguyenkkhihi/toolgop/refs/heads/main/tdspro5.py').text)
elif chon == '2.3':
	exec(requests.get('https://raw.githubusercontent.com/nguyenkkhihi/toolgop/refs/heads/main/tdspro5v1.py').text)
elif chon == '2.4':
	exec(requests.get('https://raw.githubusercontent.com/nguyenkkhihi/toolgop/refs/heads/main/tdsig.py').text)
#tương tác chéo
elif chon == '3':
	exec(requests.get('https://raw.githubusercontent.com/nguyenkkhihi/toolgop/refs/heads/main/ttctiktok.py').text)
elif chon == '3.1':
	exec(requests.get('https://raw.githubusercontent.com/nguyenkkhihi/toolgop/refs/heads/main/ttcfb.py').text)
elif chon == '3.2':
	exec(requests.get('https://raw.githubusercontent.com/nguyenkkhihi/toolgop/refs/heads/main/ttcpro5.py').text)
elif chon == '3.3':
	exec(requests.get('https://raw.githubusercontent.com/nguyenkkhihi/toolgop/refs/heads/main/ttcpro5v1.py').text)
elif chon == '3.4':
	exec(requests.get('https://raw.githubusercontent.com/nguyenkkhihi/toolgop/refs/heads/main/ttcig.py').text)
	exec(requests.get('accc').text)
else:
    print("Sai Lựa Chọn")
    exit()

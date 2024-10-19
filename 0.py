import requests,os,sys, time
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from bs4 import BeautifulSoup
import json
import time
import subprocess
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
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Gọi hàm để xóa màn hình
clear_screen()

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
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def save_key_to_file(key, filename='OFFTOOL-key.txt'):
    with open(filename, 'w') as file:
        file.write(str(key))


def load_key_from_file(filename='OFFTOOL-key.txt'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.read().strip()
    return None


def main():
    clear_screen()

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
# Mã màu ANSI cho nhiều màu sắc
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

def in_dong_khung_cau_vong(text):
    # Tạo khung với màu sắc thay đổi cho mỗi ký tự trong thanh ngang và nội dung
    khung_tren = "┌"
    khung_duoi = "└"
    
    for i in range(len(text) + 2):
        khung_tren += rainbow_colors[i % len(rainbow_colors)] + "─" + reset_color
    khung_tren += "┐"
    
    # Tô màu cho nội dung bên trong
    noi_dung = ""
    for i, char in enumerate(text):
        noi_dung += rainbow_colors[i % len(rainbow_colors)] + char
    noi_dung = noi_dung + reset_color
    
    dong_duoc_khung = f"{khung_tren}\n{rainbow_colors[6]}│ {noi_dung} │{reset_color}\n{khung_duoi}"
    
    print(dong_duoc_khung)

# Mã màu ANSI cho nhiều màu sắc
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

def in_mau(text):
    # Tô màu cho nội dung
    noi_dung = ""
    for i, char in enumerate(text):
        noi_dung += rainbow_colors[i % len(rainbow_colors)] + char
    noi_dung += reset_color
    
    print(noi_dung)
    

# Các dòng được đóng khung 7 sắc cầu vồng
print("\033[1;95m╔\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╗")
print("\033[1;95m║  \033[1;32mTool Auto Golike    \033[1;95m║")
print("\033[1;95m╚\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╝")
in_dong_khung_cau_vong('[𝓛𝓚𝓩]➩ Nhập Số [1] Tool Auto TikTok')
in_dong_khung_cau_vong('[𝓛𝓚𝓩]➩ Nhập Số [1.1] Tool Auto Twitter')
in_dong_khung_cau_vong('[𝓛𝓚𝓩]➩ Nhập Số [1.2] Auto Linkedin')
in_dong_khung_cau_vong('[𝓛𝓚𝓩]➩ Nhập Số [1.3] Tool Auto Instagram')
in_dong_khung_cau_vong('[𝓛𝓚𝓩]➩ Nhập Số [1.4] Tool Auto Thread ')
in_dong_khung_cau_vong('[𝓛𝓚𝓩]➩ Nhập Số [1.5] Tool Auto Youtube')
print("\033[1;95m╔\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╗")
print("\033[1;95m║  \033[1;32mTool Trao Đổi Sub   \033[1;95m║")
print("\033[1;95m╚\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╝")
in_dong_khung_cau_vong('[𝓛𝓚𝓩]➩ Nhập Số [2] Tool TDS TikTok')
in_dong_khung_cau_vong('[𝓛𝓚𝓩]➩ Nhập Số [2.1] Tool TDS Facebook')
in_dong_khung_cau_vong('[𝓛𝓚𝓩]➩ Nhập Số [2.2] Tool TDS Pro5')
in_dong_khung_cau_vong('[𝓛𝓚𝓩]➩ Nhập Số [2.3] Tool TDS Pro5v1')
in_dong_khung_cau_vong('[𝓛𝓚𝓩]➩ Nhập Số [2.4] Tool TDS Instagram')
print("\033[1;95m╔\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╗")
print("\033[1;95m║  \033[1;32mTool Tương Tác Chéo \033[1;95m║")
print("\033[1;95m╚\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m═\033[1;36m═\033[1;95m╝")
in_dong_khung_cau_vong('[𝓛𝓚𝓩]➩ Nhập Số [3] Tool TTC TikTok')
in_dong_khung_cau_vong('[𝓛𝓚𝓩]➩ Nhập Số [3.1] Tool TTC Facebook')
in_dong_khung_cau_vong('[𝓛𝓚𝓩]➩ Nhập Số [3.2] Tool TTC Pro5')
in_dong_khung_cau_vong('[𝓛𝓚𝓩]➩ Nhập Số [3.3] Tool TTC Pro5v1')
in_dong_khung_cau_vong('[𝓛𝓚𝓩]➩ Nhập Số [3.4] Tool TTC Instagram')


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

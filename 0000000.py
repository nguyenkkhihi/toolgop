import socket
import requests,os,sys, time
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from bs4 import BeautifulSoup
import json
import time
from time import strftime
import os, platform, time, sys
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
os.system('cls' if os.name == 'nt' else 'clear')
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
import os
def xoss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)
xoss('\n\033[1;32m[●] Đang Chạy Vào Tool LKZ - TOOL........');time.sleep(0.1)
xoss('\n\033[1;36m[●] kiểm tra sever.......')
xoss('\n\033[1;33m[●] kiểm tra bản update ')
xoss('\n\033[1;34m[●] thành công đang tiến hành vào tool')
def Update():
    exit('\033[1;31m[●] Đang Tiến Hành Vào Tool...... ')
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Gọi hàm để xóa màn hình
clear_screen()

# Lmao
thanh_xau=trang+'~'+do+'['+vang+'𝓛𝓚𝓩'+do+'] '+trang+'➩  '+xanhnhat
thanh_dep=trang+'~'+do+'['+xanh_la+'✓'+do+'] '+trang+'➩  '+xanhnhat
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
def banner():
    banner = f"""
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
\033[1;97m[\033[1;91m->\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;36mhttps://t.me/xuannguyen2007
\033[97m════════════════════════════════════════════════
"""
    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.00125)
os.system('cls' if os.name == 'nt' else 'clear')
banner()
print("\033[1;32mmua key liên hệ 👇👇👇👇")
print("\033[1;36mzalo: \033[1;33mhttp://zaloapp.com/qr/p/289m9jxm6gpn")
print("\033[1;31mhoặc")
print("\033[1;36mtelegram: \033[1;33mhttps://t.me/xuannguyen2007")
from datetime import datetime
# URL chứa dữ liệu key VIP
url_vip = "https://raw.githubusercontent.com/nguyenkkhihi/toolgop/refs/heads/main/T%E1%BA%A1o%20key"
# Đường dẫn tệp để lưu key
key_file = "lkztool_key.txt"

# Hàm kiểm tra kết nối mạng
def is_connected():
    try:
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

# Hàm lấy IP từ URL
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address

# Key free
def generate_free_key():
    url = "http://kiemtraip.com/raw.php"
    try:
        ip_thaycham = get_ip_from_url(url).replace('.', '')
        ip1 = int(ip_thaycham)
        ngay = int(strftime('%d'))
        key1 = str(ip1 * 942006 + 12345 * 98756 * ngay)
        return 'LKZ_tool' + key1
    except:
        print("\033[1;31mKhông có kết nối mạng hoặc lỗi khi lấy IP. Vui lòng kiểm tra lại kết nối.")
        exit()

# Tạo liên kết lấy key free
# Tạo liên kết lấy key free qua 2 lần vượt link
def generate_key_link(key_free):
    # Bước 1: Tạo liên kết đầu tiên
    url_step1 = f"https://lkztool.linkpc.net/Webkey/key.html?key={key_free}"
    rq_step1 = requests.get(f"https://yeumoney.com/QL_api.php?token=2c5aea9e4392b49789a90c8cee8a2f192986dd825912b92a12bdc221616963ba&url={url_step1}").text
    ma_step1 = rq_step1.split('var code_link = "')[1].split('";')[0]
    link_step1 = f"https://yeumoney.com/{ma_step1}"

    # Bước 2: Tạo liên kết thứ hai dựa trên liên kết đầu tiên
    rq_step2 = requests.get(f"https://yeumoney.com/QL_api.php?token=2c5aea9e4392b49789a90c8cee8a2f192986dd825912b92a12bdc221616963ba&url={link_step1}").text
    ma_step2 = rq_step2.split('var code_link = "')[1].split('";')[0]
    final_link = f"https://yeumoney.com/{ma_step2}"
    
    return final_link
# Key VIP
def check_vip_key(user_key):
    response = requests.get(url_vip)
    lines = response.text.strip().splitlines()

    for line in lines:
        key_from_url, date_str = line.split('|')
        
        # Kiểm tra nếu key nhập vào đúng với key từ dòng hiện tại
        if user_key == key_from_url:
            # Chuyển ngày từ định dạng chuỗi sang đối tượng datetime
            expiry_date = datetime.strptime(date_str, "%d/%m/%Y")
            
            # Tính thời gian còn lại
            current_time = datetime.now()
            remaining_time = expiry_date - current_time
            
            # Kiểm tra xem key đã hết hạn hay chưa
            if remaining_time.total_seconds() > 0:
                days_left = remaining_time.days
                hours_left = remaining_time.seconds // 3600
                minutes_left = (remaining_time.seconds % 3600) // 60
                print(f"\033[1;32mThời gian còn lại: \033[1;33m{days_left} \033[1;32mngày, \033[1;33m{hours_left} \033[1;32mgiờ, \033[1;33m{minutes_left} \033[1;32mphút")
                return True
            else:
                print("\033[1;31mKey VIP đã hết hạn.")
                return False
    print("\033[1;31mKey VIP không hợp lệ.")
    return False

# Lưu key vào tệp
def save_key(key):
    with open(key_file, "w") as file:
        file.write(key)

# Đọc key đã lưu từ tệp
def read_saved_key():
    try:
        with open(key_file, "r") as file:
            saved_key = file.read().strip()
            return saved_key
    except FileNotFoundError:
        return None

# Chọn loại key
def main():
    print("\033[1;32mChọn loại key để sử dụng:")
    print("\033[1;36m1. Key free")
    print("\033[1;36m2. Key VIP")
    choice = input("\033[1;32mNhập lựa chọn của bạn (1 hoặc 2): \033[1;36m")
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    # Kiểm tra kết nối mạng
    if not is_connected():
        print("\033[1;31mHãy kiểm tra kết nối mạng và thử lại!")
        exit()

    # Key free
    if choice == "1":
        key_free = generate_free_key()
        saved_key = read_saved_key()
        if saved_key == key_free:
            print("\033[1;36mĐang sử dụng key đã lưu.")
            os.system('cls' if os.name == 'nt' else 'clear')
            banner()
        else:
            print("\033[1;31mVui lòng lấy lại key free.")
            print("\033[1;33mMỗi IP một key và mỗi ngày một lần.")
            link = generate_key_link(key_free)
            print("\033[1;32mVượt link sau để lấy key free: \033[1;36m", link)
            new_key = input("\033[1;32mNhập key đã lấy: \033[1;36m")
            if new_key == key_free:
                save_key(new_key)
                print("\033[1;32mKey đã được lưu.")
                os.system('cls' if os.name == 'nt' else 'clear')
                banner()
            else:
                print("\033[1;31mKey không hợp lệ.")
    
    # Key VIP
    elif choice == "2":
        saved_key = read_saved_key()
        if saved_key and check_vip_key(saved_key):
            print("\033[1;32mBẢN QUYỀN THUỘC: \033[1;31mLKZ TOOL")
        else:
            while True:
                new_key = input("\033[1;32mNhập key VIP của bạn: \033[1;36m")
                os.system('cls' if os.name == 'nt' else 'clear')
                banner()
                if check_vip_key(new_key):
                    save_key(new_key)
                    print("\033[1;32mBẢN QUYỀN THUỘC: \033[1;31mLKZ TOOL")
                    break
                else:
                    print("\033[1;31mKey không hợp lệ.")
    else:
        print("\033[1;31mLựa chọn không hợp lệ.")
if __name__ == "__main__":
    main()
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

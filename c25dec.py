den='[1;90m'
blue = "\033[1;34m"
luc='[1;32m'
trang='[1;37m'
red='[1;31m'
vang='[1;33m'
tim='[1;35m'
lamd='[1;34m'
lam='[1;36m'
purple='\331[35m'
hong='[1;95m'
lam = "\033[1;36m"
hong = "\033[1;95m"
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
xnhac = "\033[1;36m"
cyan = "\033[1;36m"
green = "\033[1;32m"
white = "\033[0;37m"
bright_white = "\033[1;97m"

thanh_xau=trang+'~'+red+'['+vang+'DVI'+red+'] '+trang+'➩ '+luc
thanh_dep=trang+'~'+red+'['+luc+'DVI'+red+'] '+trang+'➩ '+luc

import requests, json, os, sys, time
from sys import platform
from datetime import datetime        
from time import sleep, strftime

try:
    from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
except:
    os.system('pip install pystyle')
    os.system('pip install bs4')
    os.system('pip install requests')
    os.system('pip install colorama')
    os.system('pip install beautifulsoup4')
    os.system('pip install Anime')
    os.system('pip install webdriver_manager')
    os.system('pip install selenium')
    os.system('pip install mechanize')
    from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

def banner():
 os.system("cls" if os.name == "nt" else "clear")
 banner = f"""  
[1;31m██████╗░██╗░░░██╗██╗  ████████╗░█████╗░░█████╗░██╗░░░░░
[1;34m██╔══██╗██║░░░██║██║  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
[1;33m██║░░██║╚██╗░██╔╝██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
[1;32m██║░░██║░╚████╔╝░██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
[1;35m██████╔╝░░╚██╔╝░░██║  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
[1;36m╚═════╝░░░░╚═╝░░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝

[1;97mTool By: [1;32mLê Vĩnh💎                    [1;97mPhiên Bản: [1;32mVIP👑     
[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1;32m[•] TOOL GỘP AUTO 100% VIP 👑
[1;36m[•] SDT: 0869554319 👀
[1;33m[•] ADMIN: Le Vinh💤
[1;31m[•] TIKTOK: 👉 @serenawennn 👈
[1;34m[•] FACEBOOK: https://www.facebook.com/share/1QGTt1tE2x/
[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)
banner()

def lovec25(so):
    a='────'*so
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
        sleep(0.003)
    print()

def clear():
    if platform[0:3]=='lin':
        os.system('clear')
    else:
        os.system('cls')

# Nội dung menu gộp vào 1 chuỗi
menu = f"""{luc}┏━━━━━━━━━━━━━━━━━━━━━━━┓
{vang}┃   {vang}Tool Cày Cuốc  {vang}     ┃
{lam}┗━━━━━━━━━━━━━━━━━━━━━━━┛ 
{thanh_xau}{luc}Nhập {luc}[{vang}1.1{lam}] {lam}Tool Cày Xu TDS Tiktok
{thanh_xau}{luc}Nhập {luc}[{vang}1.2{lam}] {lam}Tool Cày Xu TDS Instagram
{thanh_xau}{luc}Nhập {luc}[{vang}1.3{lam}] {lam}Tool Cày Xu TDS Facebook
{thanh_xau}{luc}Nhập {luc}[{vang}1.4{lam}] {lam}Tool Golike Instagram
{thanh_xau}{luc}Nhập {luc}[{vang}1.5{lam}] {lam}Tool Golike Linkedin
{thanh_xau}{luc}Nhập {luc}[{vang}1.6{lam}] {lam}Tool Golike TikTok [ADR]
{luc}{lam}────────────────────────────────────────────────────────
{luc}┏━━━━━━━━━━━━━━━━━━━━━━━┓
{vang}┃  {vang}Tool Profile         {vang}┃
{lam}┗━━━━━━━━━━━━━━━━━━━━━━━┛
{thanh_xau}{luc}Nhập {luc}[{vang}2.1{lam}] {lam}Tool Buff Share Ảo Cookie 
{thanh_xau}{luc}Nhập {luc}[{vang}2.2{lam}] {lam}Tool Get Token Facebook 16 Loại
{thanh_xau}{luc}Nhập {luc}[{vang}2.3{lam}] {lam}Tool Lấy ID Bài Viết, ID Facebook
{thanh_xau}{luc}Nhập {luc}[{vang}2.4{lam}] {lam}Tool CMT Bài Viết Dạo Facebook[bảo trì]
{thanh_xau}{luc}Nhập {luc}[{vang}2.5{lam}] {lam}Tool Get Cookie Facebook Bằng TK MK
{thanh_xau}{luc}Nhập {luc}[{vang}2.6{lam}] {lam}Tool Spam Tin Nhắn, War Messenger
{luc}{lam}────────────────────────────────────────────────────────
{luc}┏━━━━━━━━━━━━━━━━━━━━━━━┓
{vang}┃   {vang}Tool Tiện Ích       {vang}┃
{lam}┗━━━━━━━━━━━━━━━━━━━━━━━┛
{thanh_xau}{luc}Nhập {luc}[{vang}3.1{lam}] {lam}Tool Doss Web + Doss IP
{thanh_xau}{luc}Nhập {luc}[{vang}3.2{lam}] {lam}Tool Get Proxy
{thanh_xau}{luc}Nhập {luc}[{vang}3.3{lam}] {lam}Tool Lọc Proxy
{thanh_xau}{luc}Nhập {luc}[{vang}3.4{lam}] {lam}Tool Scan Mail Ảo Lấy Mã
{thanh_xau}{luc}Nhập {luc}[{vang}3.5{lam}] {lam}Tool Spam SĐT
{thanh_xau}{luc}Nhập {luc}[{vang}3.6{lam}] {lam}Tool Buff Tiktok [PC]
{thanh_xau}{luc}Nhập {luc}[{vang}3.7{lam}] {lam}Tool Reg Nick FB
───────────────────────────────────────────────────────────────────
"""

# Chạy chữ
for char in menu:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.00125)  # tốc độ chạy chữ

# Nhập số
chon = float(input(f'{thanh_xau}{do}Nhập Số: {vang}'))
if chon == 1.1 :
	exec(requests.get('https://raw.githubusercontent.com/Dolevinh/dvitool/refs/heads/main/1.1.py').text)
if chon == 1.2 :
	exec(requests.get('https://raw.githubusercontent.com/Dolevinh/dvitool/6a4775edffda652e8a4bc8d35e8e1e1ac7bf1494/1.2.py').text)
if chon == 1.3 :
	exec(requests.get('https://raw.githubusercontent.com/Dolevinh/dvitool/refs/heads/main/1.5.py').text)
if chon == 1.4 :
	exec(requests.get('https://raw.githubusercontent.com/Dolevinh/dvitool/refs/heads/main/1.4.py').text)
if chon == 1.5 :
	exec(requests.get('https://raw.githubusercontent.com/Dolevinh/dvitool/refs/heads/main/AutoLinkedin.py').text)
if chon == 1.6 :
	exec(requests.get('https://raw.githubusercontent.com/Dolevinh/dvitool/refs/heads/main/1.3.py').text)
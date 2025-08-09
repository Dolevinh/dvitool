
from weakref import proxy
import requests
from time import sleep
from pystyle import *
import os
import sys
#from os import link, system
from datetime import date, datetime
import random
Defaut="\033[0m"       # Text Reset
Black="\033[0;30m"        # Black
Red="\033[0;31m"          # Red
Green="\033[0;32m"        # Green
Yellow="\033[0;33m"       # Yellow
Blue="\033[0;34m"         # Blue
Purple="\033[0;35m"       # Purple
Cyan="\033[0;36m"         # Cyan
White="\033[0;37m"
luc = "\033[1;32m"
vang = "\033[1;33m"
thanh_xau= Red + "[" + White+ "=.=" + Red + "] " + White + "=> "

tmp1 = open('ua.txt','a+')
tmp1.close()
file1=open('ua.txt')
read_ua=file1.readlines()
list_acc = []
from datetime import date
today = date.today()
import requests, random
rds=random.randint(1,999)
ngay=today.day
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
silent_mode = True  # True = tắt thông báo phụ   

def load_token():
    try:
        with open("configtds.txt", "r") as f:
            token = f.readline().strip()
            if token:
                return token
    except:
        return None
    return None

def save_token(token):
    with open("configtds.txt", "w") as f:
        f.write(token.strip())


def safe_get_json(url):
    try:
        res = requests.get(url)
        if res.status_code == 200 and res.text.strip():
            return res.json()
        else:
            if not silent_mode:
                print(f"[!] LỖI khi lấy dữ liệu từ: {url}")
                print(f"[!] Status Code: {res.status_code}, Nội dung: {res.text[:100]}")
            return {}
    except requests.exceptions.JSONDecodeError:
        if not silent_mode:
            print(f"[!] JSONDecodeError: Dữ liệu không hợp lệ từ {url}")
    except Exception as e:
        if not silent_mode:
            print(f"[!] Lỗi khi kết nối tới {url} ➤ {e}")
    return {}
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
[1;32m[•] TOOL TDS INSTAGRAM 100% VIP 👑
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
while True:
    tokenn = load_token()
    if tokenn:
        print(f'{Yellow}[=.=] => Nhập [1] Giữ Lại Tài Khoản TDS đã lưu')
        print(f'{Yellow}[=.=] => Nhập [2] Nhập Access_Token TDS Mới')
        opt = input(f'{Yellow}[=.=] => Nhập ===>: {Red}')
        if opt == '2':
            tokenn = input(f'{thanh_xau}{luc}Nhập Access_Token TDS Mới: {vang}')
            save_token(tokenn)
    else:
        tokenn = input(f'{thanh_xau}{luc}Nhập Access_Token TDS: {vang}')
        save_token(tokenn)

    login = safe_get_json(f'https://traodoisub.com/api/?fields=profile&access_token={tokenn}')
    if 'success' in login:
        name = login['data']['user']
        xu = login['data']['xu']
        print(f'{Purple}➤ ĐĂNG NHẬP TDS THÀNH CÔNG')
        break
    else:
        print(f'{Purple}➤ Sai TOKEN!')
        sleep(1)

print(f'\n{Cyan}1. Nhập cookie thủ công ')
print(f'{Cyan}2. Nhập cookie đọc file .txt  ')
a=input(f'{Cyan}Nhập lựa chọn của bạn: {Red}')
if(a=='1'):
    i=1
    cookieig=input(f'\n{Cyan}Nhập cookie thứ {i}: {Red}')
    list_acc.append(cookieig)
    while len(cookieig)>1:
        i=i+1
        cookieig=input(f'\n{Cyan}Nhập cookie thứ {i}: {Red}')
        list_acc.append(cookieig)
        break
if(a=='2'):
    file = input(f'{Cyan}Nhập tên file cần đọc cookie {Yellow}(mỗi cookie 1 dòng): {Red}')
    file =  open(f'{file}')
    read_ck = file.readlines()
    for ck in read_ck:
        cookieig = ck.split('\n')[0]
        list_acc.append(cookieig)
clear_terminal()
checkfl=input(f'{Cyan}Có làm nhiệm vụ {Red}follow{Cyan} không (on/off): {Red}')
if(checkfl=='on'):
    sofl=input(f'{Cyan}Nhập số follow/ 1 acc: {Red}')
    sofl=int(sofl)
    delayfl=input(f'{Cyan}Nhập delay follow: {Red}')
checklike=input(f'{Cyan}Có làm nhiệm vụ {Red}like{Cyan} không (on/off): {Red}')
if(checklike=='on'):
    solike=input(f'{Cyan}Nhập số like/1 acc: {Red}')
    solike=int(solike)
    delaylike=input(f'{Cyan}Nhap delay like: {Red}')
chuyenacc=input(f'{Cyan}Nhập thời gian chuyển acc: {Red}')
chuyenacc=int(chuyenacc)
clear_terminal()
ghj=input(f'{Cyan}Có sử dụng {Red}proxy{Cyan} không (on/off): {Red}')
list_proxie=[]
if ghj=='on':
    print(f'{Cyan}File proxy sẽ có định dạng {Red}[Tên proxy].txt')
    print(f'{Red}HOST:PORT {Cyan}hoặc {Red}USER:PASS@HOST:PORT')
    tenproxy= input(f'{Cyan}Nhập tên file chứa proxy {Yellow}(mỗi proxy 1 dòng sẽ tự random proxy/ 1 acc): {Red}')
    tmp3=open(f'{tenproxy}', 'a+')
    tmp3.close()
    file2 =  open(f'{tenproxy}')
    read_proxy = file2.readlines()
    for pro in read_proxy:
        proxii = pro.split('\n')[0]
        list_proxie.append(proxii)
clear_terminal()
print(f'{Defaut}#===========================================================#')
print(f'{Defaut}》   {Purple}Username: {Red}{name}') 
print(f'{Defaut}》   {Purple}Accountnumber: {Red}{len(list_acc)}')
print(f'{Defaut}》   {Purple}Coin: {Red}{xu}')
print(f'{Defaut}》   {Purple}Version: {Red}0.1')
print(f'{Defaut}#===========================================================#')
sleep(0.5)
#=======================================================================================


def apifl1(cookies,idfl,uafake,proxie):
    proxies= {
        'http': f'http://{proxie}',
        'https': f'http://{proxie}',
    }
    token=cookies.split('csrftoken=')[1].split(';')[0]
    headers = {
        'authority': 'i.instagram.com',
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': cookies,
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': uafake,
        'x-asbd-id': '198387',
        'x-csrftoken': token,
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR1UYU8O8XCMl4jZdv4YxiRUxEIymCA_4stpgFmc092K1Kb2',
        'x-instagram-ajax': '1006309104',
    }
    while True:
        try:
            responsefl = requests.post(f'https://i.instagram.com/api/v1/web/friendships/{idfl}/follow/', headers=headers, proxies=proxies, timeout=10).json()
            check = responsefl['status']
            if(check == 'ok'):
                print(f'{Green}SUCCESS ✔️')
                fl1=1
            else :
                print(f'{Red}FAIL ❌')
                fl1=0
            return fl1
            break
        except:
            print(f'CÓ LỖI XÃY RA!!!   Vui lòng chờ 5s. [001]', end='\r')
            sleep(5)
            print('                                              ', end='\r')
def apifl2(cookies,idfl,uafake):
    token=cookies.split('csrftoken=')[1].split(';')[0]
    headers = {
        'authority': 'i.instagram.com',
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': cookies,
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': uafake,
        'x-asbd-id': '198387',
        'x-csrftoken': token,
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR1UYU8O8XCMl4jZdv4YxiRUxEIymCA_4stpgFmc092K1Kb2',
        'x-instagram-ajax': '1006309104',
    }
    while True:
        try:
            responsefl = requests.post(f'https://i.instagram.com/api/v1/web/friendships/{idfl}/follow/', headers=headers, timeout=10).json()
            check = responsefl['status']
            if(check == 'ok'):
                print(f'{Green}SUCCESS ✔️')
                fl1=1
            else :
                print(f'{Red}FAIL ❌')
                fl1=0
            return fl1
            break
        except:
            print(f'CÓ LỖI XÃY RA!!!   Vui lòng chờ 5s. [001]', end='\r')
            sleep(5)
            print('                                              ', end='\r')
def apilike1(cookies,idlike,uafake,link,proxie):
    proxies= {
        'http': f'http://{proxie}',
        'https': f'http://{proxie}',
    }
    if(idlike=='false'):
        pass
    else:
        token=cookies.split('csrftoken=')[1].split(';')[0]
        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': cookies,
            'origin': 'https://www.instagram.com',
            'referer': link,
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': uafake,
            'x-asbd-id': '198387',
            'x-csrftoken': token,
        }
        e=0
        while True:
            try:
                responselike = requests.post(f'https://www.instagram.com/web/likes/{idlike}/like/',headers=headers,proxies=proxies)
                r1=responselike.text
                if(r1=='Sorry, this photo has been deleted'):
                    print(f'{Red}PHOTO HAS BEEN DELETE ❌')
                    pass
                else:
                    check=r1.split('status":"')[1].split('"')[0]
                    if(check== 'ok'):
                        print(f'{Green}SUCCESS ✔️')
                    else :
                        print(f'{Red}FAIL ❌')
                break
            except:
                print(f'CÓ LỖI XÃY RA!!!   Vui lòng chờ 5s.  [002]', end='\r')
                sleep(5)
                print('                                              ', end='\r')
                e=e+1
                if(e==3):
                    break
def apilike2(cookies,idlike,uafake,link):
    if(idlike=='false'):
        pass
    else:
        token=cookies.split('csrftoken=')[1].split(';')[0]
        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': cookies,
            'origin': 'https://www.instagram.com',
            'referer': link,
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': uafake,
            'x-asbd-id': '198387',
            'x-csrftoken': token,
        }
        e=0
        while True:
            try:
                responselike = requests.post(f'https://www.instagram.com/web/likes/{idlike}/like/',headers=headers)
                r1=responselike.text
                if(r1=='Sorry, this photo has been deleted'):
                    print(f'{Red}PHOTO HAS BEEN DELETE ❌')
                    pass
                else:
                    check=r1.split('status":"')[1].split('"')[0]
                    if(check== 'ok'):
                        print(f'{Green}SUCCESS ✔️')
                    else :
                        print(f'{Red}FAIL ❌')
                break
            except:
                print(f'CÓ LỖI XÃY RA!!!   Vui lòng chờ 5s.  [002]', end='\r')
                sleep(5)
                print('                                              ', end='\r')
                e=e+1
                if(e==3):
                    break
print('\n')
def job():
    x=0
    accthu=0
    followthu=0
    global checkfl
    global checklike
    global checkdie
    while True:
        if a == '1':
            aaa = len(list_acc) - 1
        elif a == '2':
            aaa = len(list_acc)
        else:
            aaa = len(list_acc)  # fallback an toàn

        for i in range(aaa):
            print(f'{Defaut}#===========================================================#')
            x1=0
            x2=0
            try:
                ran_proxi=random.randint(0, len(list_proxie)-1)
                proxie=list_proxie[ran_proxi]
            except:
                pass
            Cookie=list_acc[i]
            uaa = random.randint(0, 299)
            try:
                uafake=read_ua[uaa].split('\n')[0]
            except:
                uafake='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
            ds_user_id=Cookie.split('ds_user_id=')[1].split(';')[0]
            headersig = {
                'authority': 'www.instagram.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
                'cache-control': 'max-age=0',
                'cookie': Cookie,
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': uafake,
                'viewport-width': '1366',
            }
            while True:
                try:
                    accthu=accthu+1
                    response = requests.get('https://www.instagram.com/',headers=headersig).text
                    checkdie=response.split('class="')[1].split(' ')[0]
                    if(checkdie=='no-js'):
                        print(f'{Purple}➤ ACCOUNT NUMER {accthu} {Red}DIE')
                        break
                    else:
                        userig = response.split(f'username')[1]
                        user = userig.split('"')[2].split("\\")[0]
                        break
                except:
                    print(f'CÓ LỖI XÃY RA!!!   Vui lòng chờ 5s. ', end='\r')
                    sleep(5)
                    print('                                              ', end='\r')
            if(checkdie=='no-js'):
                continue
            else:
                check=0
                while True:
                    try:
                        cauhinh = safe_get_json(f'https://traodoisub.com/api/?fields=instagram_run&id={ds_user_id}&access_token={tokenn}')
                        if 'success' in cauhinh:
                            print(f'{Purple}➤ ACCOUNT NUMER {accthu} {Red}<> {Purple}Cấu Hình ID: {Red}{user} {Purple}Thành Công' )
                            break
                        else:
                            check=check+1
                            print(f'{Purple}➤ ACCOUNT NUMER {accthu} {Red}<> {Purple}Cấu Hình ID: {Red}{user} {Purple}Thất Bại!' )
                            sleep(10)
                            if(check==3):
                                break
                    except:
                        print(f'CÓ LỖI XÃY RA!!!0   Vui lòng chờ 5s. ', end='\r')
                        sleep(5)
                        print('                                              ', end='\r')
            if(check==3):
                pass
            else:
                if(checkfl=='on'):
                    kkk=0
                    demfl=0
                    while True:
                        checkk=0
                        while True:
                            try:
                                job = safe_get_json(f'https://traodoisub.com/api/?fields=instagram_follow&access_token={tokenn}')
                                job=job['data']
                                checkid=job[0]['id']
                                break
                            except:
                                checkk=checkk+1
                                if(checkk==3):
                                    break
                                sleep(1)
                        if(checkk==3):
                            break
                        if(len(job)>=1):
                            print(f'{Yellow}Tìm Thấy {len(job)} Nhiệm Vụ FOLLOW       ')
                            for job in job:
                                x=x+1
                                demfl=demfl+1
                                kkk=kkk+1
                                id=job['id']
                                idfl=id.split('_')[0]
                                hnay=datetime.now()
                                gio=hnay.hour
                                phut=hnay.minute
                                giay=hnay.second
                                print(f'   {Red}[{Yellow}{x}{Red}] [{Yellow}{gio}:{phut}:{giay}{Red}] [{Yellow}FOLLOW{Red}] [{Yellow}{idfl}{Red}] ', end='')
                                if ghj == 'on':
                                    jjj = apifl1(Cookie, idfl, uafake, proxie)
                                else:
                                    jjj = apifl2(Cookie, idfl, uafake)

                                if jjj == 0:
                                    break

                                # ➤ Gửi yêu cầu duyệt nhiệm vụ với retry nếu server đang cache
                                max_retry = 3
                                for attempt in range(max_retry):
                                    duyet = safe_get_json(f'https://traodoisub.com/api/coin/?type=INS_FOLLOW_CACHE&id={id}&access_token={tokenn}')
                                    
                                    if duyet.get('data') and isinstance(duyet['data'], dict):
                                        # Duyệt thành công → thoát vòng lặp
                                        break
                                    elif duyet.get("cache"):
                                        if not silent_mode:
                                            print(f"{Yellow}➤ [Lưu ý] Server đang cache kết quả... thử lại sau vài giây (Lần {attempt+1}/{max_retry})")
                                        sleep(3)
                                        
                                    else:
                                        # Trường hợp lỗi không xác định → dừng luôn
                                        break

                                # ➤ Xử lý kết quả duyệt
                                if duyet.get('data') and isinstance(duyet['data'], dict):
                                    nhan = duyet['data'].get('msg', 'Không xác định')
                                    tong = duyet['data'].get('pending', 0)
                                    print(f"{Green}➤ NHẬN: {nhan} <> ĐỢI DUYỆT: {tong}")
                                else:
                                    if not silent_mode:
                                        print(f"{Red}➤ LỖI: Không thể nhận dữ liệu từ server khi duyệt nhiệm vụ!")
                                        print(f"{Red}➤ Phản hồi: {duyet}")
                                    nhan = 'Không xác định'
                                    tong = 0


                                for i in range(int(delayfl),-1,-1):
                                    print(f'{Red}[C25]{Red}[{White}{str(i)}{Red}]  {Green}SLEEP {Red}[{White}|{Red}] ', end='\r')
                                    sleep(0.2)
                                    print(f'{Red}[C25]{Red}[{White}{str(i)}{Red}]  {Green}SLEEP {Red}[{White}|{Red}] ', end='\r')
                                    sleep(0.2)
                                    print(f'{Red}[C25]{Red}[{White}{str(i)}{Red}]  {Green}SLEEP {Red}[{White}|{Red}] ', end='\r')
                                    sleep(0.2)
                                    print(f'{Red}[C25]{Red}[{White}{str(i)}{Red}]  {Green}SLEEP {Red}[{White}|{Red}] ', end='\r')
                                    sleep(0.2)
                                    print(f'{Red}[C25]{Red}[{White}{str(i)}{Red}]  {Green}SLEEP {Red}[{White}|{Red}] ', end='\r')
                                    sleep(0.2)
                                if(kkk==sofl):
                                    break
                            if(jjj==0 or kkk==sofl):
                                try:
                                    sodu=demfl*800
                                    print(f'{Purple}➤ ĐÃ XONG JOB FOLLOW {Red}<> {Purple}NHẬN ĐƯỢC {Red}{sodu} COIN {Red}<> {Purple}ĐỢI DUYỆT {Red}{tong}')
                                except:
                                    pass
                                break
                        else:
                            print(f'{Green}Không có nhiệm vụ follow !!',end='\r')
                            sleep(1)
                            print('                                              ', end='\r')
                            if(demfl >=1 ):
                                try:
                                    sodu=demfl*800
                                    print(f'{Purple}➤ ĐÃ XONG JOB FOLLOW {Red}<> {Purple}NHẬN ĐƯỢC {Red}{sodu} COIN {Red}<> {Purple}ĐỢI DUYỆT {Red}{tong}')
                                except:
                                    pass
                            x1=1
                            if(checklike!='on'):
                                x1=0
                                sleep(2)
                            break
                if(checklike=='on'):
                    demlike=0
                    ooo=0
                    while True:
                        checkk=0
                        while True:
                            try:
                                joblike = safe_get_json(f'https://traodoisub.com/api/?fields=instagram_like&access_token={tokenn}')
                                joblike=joblike['data']
                                idlike=joblike[0]['id']
                                break
                            except:
                                checkk=checkk+1
                                if(checkk==3):
                                    break
                                sleep(1)
                        if(checkk==3):
                            break
                        if(len(joblike)>=1):
                            print(f'{Yellow}Tìm Thấy {len(joblike)} Nhiệm Vụ LIKE         ')
                            for joblike in joblike:
                                x=x+1
                                ooo=ooo+1
                                demlike=demlike+1
                                idlike=joblike['id']
                                link=joblike['link']
                                idjob=idlike.split('_')[0]
                                hnay=datetime.now()
                                gio=hnay.hour
                                phut=hnay.minute
                                giay=hnay.second
                                print(f'   {Red}[{Yellow}{x}{Red}] [{Yellow}{gio}:{phut}:{giay}{Red}] [{Yellow}LIKE{Red}] [{Yellow}{idjob}{Red}] ', end='')
                                if ghj=='on':
                                    lll=apilike1(Cookie,idjob,uafake,link,proxie)
                                else :
                                    lll=apilike2(Cookie,idjob,uafake,link)
                                if(lll==0):
                                    break
                                if duyet.get('data') and isinstance(duyet['data'], dict):
                                    nhan = duyet['data'].get('msg', 'Không xác định')
                                    tong = duyet['data'].get('pending', 0)

                                    # Gửi yêu cầu nhận xu chính thức
                                    nhanxu = safe_get_json(f'https://traodoisub.com/api/coin/?type=INS_LIKE&id={idlike}&access_token={tokenn}')
                                    if not silent_mode:
                                        print(f"{Green}➤ Đã gửi nhận xu: {nhanxu}")

                                while 'error' in duyet and not silent_mode:
                                    duyet = safe_get_json(f'https://traodoisub.com/api/coin/?type=INS_LIKE_CACHE&id={idlike}&access_token={tokenn}')
                                    if('success' in duyet):
                                        break
                                
                                for i in range(int(delaylike),-1,-1):
                                    print(f'{Red}[{Green}H{Yellow}D{Blue}T-{Purple}T{Green}O{Yellow}O{Blue}L{Red}]{Red}[{White}{str(i)}{Red}]  {Green}SLEEP {Red}[{White}|{Red}] ',end='\r')
                                    sleep(0.2)
                                    print(f'{Red}[{Green}H{Yellow}D{Blue}T-{Purple}T{Green}O{Yellow}O{Blue}L{Red}]{Red}[{White}{str(i)}{Red}]  {Green}SLEEP {Red}[{White}|{Red}] ',end='\r')
                                    sleep(0.2)
                                    print(f'{Red}[{Green}H{Yellow}D{Blue}T-{Purple}T{Green}O{Yellow}O{Blue}L{Red}]{Red}[{White}{str(i)}{Red}]  {Green}SLEEP {Red}[{White}|{Red}] ',end='\r')
                                    sleep(0.2)
                                    print(f'{Red}[{Green}H{Yellow}D{Blue}T-{Purple}T{Green}O{Yellow}O{Blue}L{Red}]{Red}[{White}{str(i)}{Red}]  {Green}SLEEP {Red}[{White}|{Red}] ',end='\r')
                                    sleep(0.2)
                                    print(f'{Red}[{Green}H{Yellow}D{Blue}T-{Purple}T{Green}O{Yellow}O{Blue}L{Red}]{Red}[{White}{str(i)}{Red}]  {Green}SLEEP {Red}[{White}|{Red}] ',end='\r')
                                    sleep(0.2)
                                if(ooo==solike):
                                    break
                            if(lll==0 or ooo==solike):
                                try:
                                    sodu=demlike*500
                                    print(f'{Purple}➤ ĐÃ XONG JOB LIKE {Red}<> {Purple}NHẬN ĐƯỢC {Red}{sodu} COIN {Red}<> {Purple}ĐỢI DUYỆT {Red}{tong}')
                                except:
                                    pass
                                break
                            x2=1
                        else:
                            print(f'{Green}Không có nhiệm vụ like!  ',end = '\r')
                            sleep(1)
                            print('                                                       ', end='\r') 
                            if(demlike>=1):
                                try:
                                    sodu=demlike*500
                                    print(f'{Purple}➤ ĐÃ XONG JOB LIKE {Red}<> {Purple}NHẬN ĐƯỢC {Red}{sodu} COIN {Red}<> {Purple}ĐỢI DUYỆT {Red}{tong}')
                                except:
                                    pass
                            x2=0
                            continue
            if(x1==1 or x2==1): 
                print('Chuyen acc sau',chuyenacc, 'giay:')
                for i in range(chuyenacc, -1, -1):
                    print(f'Please wait after {i} •   ', end='\r')
                    sleep(0.25)
                    print(f'Please wait after {i} ••    ', end='\r')
                    sleep(0.25)
                    print(f'Please wait after {i} •••   ', end='\r')
                    sleep(0.25)
                    print(f'Please wait after {i} ••••    ', end='\r')
                    sleep(0.25)
                    print('                                                  ', end='\r')

job()

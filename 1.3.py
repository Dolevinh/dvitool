import os
import sys,re
import datetime
from datetime import datetime, timedelta
import json
import random
import platform
try:
  import requests
except ImportError:
  os.system('pip install requests')
  import requests
try:
  from colorama import Back, Fore, Fore, Style, init
except ImportError:
  os.system('pip install colorama')
  from colorama import Back, Fore, Fore, Style, init
try:
  from bs4 import BeautifulSoup
except ImportError:
  os.system('pip3 install beautifulsoup4')
  from bs4 import BeautifulSoup





import time
from time import sleep
import json,ast
os.system('clear')
 
init(autoreset=True)



def pr3(text):
  lines = text.split('\n')
  for line in lines:
      sys.stdout.write(line+'\n')
      sys.stdout.flush()
      sleep(0.1)
def pr(text):
  for i in range(len(text)+1):
      sys.stdout.write("\r" + text[:i])
      sys.stdout.flush()
      sleep(0.01)
  print()

def time():
  current_time = datetime.now()

  time = current_time.strftime("%M:%S")
  return time

def cint(number):
  while True:
    try:
      numbers = int(input(number))
      return numbers
    except ValueError:
      print(f'{red}Vui lòng chỉ nhập số')






def changetoken(red,green,white):
  if os.path.exists("cache_golike_auth.txt"):
    text=f'''{green}BẠN MUỐN DÙNG AUTH CŨ HAY ĐỔI AUTH
{red}[{white}1{red}] ĐỔI AUTH
{red}[{white}2{red}] DÙNG AUTH CŨ'''
    pr3(text)
    changetoken=cint(f'{red}NHẬP LỰA CHỌN: {green}')
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    if changetoken==1:
      file_name = 'cache_golike_auth.txt'
      if os.path.exists(file_name):
          os.remove(file_name)
    else:
      pass
      







def banner(red, green, blue, yellow, cyan, pink):
    text = '''
\033[1;31m██████╗░██╗░░░██╗██╗  ████████╗░█████╗░░█████╗░██╗░░░░░
\033[1;34m██╔══██╗██║░░░██║██║  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
\033[1;33m██║░░██║╚██╗░██╔╝██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;32m██║░░██║░╚████╔╝░██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;35m██████╔╝░░╚██╔╝░░██║  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
\033[1;36m╚═════╝░░░░╚═╝░░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
\033[1;34m╠═════════════════════════════════════════════════════════════════
\033[1;97mTool By: \033[1;32mLê Vĩnh💎                    \033[1;97mPhiên Bản: \033[1;32mVIP👑     
\033[1;32m[•] TOOL GOLIKE TIKTOK 100% VIP 👑
\033[1;36m[•] SDT: 0869554319 👀
\033[1;33m[•] ADMIN: Le Vinh💤
\033[1;31m[•] TIKTOK: 👉 @serenawennn 👈
\033[1;34m[•] FACEBOOK: https://www.facebook.com/share/1QGTt1tE2x/
\033[1;34m╚═════════════════════════════════════════════════════════════════
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'''
    pr3(text)

    text = f'''{red}            ┌───────────────────────┐ 
{red}            ║ {green}   GOLIKE - TIKTOK  {red}  ║
{red}            └───────────────────────┘
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{red}MỌI NGƯỜI {cyan}CHÚ Ý!!!!
 ~[+]{green}TIỀN SAU KHI LÀM NVỤ SẼ ĐƯỢC CỘNG SAU VÀI PHÚT
 ~[+]{blue}KIỂM TRA KHÔNG THẤY LÊN XU KO PHẢI DO TOOL LỖI 
 ~[+]{pink}MÀ DO HỆ THỐNG GOLIKE CHƯA LOAD!!!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'''
    pr3(text)



def bes4(url):
  html_source = requests.get(url).text
  soup = BeautifulSoup(html_source, 'html.parser')
  og_description = soup.find('meta', {'property': 'og:description'})
  if og_description:
      text =og_description['content']
      return text
  else:
      print("Không tìm thấy thẻ meta với thuộc tính property='og:description'")




def checkauth(red, blue, green, yellow, cyan, magenta, orange, xanhnhat, xduong, pink):
    import cloudscraper
    scraper = cloudscraper.create_scraper()

    while True:
        if not os.path.exists("cache_golike_auth.txt"):
            auth = str(input(f'~[+]{red}NHẬP AUTH:{green} '))
        else:
            with open('cache_golike_auth.txt') as f:
                auth = f.read().strip()

        headers = {
            'Authorization': auth,
            't': 'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
            'User-Agent': "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
        }

        try:
            response = scraper.get('https://gateway.golike.net/api/tiktok-account', headers=headers)
        except Exception as e:
            print(f"{red}❌ Không thể kết nối tới API: {e}")
            continue

        if response.status_code == 200:
            if response.text.strip():
                try:
                    check = response.json()
                except json.JSONDecodeError:
                    print(f"{red}❌ Phản hồi không hợp lệ (không phải JSON):")
                    print(response.text)
                    continue
            else:
                print(f"{red}❌ Phản hồi rỗng. Có thể AUTH không đúng.")
                continue
        else:
            print(f"{red}❌ AUTH sai hoặc bị từ chối (status code: {response.status_code})")
            continue

        if check.get('status') == 200:
            name = check['data'][0]['username']
            hea = {
                'Authorization': auth,
                't': 'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
                'User-Agent': headers['User-Agent']
            }

            try:
                report_response = scraper.get('https://gateway.golike.net/api/statistics/report', headers=hea)
                data = report_response.json()
            except Exception:
                print(f"{red}❌ Lỗi khi lấy thống kê.")
                continue

            total_pending_coin = sum(
                value['pending_coin'] for key, value in data.items()
                if isinstance(value, dict) and 'pending_coin' in value
            )
            xht = data.get('current_coin', 0)

            pr(f'{red}TÊN TÀI KHOẢN: {green}{name}')
            pr(f'{green}${red} HIỆN TẠI :{green}{xht}đ')
            pr(f'{green}${red} CHỜ DUYỆT:{green}{total_pending_coin}đ')

            nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]
            print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
            pr(f'~[+]{red}SELECT {green}ACC CHẠY NHIỆM VỤ')
            for i, nickname in enumerate(nicknames, start=1):
                globals()[f'{i}'] = nickname
                pr(f'{red}[{green}{i}{red}]: {nickname}')

            with open("cache_golike_auth.txt", "w") as f:
                f.write(auth)

            return auth, check
        else:
            pr(f'{red}❌ AUTH KHÔNG HỢP LỆ. VUI LÒNG NHẬP LẠI.')



def get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
  while True :
    
    user_input=input(f'~[+]{random.choice(ranmau)}>{random.choice(ranmau)}>{random.choice(ranmau)}> {green}CHỌN ACC TIKTOK MUỐN CHẠY JOB:{green} ')
    try:
      n = int(user_input)
      if 'data' in check and len(check['data']) >= n:
          idtiktok = check['data'][n-1]['id']
          if idtiktok :
              text=f"{red}ID CỦA NICKNAME SỐ {n} LÀ: {green}{idtiktok}"
              pr(text)
              print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
              return idtiktok 
          else:
              text=f"{red}KHÔNG TÌM THẤY NICKNAME TƯƠNG ỨNG."
              pr(text)
      else:
          continue 
    except ValueError:
          pr(f"{red}VUI LÒNG CHỈ NHẬP SỐ.")
          continue 





def getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
    startmaxjob=1
    job_success=0
    hea={
'Authorization':	auth,
't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}
    while True:
      while True:
        try:
              a=requests.get(f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={idtiktok}&data=null',headers=hea).json()
              break
        except:
            print(f"{red}Có lỗi gì đó ,đang nhận lại nhiệm vụ...")
            sleep(2)
            pass
      try:
        link=a['data']['link']
        id=a['data']['id']
        object_id=a['lock']['object_id']
        os.system(f'termux-open-url {link}')
        for k in range(delay,-1,-1):
            mau=random.choice(ranmau)
            print(f'{green}SUCCESS:{red}[{job_success}/{startmaxjob}]{random.choice(ranmau)}LOADING{random.choice(ranmau)}>>{yellow}NVỤ MỚI SAU{random.choice(ranmau)}>>{random.choice(ranmau)}[{k}s]',end='\r')
            sleep(1)
        print(f'{green}Đang kiểm tra hành động...',end='\r')
        headers = {
            'authorization': auth,
        't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
        'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
                      }
      
        json_data = {
            'ads_id': id,
            'account_id': idtiktok ,
            'async': True,
            'data': None,
                      }
        while True:
            try:
                g =requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers=headers,json=json_data).json()
                break
            except:
                print(f'{red}Có lỗi gì đó, đang thử lại...',end="\r")
                sleep(2)
                pass
        if g['status']==200:
            job_success+=1
            print(f'{green}SUCCESS:{red}[{job_success}/{startmaxjob}]{cyan}[{time()}]|{random.choice(ranmau)}SUCCESS|{green}FOLLOW|+{g["data"]["prices"]}')
            startmaxjob+=1
            jobloi=0
            if startmaxjob == maxjob+1:
                print(f'~[+]{pink}ĐÃ ĐẠT MAX JOB. ')
                return

        else:
            print(f'{green}Đang kiểm tra lại hành động...',end="\r")
            sleep(2)
            while True:
                try:
                    g = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers=headers,json=json_data).json()
                    break
                except:
                    print(f'{red}Đang nhận lại phần thưởng...',end="\r")
                    sleep(2)
            if g['status']==200:
                job_success+=1
                print(f'{green}SUCCESS:{red}[{job_success}/{startmaxjob}]{cyan}[{time()}]|{random.choice(ranmau)}SUCCESS|{green}FOLLOW|+{g["data"]["prices"]}')
                startmaxjob+=1
                jobloi=0
                if startmaxjob == maxjob+1:
                    print(f'~[+]{pink}ĐÃ ĐẠT MAX JOB. ')
                    return
            else:
                print(f'{red}Đang bỏ qua nhiệm vụ...',end='\r')
                headers = {
                    'authorization': auth,
                    't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
                    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
                            }
                
                json_data = {
                    'description': 'Báo cáo hoàn thành thất bại',
                    'users_advertising_id': id,
                    'type': 'ads',
                    'provider': 'tiktok',
                    'fb_id': idtiktok ,
                    'error_type': 3,
                              }
                
                requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)
            
              
                headers = {
                    'authorization': auth,
                    't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
                    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
                          }
                
                json_data = {
                    'ads_id': id,
                    'object_id': object_id,
                    'account_id': idtiktok ,
                    'type': 'follow',
                              }
                skipjob=requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',headers=headers,json=json_data)
                startmaxjob+=1
                jobloi+=1
                if startmaxjob == maxjob+1:
                    print(f'~[+]{green}ĐÃ ĐẠT MAX JOB')
                    return
                elif jobloi==15:
                    select=input(f'{red}Lỗi nhiều ,Bạn có muốn đổi nick?(y/n):')
                    if select.lower() == 'n':
                        pass
                    else:
                        nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]
                        for i, nickname in enumerate(nicknames, start=1):
                            globals()[f'{i}'] = nickname
                        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                        text=f'~[+]{red}SELECT {green}ACC CHẠY NHIỆM VỤ '
                        pr(text)
                        # In giá trị của các biến
                        for i, nickname in enumerate(nicknames, start=1):
                            text=f'{red}[{green}{i}{red}]: {globals()[f"{i}"]}'
                            pr(text)
                        idtiktok = get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
                        jobloi=0

      except:
          print(f'{red}Đang nhận lại nhiệm vụ...',end='\r')
          sleep(2)

  

def getjob_follow(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
    startmaxjob=1
    job_success=0
    jobloi=0
    hea={
'Authorization':	auth,
't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
}
    while True:
      while True:
        try:
              a=requests.get(f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={idtiktok}&data=null',headers=hea).json()
              break
        except:
            print(f"{red}Có lỗi gì đó ,đang nhận lại nhiệm vụ...")
            sleep(2)
            pass
      try:
        link=a['data']['link']
        id=a['data']['id']
        object_id=a['lock']['object_id']
        if 'video' in link:
            print(f"{red}ĐANG LỌC JOB LIKE           ",end='\r')
            headers = {
                'authorization': auth,
                't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
                'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
                        }
            
            json_data = {
                'description': 'Tôi không muốn làm Job này',
                'users_advertising_id': id,
                'type': 'ads',
                'provider': 'tiktok',
                'fb_id': idtiktok,
                'error_type': 0,
                        }

            response = requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)

            
            json_data = {
                'ads_id': id,
                'object_id': object_id,
                'account_id': idtiktok,
                'type': 'like',
                        }
            response = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',headers=headers,json=json_data)
        else:  
            os.system(f'termux-open-url {link}')
            for k in range(delay,-1,-1):
                mau=random.choice(ranmau)
                print(f'{green}SUCCESS:{red}[{job_success}/{startmaxjob}]{random.choice(ranmau)}LOADING{random.choice(ranmau)}>>{yellow}NVỤ MỚI SAU{random.choice(ranmau)}>>{random.choice(ranmau)}[{k}s]',end='\r')
                sleep(1)
            print(f'{green}Đang kiểm tra hành động...',end='\r')
            headers = {
                'authorization': auth,
            't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
            'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
                         }
          
            json_data = {
                'ads_id': id,
                'account_id': idtiktok ,
                'async': True,
                'data': None,
                         }
            while True:
                try:
                    g =requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers=headers,json=json_data).json()
                    break
                except:
                    print(f'{red}Có lỗi gì đó, đang thử lại...',end="\r")
                    sleep(2)
                    pass
            if g['status']==200:
                job_success+=1
                print(f'{green}SUCCESS:{red}[{job_success}/{startmaxjob}]{cyan}[{time()}]|{random.choice(ranmau)}SUCCESS|{green}FOLLOW|+{g["data"]["prices"]}')
                startmaxjob+=1
                jobloi=0
                if startmaxjob == maxjob+1:
                    print(f'~[+]{pink}ĐÃ ĐẠT MAX JOB. ')
                    return

            else:
                print(f'{green}Đang kiểm tra lại hành động...',end="\r")
                sleep(2)
                while True:
                    try:
                        g = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers=headers,json=json_data).json()
                        break
                    except:
                        print(f'{red}Đang nhận lại phần thưởng...',end="\r")
                        sleep(2)
                if g['status']==200:
                    job_success+=1
                    print(f'{green}SUCCESS:{red}[{job_success}/{startmaxjob}]{cyan}[{time()}]|{random.choice(ranmau)}SUCCESS|{green}FOLLOW|+{g["data"]["prices"]}')
                    startmaxjob+=1
                    jobloi=0
                    if startmaxjob == maxjob+1:
                        print(f'~[+]{pink}ĐÃ ĐẠT MAX JOB. ')
                        return
                else:
                    print(f'{red}Đang bỏ qua nhiệm vụ...',end='\r')
                    headers = {
                        'authorization': auth,
                        't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
                        'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
                                }
                    
                    json_data = {
                        'description': 'Báo cáo hoàn thành thất bại',
                        'users_advertising_id': id,
                        'type': 'ads',
                        'provider': 'tiktok',
                        'fb_id': idtiktok ,
                        'error_type': 3,
                                 }
                    
                    requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)
                
                  
                    headers = {
                        'authorization': auth,
                        't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
                        'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"
                             }
                    
                    json_data = {
                        'ads_id': id,
                        'object_id': object_id,
                        'account_id': idtiktok ,
                        'type': 'follow',
                                 }
                    skipjob=requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',headers=headers,json=json_data)
                    startmaxjob+=1
                    jobloi+=1
                    if startmaxjob == maxjob+1:
                        print(f'~[+]{green}ĐÃ ĐẠT MAX JOB')
                        return
                    elif jobloi==15:
                        select=input(f'{red}Lỗi nhiều ,Bạn có muốn đổi nick?(y/n):')
                        if select.lower() == 'n':
                            pass
                        else:
                            nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]
                            for i, nickname in enumerate(nicknames, start=1):
                                globals()[f'{i}'] = nickname
                            print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                            text=f'~[+]{red}SELECT {green}ACC CHẠY NHIỆM VỤ '
                            pr(text)
                            # In giá trị của các biến
                            for i, nickname in enumerate(nicknames, start=1):
                                text=f'{red}[{green}{i}{red}]: {globals()[f"{i}"]}'
                                pr(text)
                            idtiktok = get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
                            jobloi=0

      except:
          print(f'{red}Đang nhận lại nhiệm vụ...',end='\r')
          sleep(2)

  
  


  
  
  
  
  

  

def creat_key():
  current_time = datetime.now()
  time = current_time.strftime("%F")
  characters_to_choose_from = 'qưertyuiopasdghjklzxcvbnmQWERTYUIOPASDGHJKLZXCVBNM123456789'
  characters = 'qưertyuiopasdghjklzxcvbnmQWERTYUIOPASDGHJKLZXCVBNM123456789'
    # Tạo một chuỗi ngẫu nhiên gồm 5000 ký tự từ danh sách trên
  randoma = ''.join(random.choice(characters_to_choose_from) for _ in range(10))
  end_link = ''.join(random.choice(characters) for _ in range(10))
  dulieu=f'Key-{time}-{randoma}'
  notelink= f'https://laylinkngon.000webhostapp.com/?text={dulieu}'
  data = {
    'url': notelink,
    'custom': '',
    'expiry': '',
    'password': '',
    'description': '',
    'multiple': '0',
        }

  response = requests.post('https://bom.so/shorten', data=data).json()
  note=response['short']
  shortlink=requests.get(f"https://3link.co/api?api=e21aeb8a5f25d560d53a6881ae7b74703470f98d&url={note}").json()
  shortlink=shortlink['shortenedUrl']
  return shortlink,dulieu
  
  
  
  
  
#biến
#green='\033[38;5;10m'
blue='\033[38;5;12m'
cyan='\033[38;5;14m'
white='\033[1;39m'
magenta='\033[38;5;5m'
orange='\033[38;5;202m'
xanhnhat = "\033[1;36m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
xduong = "\033[1;34m"
pink = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
redb="\033[1;31m"
end='\033[0m'
ranmau=(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)





       








            


while True:
  banner(red, green, blue, yellow, cyan, pink)
  current_time = datetime.now()
  time_key = current_time.strftime("%F")
  print(f'{pink}VERSION 1.5.0')
  changetoken(red,green,white) 
  auth,check =checkauth(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
  if not os.path.exists("setting_golike.txt"):
      idtiktok =get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
      print(f'''~[+]{red}BẠN CÓ MUỐN LỌC JOB LIKE KHÔNG:
{red}[1]:{green}CÓ
{red}[2]:{green}KHÔNG''')
      select_job=cint(f'{red}NHẬP LỰA CHỌN:{green}')
      delay =cint(f'~[+]{red}NHẬP DELAY: {green}')
      maxjob= cint(f'~[+]{red}NHẬP MAX JOB: {green}')
      setting={
        "loaijob":select_job,
        "delay":delay,
        "maxjob":maxjob
      }

      file = open("setting_golike.txt", "a")  # Append mode
      file.write(json.dumps(setting))
      file.close()
      print(f'{cyan}KHỞI CHẠY NHIỆM VỤ') 
      print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
      sleep(1)
      if select_job==1:
        getjob_follow(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
      else:
        getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)   
          
                
  else: 
        idtiktok = get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
        select_setting=input(f'{green}Bạn có muốn sử dụng setting cũ không?[y/n]{cyan}:' )
        if select_setting.lower() == 'n':
            os.remove('setting_golike.txt')
            idtiktok =get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
            print(f'''~[+]{red}BẠN CÓ MUỐN LỌC JOB LIKE KHÔNG:
{red}[1]:{green}CÓ
{red}[2]:{green}KHÔNG''')
            select_job=cint(f'{red}NHẬP LỰA CHỌN:{green}')
            delay =cint(f'~[+]{red}NHẬP DELAY: {green}')
            maxjob= cint(f'~[+]{red}NHẬP MAX JOB: {green}')
            setting={
              "loaijob":select_job,
              "delay":delay,
              "maxjob":maxjob
            }
            file = open("setting_golike.txt", "a")  # Append mode
            file.write(json.dumps(setting))
            file.close()

            print(f'{cyan}KHỞI CHẠY NHIỆM VỤ') 
            print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
            sleep(1)
            if select_job==1:
              getjob_follow(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
            else:
              getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)   
                
                      
        else:
          try:
              with open("setting_golike.txt", "r") as file:
                data_txt=file.read()
                data_json = json.loads(data_txt)
                select_job = int(data_json.get('loaijob'))
                delay = int(data_json.get('delay'))
                maxjob= int(data_json.get('maxjob'))
                print(f'{cyan}KHỞI CHẠY NHIỆM VỤ') 
                print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                sleep(1)
                if select_job==1:
                  getjob_follow(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
                else:
                  getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
          except json.JSONDecodeError:
              print("Dữ liệu không hợp lệ. Vui lòng kiểm tra lại định dạng JSON trong tệp.")
          

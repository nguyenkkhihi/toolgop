import requests
import os, sys, json, re
from time import sleep
session = requests.Session()
import os, sys, re, json
from time import sleep
import random
from datetime import datetime
import requests
import requests
p=0
listck=[]
import uuid
class ApiPro5:
    def __init__(self, cookies) -> None:
        self.headers = {
                'authority': 'www.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'vi',
                'cookie': cookies,
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                'viewport-width': '1366',
            }
        url_profile = requests.get('https://www.facebook.com/me', headers=self.headers).url
        profile = requests.get(url_profile, headers=self.headers).text
        try:
            self.fb_dtsg = profile.split('{"name":"fb_dtsg","value":"')[1].split('"},')[0]
            self.jazoet = profile.split('{"name":"jazoest","value":"')[1].split('"},')[0]
            self.user_id = profile.split('","viewer_actor":{"__typename":"User","id":"')[1].split('"},"')[0]
        except:
            self.fb_dtsg = profile.split(',"f":"')[1].split('","l":null}')[0]
            self.jazoet = profile.split('&jazoest=')[1].split('","e":"')[0]
            self.user_id = profile.split('{"u":"\/ajax\/qm\/?__a=1&__user=')[1].split('&__comet_req=')[0]
    def reaction(self, id_post, type):
        if type == 'LIKE':
            reac = '1635855486666999'
        elif type ==  'LOVE':
            reac  =  '1678524932434102'
        elif type ==  'CARE':
            reac = '613557422527858'
        elif type ==  'HAHA':
            reac = '115940658764963'
        elif type ==  'WOW':
            reac = '478547315650144'
        elif type ==  'SAD':
            reac = '908563459236466'
        elif type ==  'ANGRY':
            reac = '444813342392137'
        try:
            url = requests.get('https://www.facebook.com/'+id_post, headers=self.headers).url
            home = requests.get(url, headers=self.headers).text
            feedback_id = home.split('{"__typename":"CommentComposerLiveTypingBroadcastPlugin","feedback_id":"')[1].split('","')[0]
            data = {
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoet,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation',
                'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1667106623951,429237,190055527696468,","feedback_id":"'+feedback_id+'","feedback_reaction_id":"'+reac+'","feedback_source":"PROFILE","is_tracking_encrypted":true,"tracking":["AZXg8_yM_zhwrTY7oSTw1K93G-sycXrSreRnRk66aBJ9mWkbSuyIgNqL0zHEY_XgxepV1XWYkuv2C5PuM14WXUB9NGsSO8pPe8qDZbqCw5FLQlsGTnh5w9IyC_JmDiRKOVh4gWEJKaTdTOYlGT7k5vUcSrvUk7lJ-DXs3YZsw994NV2tRrv_zq1SuYfVKqDboaAFSD0a9FKPiFbJLSfhJbi6ti2CaCYLBWc_UgRsK1iRcLTZQhV3QLYfYOLxcKw4s2b1GeSr-JWpxu1acVX_G8d_lGbvkYimd3_kdh1waZzVW333356_JAEiUMU_nmg7gd7RxDv72EkiAxPM6BA-ClqDcJ_krJ_Cg-qdhGiPa_oFTkGMzSh8VnMaeMPmLh6lULnJwvpJL_4E3PBTHk3tIcMXbSPo05m4q_Xn9ijOuB5-KB5_9ftPLc3RS3C24_7Z2bg4DfhaM4fHYC1sg3oFFsRfPVf-0k27EDJM0HZ5tszMHQ"],"session_id":"'+str(uuid.uuid4())+'","actor_id":"'+self.user_id+'","client_mutation_id":"1"},"useDefaultActor":false,"scale":1}',
                'server_timestamps': 'true',
                'doc_id': '5703418209680126',
            }

            reaction = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
            return {'status': True, 'type': type, 'url': url}
        except:
            return {'status': False, 'type': type, 'url': url}
def idelay(o):
    while(o>0):
        o=o-1
        print(f"[LKZ TOOL][.....""]""["+str(o)+"]""     ",end='\r')
        sleep(1/6)
        print(f"[LKZ TOOL][•....""]""["+str(o)+"]""     ",end='\r')
        sleep(1/6)
        print(f"[LKZ TOOL][••...""]""["+str(o)+"]" "     ",end='\r')
        sleep(1/6)
        print(f"[LKZ TOOL][•••..""]""["+str(o)+"]"" ",end='\r')
        sleep(1/6)
        print(f"[LKZ TOOL][••••.""]""["+str(o)+"]""     ",end='\r')
        sleep(1/6)
        print(f"[LKZ TOOL][•••••""]""["+str(o)+"]""     ",end='\r')
        sleep(1/6)
dem=0
stop=1
listjob=[]
os.system("clear")
rf_acc='https://traodoisub.com/view/cauhinh'
rf_login='https://traodoisub.com/home/'
head_login={
'Host':'traodoisub.com',
'accept':'*/*',
'content-length':'28',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
}
	print("\033[1;33m██╗░░░░░██╗░░██╗███████╗")
	print("\033[1;35m██║░░░░░██║░██╔╝╚════██║")
	print("\033[1;36m██║░░░░░█████═╝░░░███╔═╝")
	print("\033[1;31m██║░░░░░██╔═██╗░██╔══╝░░")
	print("\033[1;32m███████╗██║░╚██╗███████╗")
	print("\033[1;31m╚══════╝╚═╝░░╚═╝╚══════╝\n")
	print("\033[97m════════════════════════════════════════════════  ")
	print("\033[1;31mTool By: \033[1;32mLKZ TOOL ")
	print("\033[1;97m[\033[1;91m->\033[1;97m]\033[1;97m nhóm telegram\033[1;31m  : \033[1;36mhttps://t.me/lkztool")
	print("\033[1;97m[\033[1;91m->\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;36mhttps://youtube.com/@lkztool?si=7aPtPEHjDvOAIVgl")
	print("\033[1;97m[\033[1;91m->\033[1;97m]\033[1;97m Zalo\033[1;31m     : \033[1;36mhttp://zaloapp.com/qr/p/289m9jxm6gpn")
	print("\033[1;97m[\033[1;91m->\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;36mhttps://t.me/van_anh2004")
	print("\033[97m════════════════════════════════════════════════")

tk=input('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập Tài Khoản TDS: \033[1;33m ')
mk=input('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập Mật Khẩu TDS: \033[1;33m')
data_login={
'username': tk,
'password': mk,
}
log=session.post(url='https://traodoisub.com/scr/login.php', headers=head_login, data=data_login).text
if "success" in log:
    print('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mLogin Thành Công ')
    sleep(2)
else:
    print('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;31mLogin Thất Bại ')
    exit()
sleep(0.2)
reg = log
m = session.cookies.get_dict()
ph = m['PHPSESSID']
cktds='PHPSESSID='+ph
os.system('clear')
cookies = {
    'PHPSESSID': ph
}
headerss = {
    'authority': 'traodoisub.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'PHPSESSID=bd3451757cdf7d559ce2583228792b19',
    'referer': 'https://traodoisub.com/view/chtiktok/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
    'x-requested-with': 'XMLHttpRequest',
}
gettk=requests.get('https://traodoisub.com/view/setting/load.php', cookies=cookies, headers=headerss).json()
tokentds=gettk['tokentds']
head={
'Host':'traodoisub.com',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':rf_login,
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
}
	print("\033[1;33m██╗░░░░░██╗░░██╗███████╗")
	print("\033[1;35m██║░░░░░██║░██╔╝╚════██║")
	print("\033[1;36m██║░░░░░█████═╝░░░███╔═╝")
	print("\033[1;31m██║░░░░░██╔═██╗░██╔══╝░░")
	print("\033[1;32m███████╗██║░╚██╗███████╗")
	print("\033[1;31m╚══════╝╚═╝░░╚═╝╚══════╝\n")
	print("\033[97m════════════════════════════════════════════════  ")
	print("\033[1;31mTool By: \033[1;32mLKZ TOOL ")
	print("\033[1;97m[\033[1;91m->\033[1;97m]\033[1;97m nhóm telegram\033[1;31m  : \033[1;36mhttps://t.me/lkztool")
	print("\033[1;97m[\033[1;91m->\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;36mhttps://youtube.com/@lkztool?si=7aPtPEHjDvOAIVgl")
	print("\033[1;97m[\033[1;91m->\033[1;97m]\033[1;97m Zalo\033[1;31m     : \033[1;36mhttp://zaloapp.com/qr/p/289m9jxm6gpn")
	print("\033[1;97m[\033[1;91m->\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;36mhttps://t.me/van_anh2004")
	print("\033[97m════════════════════════════════════════════════")
check_tk=requests.get(url='https://traodoisub.com/scr/user.php', headers=head)
xu=check_tk.json()['xu']
print('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mXu Hiện Tại : \033[1;37m'+xu)
print("\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
# def cauhinh(idfb):
# 	run = requests.get(f'https://traodoisub.com/api/?fields=run&id={idfb}&access_token={tokentds}').json()
# 	if 'success' in run:
# 	       print('', end='\r')
# 	else:
# 	           print(run['error'])
# 	           #quit()
def cauhinh(idfb):
    run = requests.get(f'https://traodoisub.com/api/?fields=run&id={idfb}&access_token={tokentds}').json()
    if run.get('success'):
        print('', end='\r')
    else:
        print(run.get('error', 'Unknown error'))

cookiefb=input(f'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập Cookie Facebook: \033[1;33m')
while True:
	p+=1
	idpro5=str(input(f'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập ID PROFILE SỐ {p}: '))
	if idpro5=='':break
	else:
		headers={
                'authority': 'www.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'vi',
                'cookie': cookiefb,
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                'viewport-width': '1366',
            }
		url='https://m.facebook.com/profile.php?id='+str(idpro5)
		r=requests.get(url, headers=headers, ).text
		try:
			user=r.split('<title>')[1].split('</title>')[0]
			print(f'[SUCCESS-NAME:{user}]')
			listck.append(f'{cookiefb}i_user={idpro5};|{p}>{user}')
		except:quit('Cookies Sai')
lc=str(input('1-Cảm Xúc\nLựa Chọn: '))
delay=int(input('DELAY: '))
for t in lc.split('+'):
	if t=='1':listjob.append('cx')
while True:
	runn=random.choice(listjob)
	ckkk=random.choice(listck)
	ckk=ckkk.split('|')[0]
	soac=ckkk.split('|')[1].split('>')[0]
	idd=ckk.split('i_user=')[1].split(';')[0]
	user=ckkk.split('>')[1]
	cauhinh(idd)
	print(f'[Cấu Hình Thành Công!][{soac} -> USER: {user}]', end='\r')
	if str(runn)=='cx':
		try:
			head_job={
'Host':'traodoisub.com',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/ex/reaction/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,}
			getjob=requests.get(url='https://traodoisub.com/ex/reaction/load.php', headers=head_job).json()
			for x in getjob['data']:
				id=x['id']
				type=x['type']
				cookies=ckk
				api = ApiPro5(cookies)
				ai=api.reaction(id, type)
				nhan_={
'Host':'traodoisub.com',
'accept':'*/*',
'content-length':'28',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/ex/reaction/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
             }
				getxu=requests.post('https://traodoisub.com/ex/reaction/nhantien.php', headers=nhan_, data={'id': id, 'type': type}).text
				if '2' in getxu:
					check_tk=requests.get(url='https://traodoisub.com/scr/user.php', headers=head)
					xu=check_tk.json()['xu']
					dem+=1
					time = datetime.now().strftime("%H:%M:%S")
					print(f'[{dem}][{time}][{type}][400][{xu}][{soac}]')
					idelay(delay)
		except:pass
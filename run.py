import os,requests,time,json
def cek():
    try:
         cookie = open(".cookie.txt","r").read()
         token = open(".token.txt","r").read()
         p = requests.get('https://graph.facebook.com/me?&access_token='+token, cookies={'cookie':cookie})
         name = json.loads(p.text)['name']
         os.system('python ./data/home.py')
    except KeyError:
           keamanan()
           os.system('bash ./data/cekpoint.sh')
           os.system('bash ./data/login.sh')       
def keamanan():
    try:
        open('./data/.pickfordganteng','r').read()
    except FileNotFoundError:
        os.system('bash ./data/keamanan.sh')
        
if __name__=='__main__':
   try:
       import os, sys, shutil, subprocess 
   except requests.exceptions.ConnectionError:
          exit ('\n\t\x1b[0m koneksi bermasalah ...\n')
   try:
       import requests 
   except (ImportError,ModuleNotFoundError):
       os.system("bash ./data/cekmodule.sh")
       os.system("pip install requests")
   try:
       import mechanize 
   except (ImportError,ModuleNotFoundError):
       os.system("bash ./data/cekmodule.sh")
       os.system("pip install mechanize")
   try:
       import rich 
   except (ImportError,ModuleNotFoundError):
       os.system("bash ./data/cekmodule.sh")
       os.system("pip install rich")
   try:
       import bs4
   except (ImportError,ModuleNotFoundError):
       os.system("bash ./data/cekmodule.sh")
       os.system("pip insstall bs4")
   try:
       bff_2 = open(os.devnull, "w")
       my_music = subprocess.call(["dpkg","-s","play-audio"],stdout=bff_2,stderr=subprocess.STDOUT)
       bff_2.close() 
       if my_music !=0:
          os.system("./data/cekmodule.sh")
          os.system('pkg install play-audio' )
   except FileNotFoundError:
       os.system("./data/cekmodule.sh")
       os.system('pkg install play-audio' )
       os.system('touch .cookie.txt .token.txt')
       cek()

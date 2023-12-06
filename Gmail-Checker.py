from concurrent.futures import ThreadPoolExecutor as thread
import requests

rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn = '\033[00;36m'

def Req(i,save):
    i = i.strip()
    r = requests.post("https://mailcheck.co/api/checkMail", data={'email': i})
    r = r.json()['smtpExists']
    if True == r:
    	with open(f'{save}/Valid.txt','a') as s:
    	    s.write(i+'\n')
    	    print (f"{lrd}[{lgn}√{lrd}] {gn}VALID! {yw}|{lgn}{i}{yw}|")
    else:
    	print (f"{lrd}[{rd}×{lrd}] {rd}INVALID! {yw}|{rd}{i}{yw}|")

address = input(f"""{pe}
____ _  _    ____ _  _ ____ ____ _  _ ____ ____ 
| __ |\/| __ |    |__| |___ |    |_/  |___ |__/ 
|__] |  |    |___ |  | |___ |___ | \_ |___ |  \ 
                                                
\n{cn}Git & Tg : @esfelurm\n
{lrd}[{lgn}~{lrd}] {gn}Address File Emails : {cn}""")
o = open(address,'r')
save = input(f"{lrd}[{lgn}~{lrd}] {gn}Where are VALID emails saved : {cn}")
print ("\n\n")
with thread() as executor:
    for i in o:
        executor.submit(Req,i,save)

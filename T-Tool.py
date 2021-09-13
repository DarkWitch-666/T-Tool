import colorama
import os
import time
from colorama import init, Fore, Back, Style

# init()
init(autoreset=True)
print("Starting T-T...")
os.system("pip3 install colorama")
Banner = f'''
{Fore.LIGHTWHITE_EX}
████████╗████████╗ ██████╗  ██████╗ ██╗     
╚══██╔══╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     
   ██║█████╗██║   ██║   ██║██║   ██║██║     
   ██║╚════╝██║   ██║   ██║██║   ██║██║     
   ██║      ██║   ╚██████╔╝╚██████╔╝███████╗
   ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝

'''
text = f"""

{Banner}


{Fore.RED}. :| by ~ t.me/DarkWitcher_666 |: .

{Fore.WHITE}═════════════════════════════════
{Fore.RED}1 {Fore.WHITE}- {Fore.LIGHTYELLOW_EX}Weeman
{Fore.RED}2 {Fore.WHITE}- {Fore.LIGHTYELLOW_EX}Infoga
{Fore.RED}3 {Fore.WHITE}- {Fore.LIGHTYELLOW_EX}Crips
{Fore.RED}4 {Fore.WHITE}- {Fore.LIGHTYELLOW_EX}SocialFish
{Fore.RED}5 {Fore.WHITE}- {Fore.LIGHTYELLOW_EX}Santet Online
{Fore.RED}6 {Fore.WHITE}- {Fore.LIGHTYELLOW_EX}Goblin
{Fore.RED}7 {Fore.WHITE}- {Fore.LIGHTYELLOW_EX}TBomb
{Fore.RED}8 {Fore.WHITE}- {Fore.LIGHTYELLOW_EX}User Recon
{Fore.RED}9 {Fore.WHITE}- {Fore.LIGHTYELLOW_EX}Hakku framework
{Fore.RED}10 {Fore.WHITE}- {Fore.LIGHTYELLOW_EX}RED HAWK
{Fore.RED}11 {Fore.WHITE}- {Fore.LIGHTYELLOW_EX}Nmap
{Fore.RED}12 {Fore.WHITE}- {Fore.LIGHTYELLOW_EX}ReconDog
{Fore.RED}13 {Fore.WHITE}- {Fore.LIGHTYELLOW_EX}LockPhish
{Fore.RED}14 {Fore.WHITE}- {Fore.LIGHTYELLOW_EX}Zphisher
{Fore.RED}15 {Fore.WHITE}- {Fore.LIGHTYELLOW_EX}IpGeoLocation
{Fore.WHITE}═════════════════════════════════
{Fore.RED}	m{Fore.WHITE} - {Fore.LIGHTYELLOW_EX}more
{Fore.RED}	ctrl + c/z{Fore.WHITE} - {Fore.LIGHTYELLOW_EX}exit
"""
os.system("clear")
print(f"""
{text}
""")
while True:
	termux = input(f'{Fore.RED}>{Fore.BLUE}>{Fore.GREEN}> {Fore.BLUE}Termux@tool {Fore.LIGHTYELLOW_EX}~ ')
	
	if termux.lower() == "m":
		try:
			print('''
═════════════════════════════════════
This tool is designed to automate the installations
of the utilities that the tool supports. 

Full name this tool >> TERMUX-TOOL

«T-T» Usage: Select the item number and press enter.
then the installation will go by itself!
═════════════════════════════════════
''')
		except:
			print("Error")
	if termux == "1":
		try:
			os.system("clear")
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Weeman installing...") #вид отображения утилиты
			os.system("cd && apt install git -y && apt install python2 -y && git clone https://github.com/evait-security/weeman && cd weeman && chmod +x * && clear") #установка
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Weeman installed successfully!")
			time.sleep(2)
			os.system("clear")
			print(f"""
			{text}
			""")
		except:
			print("Error")
	if termux == "2":
		try:
			os.system("clear")
			
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Infoga installing...")
			os.system("cd && apt install git python -y && git clone https://github.com/m4ll0k/Infoga.git && cd Infoga && pip3 install -r requirements.txt && clear")
			
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Infoga installed successfully!")
			
			time.sleep(2)
			os.system("clear")
			
			print(f"""
			{text}
			""")
		except:
			print("Error")
	if termux == "3":
		try:
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Crips installing...")
			
			os.system("cd && apt install git python python2 -y && git clone https://github.com/Manisso/Crips && cd Crips && chmod +x * && ./install.sh && cd && clear")
			
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Crips installed successfully!")
			time.sleep(2)
			os.system("clear")
			print(f"""
			{text}
			""")
		except:
			print("Error")
	if termux == "4":
		try:
			os.system("clear")
			
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}SocialPhish installing...")
			
			os.system("cd && apt install git python2 -y && git clone https://github.com/xHak9x/SocialPhish.git && cd SocialPhish && chmod +x socialphish.sh && clear")
			
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}SocialPhish installed successfully!")
			time.sleep(2)
			os.system("clear")
			print(f"""
			{text}
			""")
		except:
			print("Error")
	if termux == "5":
		try:
			os.system('clear')
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Santet-Online installing...")
			os.system("cd && apt install git python python3 -y && git clone https://github.com/Gameye98/santet-online && cd santet-online && chmod +x * && clear")
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Santet-Online installed successfully!")
			time.sleep(2)
			os.system("clear")
			print(f"""
			{text}
			""")
		except:
			print("Error")
	if termux == "6":
		try:
			os.system("clear")
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Goblin installing...")
			os.system("cd && apt install git python python2 -y && git clone https://github.com/UndeadSec/GoblinWordGenerator && cd GoblinWordGenerator && chmod +x *")
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Goblin installed successfully!")
			time.sleep(2)
			os.system("clear")
			print(f"""
			{text}
			""")
		except:
			print("Error")
	if termux == "7":
		try:
			os.system("clear")
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}TBomb installing...")
			os.system("cd && apt install git python -y && git clone https://github.com/TheSpeedX/TBomb cd TBomb && pip3 install -r requirements.txt && clear")
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}TBomb installed successfully!")
			time.sleep(2)
			os.system("clear")
			print(f"""
			{text}
			""")
		except:
			print("Error")
	if termux == "8":
		try:
			os.system("clear")
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}User Recon installing...")
			os.system("cd && apt && git clone https://github.com/thelinuxchoice/userrecon && cd userrecon && chmod +X *&& clear")
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}User Recon installed successfully!")
			time.sleep(2)
			os.system('clear')
			print(f"""
			{text}
			""")
		except:
			print("Error")
	if termux == "9":
		try:
			os.system("clear")
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}HakkuFramework installing...")
			os.system("cd && apt install git python -y && git clone https://github.com/4shadoww/hakkuframework && cd hakkuframework && chmod +x* && clear")
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}HakkuFramework installed successfully!")
			time.sleep(2)
			os.system('clear')
			print(f"""
			{text}
			""")
		except:
			print("Error")
	if termux == "10":
		try:
			os.system("clear")
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}RED HAWK installing...")
			os.system("cd && apt install git php -y && git clone https://github.com/Tuhinshubhra/RED_HAWK && cd RED_HAWK && chmod +x * && clear")
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}RED HAWK installed successfully!")
			time.sleep(2)
			os.system('clear')
			print(f"""
			{text}
			""")
		except:
			print("Error")
	if termux == "11":
		try:
			os.system("clear")
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Nmap installing...")
			os.system("cd && apt update && apt upgrade -y && apt install nmap -y && clear")
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Nmap installed successfully!")
			time.sleep(2)
			os.system('clear')
			print(f"""
			{text}
			""")
		except:
			print("Error")
			#git clone https://github.com/UltimateHackers/ReconDog
	if termux == "12":
		try:
			os.system("clear")
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}ReconDog installing...")
			os.system("cd && apt install git python2 -y && git clone https://github.com/UltimateHackers/ReconDog && cd ReconDog && chmod +x * && pip2 install -r requirements.txt && clear")
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}ReconDog installed successfully!")
			time.sleep(2)
			os.system('clear')
			print(f"""
			{text}
			""")
		except:
			print("Error")
	if termux == "13":
		try:
			os.system("clear")
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}LockPhish installing...")
			os.system("cd && apt install git wget -y && git clone https://github.com/kali-linux-tutorial/lockphish && cd lockphish && clear")
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}LockPhish installed successfully!")
			time.sleep(2)
			os.system('clear')
			print(f"""
			{text}
			""")
		except:
			print("Error")

	if termux == "14":
		try:
			os.system("clear")
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Zphisher installing...")
			os.system("cd && apt install git php curl openssh -y && git clone https://github.com/htr-tech/zphisher && cd zphisher && chmod +x zphisher.sh && clear")
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}Zphisher installed successfully!")
			time.sleep(2)
			os.system('clear')
			print(f"""
			{text}
			""")
		except:
			print("Error")
			#git clone https://github.com/maldevel/IPGeoLocation
	if termux == "15":
		try:
			os.system("clear")
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}IPGeoLocation installing...")
			os.system("cd && apt install git python -y && git clone https://github.com/maldevel/IPGeoLocation && cd IPGeoLocation && chmod +x * && pip3 install -r requirements.txt && clear")
			print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] {Fore.LIGHTYELLOW_EX}IPGeoLocation installed successfully!")
			time.sleep(2)
			os.system('clear')
			print(f"""
			{text}
			""")
		except:
			print("Error")
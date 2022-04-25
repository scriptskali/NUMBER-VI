# NUMBER-VI
#te amo doboque😭❤️
import requests
import os
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
os.system("clear")


print(GREEN+"▒█▄░▒█ ▒█░▒█ ▒█▀▄▀█ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀█ ░░ ▒█░░▒█ ▀█▀")
print("▒█▒█▒█ ▒█░▒█ ▒█▒█▒█ ▒█▀▀▄ ▒█▀▀▀ ▒█▄▄▀ ▀▀ ░▒█▒█░ ▒█░")
print("▒█░░▀█ ░▀▄▄▀ ▒█░░▒█ ▒█▄▄█ ▒█▄▄▄ ▒█░▒█ ░░ ░░▀▄▀░ ▄█▄")

print(GREEN+"///////////////////////////////////////")
print("CREADOR: s.c.r.i.p.t.s.k.a.l.i")
print("///////////////////////////////////////")
print("TIKTOK: s.c.r.i.p.t.s.k.a.l.i")
print("///////////////////////////////////////")
print("github: https://github.com/scriptskali/")
print("/////////////////////////////////////// \n")
print(GREEN+"escriba el numero del wsp para kakearlo\n ejemplo: +5491130670816\n")

api_key = '6efbbe73f83486b793920342c81a1dd0'

number = int(input(GREEN+"Numero de telefono: "+RESET))

data = requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1" % (api_key, number))

for key, value in data.json().items():

    print("%s: %s" % (key, value))

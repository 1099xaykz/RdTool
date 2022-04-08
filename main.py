import time
import os
import sys
import nmap
import threading

BLACK = '\033[1;30m'
RED = '\033[1;31m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
MAGENTA = '\033[1;35m'
CYAN = '\033[1;36m'
WHITE = '\033[1;37m'
RESET = '\033[1;39m'

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)

def search(ip_adress):
	command = "ping -c 1 " + ip_adress
	response = os.popen(command).read()
	if "1 received" in response:
		print(BLUE + "[+] " + WHITE + "Dispositivo encontrado > " + CYAN + ip_adress)
		a = open("dispositivos.txt", "a")
		a.write(ip_adress+"\n")
		a.close()

def banner():
	print(BLUE + """
 ____  ____    _____ ___   ___  _     
|  _ \|  _ \  |_   _/ _ \ / _ \| |    
| |_) | | | |   | || | | | | | | |    
|  _ <| |_| |   | || |_| | |_| | |___ 
|_| \_\____/    |_| \___/ \___/|_____|""")
	print(CYAN + """
            TikTok: @ds.8mqk
           Instagram: @ds8mqk
            Telegram: @ds8mqk
""")

def menu():
	print()
	print(BLUE + "--> " + WHITE + "1 Escanear puertos abiertos")
	print(BLUE + "--> " + WHITE + "2 Buscar dispositivos conectados a la red")
	print(BLUE + "--> " + WHITE + "3 Ver dispositivos en la red anteriormente encontrados")
	print(BLUE + "--> " + WHITE + "4 Identificar sistema operativo con nmap")
	print(BLUE + "--> " + WHITE + "5 Informacion de una direccion ip")
	print(BLUE + "--> " + WHITE + "6 Datos de mi ip")
	print()

def main():
	banner()
	while True:
		menu()
		opcion = input(CYAN + "# " + WHITE + "Selecciona una opcion > ")
		if opcion == "1":
			host = input(BLUE + "[+] " + WHITE + "Direccion IP > ")
			nm = nmap.PortScanner()
			print(BLUE + "[!!!] " + WHITE + "Este proceso puede tardar dependiendo cuandos puertos se encuentren abiertos")
			results = nm.scan(hosts=host, arguments="-sS -n -Pn -vvv -T4")
			print(BLUE + "[*] " + WHITE + "Host > " + host)
			print(BLUE + "[*] " + WHITE + "State > %s" % nm[host].state())
			for proto in nm[host].all_protocols():
				print(BLUE + "[+] " + WHITE + "Protocol > %s" % proto)
				lport = nm[host][proto].keys()
				sorted(lport)
				for port in lport:
					print("Port : %s\tstate : %s" % (port, nm[host][proto][port]["state"]))
		elif opcion == "2":
			print()
			for ip in range(1,254):
				current_ip = "192.168.0."+str(ip)
				run = threading.Thread(target=search , args = (current_ip,))
				run.start()
		elif opcion == "3":
			print()
			a = open("dispositivos.txt", "r")
			b = a.read()
			print(b)
			a.close()
		elif opcion == "4":
			ip = input(BLUE + "# " + WHITE + "IP > ")
			o = "nmap -O " + ip
			os.system(o)
		elif opcion == "5":
			ip = input(BLUE + "# " + WHITE + "IP > ")
			print()
			o = "curl -s http://ip-api.com/json/" + ip
			os.system(o)
			print()
		elif opcion == "6":
			print()
			print("IP:")
			os.system("curl ifconfig.io")
			print("Remote host:")
			os.system("curl ifconfig.io/host")
			print()

if __name__=="__main__":
	main()

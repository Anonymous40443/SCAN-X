#!/usr/bin/env python3
import os, sys, subprocess, platform, socket
from datetime import datetime

# --- CORES BLOOD MODE ---
R = '\033[31m'   # Vermelho Sangue
B = '\033[1;31m' # Vermelho Negrito
W = '\033[0m'    # Reset

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear_screen()
    print(f"""{B}
  ██████  ▄████▄   ▄▄▄       ███▄    █          ▒██    ██▒
 ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █          ▒▒ █ █ ▒░
 ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒          ░░ █   ░
   ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒           ░ █ █ ▒ 
 ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░          ▒██▒ ▒██▒
 ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒           ▒▒ ░ ░▓ ░
 ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░          ░░   ░▒ ░
 ░  ░  ░ ░           ░   ▒      ░   ░ ░            ░   ░  
       ░ ░ ░             ░  ░         ░            ░   ░  
           ░                                               
             [ SYSTEM: SCAN-X | STATUS: AGGRESSIVE ]
             [ TARGETS WILL BLEED | BY: Anonymous40443 ]
    {W}""")

def log_result(target, output):
    if not os.path.exists("reports"): os.makedirs("reports")
    filename = f"reports/scan_{target}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f: f.write(output)
    print(f"\n{R}[+] RELATÓRIO SANGRENTO SALVO EM: {filename}{W}")

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except: return "127.0.0.1"

def nmap_mega_menu():
    system = platform.system().lower()
    # Detecção de Termux para evitar o uso de sudo
    is_termux = os.path.exists('/data/data/com.termux/files/usr/bin/pkg')
    sudo = "sudo " if system == "linux" and not is_termux else ""
    
    while True:
        banner()
        print(f"{B}╔═══════════════ [ SCAN-X: NMAP ARSENAL ] ═══════════════╗")
        print(f"║ [1]  NMAP: PING SWEEP (HOST DISCOVERY)                 ║")
        print(f"║ [2]  NMAP: STEALTH SYN SCAN (DISCRETO)                 ║")
        print(f"║ [3]  NMAP: TCP CONNECT SCAN (FULL)                     ║")
        print(f"║ [4]  NMAP: UDP SCAN (DNS/DHCP/SNMP)                    ║")
        print(f"║ [5]  NMAP: XMAS SCAN (FIREWALL TEST)                   ║")
        print(f"║ [6]  NMAP: NULL SCAN (STEALTH ADVANCED)                ║")
        print(f"║ [7]  NMAP: FIN SCAN (IDS EVASION)                      ║")
        print(f"║ [8]  NMAP: OS & SERVICE DETECTION                      ║")
        print(f"║ [9]  NMAP: AGGRESSIVE (TOTAL DESTRUCTION)               ║")
        print(f"║ [10] NMAP: VULN SCAN (CVE SEARCH)                      ║")
        print(f"║ [11] NMAP: MALWARE SCAN (BACKDOOR CHECK)               ║")
        print(f"║ [12] NMAP: BRUTE FORCE AUTH (PASSWORDS)                ║")
        print(f"║ [13] NMAP: FIREWALL EVASION (FRAG)                     ║")
        print(f"║ [14] NMAP: DECOY SCAN (IP MASQUERADE)                  ║")
        print(f"║ [15] NMAP: FAST SCAN (TOP 100 PORTS)                   ║")
        print(f"║ [0]  RETURN TO DARKNESS                                ║")
        print(f"╚════════════════════════════════════════════════════════╝{W}")
        
        op = input(f"\n{B}SCAN-X:~$ {W}")
        if op == '0': break
        target = input(f"{R}➤ TARGET IP/DOMAIN: {W}").strip()
        if not target: continue

        cmds = {
            '1': f"{sudo}nmap -sn {target}", '2': f"{sudo}nmap -sS {target}",
            '3': f"{sudo}nmap -sT {target}", '4': f"{sudo}nmap -sU {target}",
            '5': f"{sudo}nmap -sX {target}", '6': f"{sudo}nmap -sN {target}",
            '7': f"{sudo}nmap -sF {target}", '8': f"{sudo}nmap -sV -O {target}",
            '9': f"{sudo}nmap -A {target}",  '10': f"{sudo}nmap --script vulners -sV {target}",
            '11': f"{sudo}nmap --script malware {target}", '12': f"{sudo}nmap --script auth {target}",
            '13': f"{sudo}nmap -f {target}", '14': f"{sudo}nmap -D RND:10 {target}",
            '15': f"{sudo}nmap -F {target}"
        }

        if op in cmds:
            print(f"\n{B}[!] SCANNING...{W}\n")
            res = subprocess.getoutput(cmds[op])
            print(res)
            log_result(target, res)
            input(f"\n{R}PRESS ENTER...{W}")

def main():
    while True:
        banner()
        print(f"{B}1 - [ SCAN-X ] NMAP MEGA MODULE (15+ SCANS)")
        print(f"2 - [ LAZY RECON ] AUTO-SCAN LOCAL NETWORK")
        print(f"3 - [ MASSACRE ] SCAN TARGET LIST (.TXT)")
        print(f"0 - EXIT SYSTEM{W}")
        
        choice = input(f"\n{B}SCAN-X:~$ {W}")
        if choice == '1': nmap_mega_menu()
        elif choice == '2':
            my_ip = get_local_ip()
            range_ip = ".".join(my_ip.split('.')[:-1]) + ".0/24"
            print(f"{R}[!] LOCAL IP: {my_ip} | RANGE: {range_ip}{W}")
            subprocess.run(f"nmap -sn {range_ip}", shell=True)
            input(f"\n{R}DONE. PRESS ENTER...{W}")
        elif choice == '3':
            file_path = input(f"{R}➤ PATH TO .TXT LIST: {W}")
            if os.path.exists(file_path): subprocess.run(f"nmap -iL {file_path}", shell=True)
            input(f"\n{R}PRESS ENTER...{W}")
        elif choice == '0': sys.exit()

if __name__ == "__main__": main()

# 🩸 SCAN-X v2.0 - Blood Tiger Edition 🐯

**SCAN-X** é um framework de reconhecimento agressivo e automatizado, projetado para transformar o motor do Nmap em uma interface simplificada, rápida e mortal. Desenvolvido para Pentesting e Auditoria de Redes.

---

## 🚀 Funcionalidades Revolucionárias

* 🐯 **Blood Tiger Interface:** Visual estilizado em High-Contrast Red.
* 💾 **Auto-Log System:** Resultados salvos automaticamente na pasta `/reports`.
* 📡 **Lazy Recon:** Detecta seu IP local e sugere o range de rede automaticamente.
* 🧨 **Massacre Mode:** Escaneia listas de alvos em massa via arquivo `.txt`.
* 📱 **Full Compatibility:** Kali Linux, Parrot OS, Termux (Android) e Windows.

---

## 📥 Instalação Passo a Passo

### 🐧 Linux (Kali / Parrot / Debian / Ubuntu)
```bash
sudo apt update && sudo apt install python3 nmap git -y
git clone [https://github.com/Anonymous40443/SCAN-X](https://github.com/Anonymous40443/SCAN-X)
cd SCAN-X
python3 SCAN-X.py

##  📥 Instalação Passo a Passo

###📱 Android (Termux)
Bash

pkg update && pkg upgrade -y
pkg install python nmap git -y
git clone [https://github.com/Anonymous40443/SCAN-X](https://github.com/Anonymous40443/SCAN-X)
cd SCAN-X
python SCAN-X.py


## 📥 Instalação Passo a Passo

### 🪟 Windows (Powershell/CMD)

    Instale o Python 3 (marque "Add to PATH").

    Instale o Nmap (nmap.org/download.html).

    Abra o terminal e rode:

Bash

git clone [https://github.com/Anonymous40443/SCAN-X](https://github.com/Anonymous40443/SCAN-X)
cd SCAN-X
python SCAN-X.py

### GUIA 💀 Guia de Operações (Módulos Nmap)
Opção	Nome	O que faz? (Explicação)
01	Ping Sweep	Localiza quais dispositivos estão "vivos" na rede agora.
02	Stealth SYN	Scan discreto que não fecha a conexão TCP (Burlar Logs).
03	TCP Connect	Scan completo e estável, mas mais fácil de ser detectado.
04	UDP Scan	Procura portas abertas de DNS, DHCP e serviços de jogos.
05	Xmas Scan	Envia pacotes com flags PSH, FIN e URG (Testar Firewalls).
06	Null Scan	Envia pacotes sem nenhuma flag (Técnica avançada de evasão).
07	FIN Scan	Tenta detectar portas fechadas enviando apenas a flag FIN.
08	OS & Service	Descobre a versão do Software e qual o Sistema Operacional.
09	Aggressive	Scan brutal: faz detecção de OS, Versão, Scripts e Traceroute.
10	Vuln Scan	Consulta o banco de dados Vulners para achar CVEs no alvo.
11	Malware Scan	Roda scripts NSE para detectar Backdoors ou infecções.
12	Brute Force	Tenta login padrão em serviços comuns (HTTP, FTP, SSH).
13	Firewall Ev	Fragmenta pacotes em pedaços minúsculos para passar pelo IPS.
14	Decoy Scan	Mascara seu IP usando 10 IPs aleatórios como "iscas".
15	Fast Scan	Varredura ultra rápida nas 100 portas mais comuns.
🛠️ Como Usar as Funções Extras

    Lazy Recon: Basta selecionar a opção 2 no menu principal. O SCAN-X vai ler seu IP, mostrar o range da sua rede e perguntar se deseja iniciar a varredura local.

    Massacre Mode: Crie um arquivo chamado alvos.txt, coloque um IP por linha, e selecione a opção 3. O SCAN-X vai processar toda a lista automaticamente.

    ⚠️ AVISO: Este software foi criado para fins estritamente educacionais. O uso em redes sem autorização prévia é ilegal e de total responsabilidade do usuário.

By: Anonymous40443 🕵️‍♂️

#CyberSecurity #Nmap #Pentest #RedTeam #Python #EthicalHacking #Tools #KaliLinux #Termux #SCANX #InformationSecurity

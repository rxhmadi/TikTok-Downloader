# TikTok-Downloader
TikTok Bulk Downloader adalah script Python sederhana untuk mengunduh video TikTok secara masal menggunakan API downloader pihak ketiga. Video akan diunduh dengan kualitas HD tanpa watermark dan disimpan dalam format .mp4 di folder yang ditentukan. Nama file video disusun dari author dan title video.

## 1. Requirements
--------------------

Daftar pustaka dan dependensi yang diperlukan agar script dapat berjalan:

- **Python 3.7 atau lebih baru**
- Pustaka Python:
  - `requests`
  - `pycryptodome`

## Cara Instalasi Requirements

Buat file bernama `requirements.txt` dan tambahkan baris berikut:
pip install -r requirements.txt
### 3. Cara Penggunaan
Langkah 1: Persiapkan Lingkungan
Pastikan Python 3.7+ telah terinstal di komputer.

Untuk memeriksa versi Python:

python --version
Instal pustaka yang dibutuhkan:

pip install -r requirements.txt

### Langkah 2: Siapkan Input
Buat file bernama urls.txt di direktori yang sama dengan script.

Tambahkan URL video TikTok yang ingin diunduh ke dalam file urls.txt, satu URL per baris. Contoh:


https://www.tiktok.com/@kharisma_ptw/video/7430678914437057800
https://www.tiktok.com/@kharisma_ptw/video/7430490764393647378
### Langkah3. Jalankan Script
Jalankan script dengan perintah:


python tiktok.py
Video akan diunduh ke folder downloads secara otomatis.

### 4. Output
Semua video akan disimpan di folder downloads dalam format .mp4.

Nama file mengikuti format:


[author] - [title].mp4
Contoh:

downloads/kharisma_ptw - met bobo semuanyaaaa 😁.mp4

### 5. Troubleshooting
Jika menghadapi masalah:

Pastikan file urls.txt berada di direktori yang sama dengan script.
Periksa koneksi internet.
Pastikan API URL masih aktif dan menerima permintaan.
Jika error berlanjut, coba jalankan script dengan menambahkan log debug:


import logging
logging.basicConfig(level=logging.DEBUG)
Dengan panduan ini, siapa pun dapat dengan mudah menggunakan script Anda untuk mengunduh video TikTok secara massal! 🚀✨


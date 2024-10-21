
# Instagram Follow Checker

Aplikasi Python sederhana menggunakan Instaloader untuk memeriksa siapa saja yang kamu follow tetapi tidak follow back di Instagram.
untuk 2fa nya masih beta kadang suka error , di harapkan matikan saya 2fa akun instagram nya

## Fitur
- Login ke akun Instagram (mendukung autentikasi dua faktor).
- Mendapatkan daftar followers dan following.
- Menampilkan siapa yang tidak follow back.

## Instalasi

1. Clone repositori ini:

    ```bash
    git clone https://github.com/username/instagram-follow-checker.git
    ```

2. Masuk ke direktori proyek:

    ```bash
    cd instagram-follow-checker
    ```

3. (Opsional) Buat dan aktifkan virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
    ```

4. Instal dependensi:

    ```bash
    pip install instaloader
    ```

## Penggunaan

1. Jalankan aplikasi:

    ```bash
    python app.py
    ```

2. Masukkan username dan password Instagram. Jika autentikasi dua faktor diaktifkan, masukkan kode 2FA.

3. Aplikasi akan menampilkan:
   - Jumlah followers dan following
   - Siapa yang tidak follow back

## Contoh Output

```bash
Masukkan username Instagram Anda: example_user
Masukkan password Instagram Anda: *********

Mencoba login tanpa 2FA...
Login berhasil.
Jumlah followers: 120
Jumlah following: 150

Semua pengguna yang Anda ikuti:
user1
user2
user3

Semua followers Anda:
user1
user4
user5

Orang yang tidak follow back:
user2
user3
```

## Catatan
- Pastikan kamu memiliki koneksi internet yang stabil.
- Aplikasi ini tidak menyimpan username atau password kamu. Data login hanya digunakan untuk autentikasi

## Lisensi
Proyek ini dilisensikan di bawah [MIT License](LICENSE).


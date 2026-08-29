# Bab 3 — Perulangan

## Misi 21–25

---

# 🧮 Misi 21 — Kalkulator Rentang Angka

## Cerita

Sebuah aplikasi edukasi memiliki fitur untuk membantu siswa memahami hubungan antara dua bilangan. Pengguna dapat memasukkan dua angka, kemudian aplikasi akan menampilkan seluruh bilangan dari yang terkecil hingga yang terbesar sekaligus menghitung jumlah seluruh bilangan tersebut.

Pengguna dapat terus memasukkan pasangan angka baru. Program akan berhenti ketika salah satu angka yang dimasukkan bernilai **0 atau negatif**.

## Tugas

Buatlah program yang dapat:

* membaca pasangan dua bilangan bulat secara berulang;
* menentukan angka yang lebih kecil dan lebih besar;
* menampilkan seluruh bilangan dari angka terkecil hingga terbesar;
* menghitung jumlah seluruh bilangan tersebut;
* menghentikan program jika salah satu angka bernilai `0` atau negatif.

## Contoh Penggunaan

```text
Masukkan dua angka: 5 2
2 3 4 5 Sum=14

Masukkan dua angka: 6 3
3 4 5 6 Sum=18

Masukkan dua angka: 5 0
Program selesai.
```

---

# ↕️ Misi 22 — Membaca Arah Pergerakan

## Cerita

Sebuah aplikasi sedang memantau pergerakan sebuah karakter berdasarkan dua posisi yang diberikan secara berurutan.

Jika posisi berikutnya lebih besar daripada posisi sebelumnya, berarti karakter bergerak **maju**. Jika lebih kecil, karakter bergerak **mundur**.

Program harus terus membaca pasangan posisi dan menentukan arah pergerakannya. Pemeriksaan berhenti ketika kedua angka yang diberikan memiliki nilai yang sama.

## Tugas

Buatlah program yang dapat:

* membaca dua bilangan bulat;
* menentukan apakah pergerakannya naik atau turun;
* menampilkan `Maju` jika angka kedua lebih besar;
* menampilkan `Mundur` jika angka kedua lebih kecil;
* berhenti jika kedua angka sama.

## Contoh Penggunaan

```text
Posisi: 5 4
Mundur

Posisi: 7 2
Mundur

Posisi: 3 8
Maju

Posisi: 2 2
Program selesai.
```

## Challenge

Modifikasi program agar selain arah, program juga menghitung **berapa jauh karakter bergerak** pada setiap perubahan posisi.

---

# 🔐 Misi 23 — Sistem Login

## Cerita

Sebuah aplikasi memiliki sistem login sederhana. Pengguna harus memasukkan PIN untuk mendapatkan akses.

PIN yang benar adalah:

```text
2002
```

Jika pengguna memasukkan PIN yang salah, aplikasi harus menampilkan pesan bahwa PIN tersebut tidak valid dan meminta pengguna mencoba kembali.

Proses akan terus berlangsung sampai pengguna memasukkan PIN yang benar.

## Tugas

Buatlah program yang dapat:

* meminta PIN pengguna;
* memeriksa apakah PIN benar;
* jika salah, tampilkan `PIN tidak valid`;
* jika benar, tampilkan `Akses diterima`;
* berhenti setelah PIN yang benar dimasukkan.

## Contoh Penggunaan

```text
Masukkan PIN: 2200
PIN tidak valid

Masukkan PIN: 1020
PIN tidak valid

Masukkan PIN: 2022
PIN tidak valid

Masukkan PIN: 2002
Akses diterima
```

## Challenge

Hitung berapa kali pengguna salah memasukkan PIN sebelum akhirnya berhasil login.

> **Catatan:** Dalam aplikasi sungguhan, sistem login biasanya memiliki batas percobaan dan mekanisme keamanan tambahan. Di misi ini kita sengaja membuat sistem sederhana untuk berlatih perulangan.

---

# 🗺️ Misi 24 — Memantau Posisi Karakter

## Cerita

Sebuah game memiliki peta berbentuk koordinat Cartesian. Setiap kali karakter berpindah tempat, game akan mengirimkan koordinat `X` dan `Y`.

Berdasarkan koordinat tersebut, program harus menentukan posisi karakter:

* kanan atas → **Kuadran 1**
* kiri atas → **Kuadran 2**
* kiri bawah → **Kuadran 3**
* kanan bawah → **Kuadran 4**

Karakter dapat berpindah berkali-kali sehingga program harus terus memproses koordinat baru.

Jika salah satu koordinat bernilai `0`, berarti karakter sudah keluar dari area permainan dan program harus berhenti.

## Tugas

Buatlah program yang dapat:

* membaca koordinat `X` dan `Y` secara berulang;
* menentukan kuadran karakter;
* menampilkan kuadran untuk setiap posisi;
* berhenti jika `X` atau `Y` bernilai `0`.

## Contoh Penggunaan

```text
Koordinat: 2 2
Kuadran 1

Koordinat: 3 -2
Kuadran 4

Koordinat: -8 -1
Kuadran 3

Koordinat: -7 1
Kuadran 2

Koordinat: 0 2
Permainan selesai.
```

## Challenge

Tambahkan penghitung untuk mengetahui **berapa kali karakter mengunjungi setiap kuadran** sebelum permainan berakhir.

---

# ➗ Misi 25 — Kalkulator Pembagian

## Cerita

Sebuah aplikasi kalkulator menerima beberapa operasi pembagian sekaligus. Pengguna terlebih dahulu menentukan berapa banyak operasi yang ingin dilakukan.

Untuk setiap operasi, pengguna memasukkan angka yang akan dibagi dan angka pembaginya.

Program harus menghitung hasil pembagian tersebut. Namun, pembagian dengan `0` tidak diperbolehkan. Jika pembagi bernilai `0`, aplikasi harus memberikan pesan bahwa pembagian tidak dapat dilakukan.

## Tugas

Buatlah program yang dapat:

* membaca jumlah operasi yang akan dilakukan;
* membaca dua bilangan untuk setiap operasi;
* menghitung hasil pembagian;
* menampilkan hasil dengan **1 angka di belakang koma**;
* jika pembagi bernilai `0`, tampilkan `Pembagian tidak dapat dilakukan`.

## Contoh Penggunaan

```text
Jumlah operasi: 3

Operasi 1
3 -2
Hasil: -1.5

Operasi 2
-8 0
Pembagian tidak dapat dilakukan

Operasi 3
0 8
Hasil: 0.0
```

## Challenge

Setelah seluruh operasi selesai, tampilkan:

* jumlah pembagian yang berhasil;
* jumlah pembagian yang gagal karena pembagi `0`.

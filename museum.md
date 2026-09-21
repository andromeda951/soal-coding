# 💎 Project — Museum Berlian

Buat sebuah game sederhana menggunakan **Python** dengan tema **Museum Berlian**.

Dalam game ini, pemain berperan sebagai seorang detektif yang harus mencari **Blue Diamond**, sebuah berlian langka yang disembunyikan di dalam museum.

Pemain harus menjelajahi beberapa ruangan, menemukan petunjuk, kemudian menggunakan semua petunjuk tersebut untuk membuka sebuah brankas.

---

# 📖 Cerita

Sebuah museum terkenal memiliki berlian langka bernama **Blue Diamond**.

Berlian tersebut tiba-tiba menghilang.

Menurut informasi yang kamu dapatkan, berlian tersebut tidak dibawa keluar dari museum.

Kemungkinan besar berlian masih tersembunyi di salah satu ruangan museum.

Kamu harus mencari berbagai petunjuk untuk menemukan lokasi berlian dan membuka brankas tempat berlian disimpan.

---

# 🏛️ Awal Game

Ketika game dimulai, tampilkan judul:

```text
========================================
          💎 MUSEUM BERLIAN
========================================
```

Kemudian tampilkan cerita singkat kepada pemain.

Setelah itu, tampilkan menu utama:

```text
1. Ruang Lukisan
2. Ruang Patung
3. Ruang Permata
4. Buka Brankas
5. Keluar
```

Pemain dapat memilih salah satu menu tersebut.

---

# 🖼️ 1. Ruang Lukisan

Jika pemain memilih **Ruang Lukisan**, tampilkan informasi bahwa terdapat banyak lukisan di dalam ruangan.

Salah satu lukisan terlihat berbeda dari yang lainnya.

Berikan dua pilihan:

```text
1. Periksa lukisan
2. Kembali
```

Jika pemain memilih **Periksa lukisan**, pemain menemukan sebuah petunjuk:

> Angka pertama adalah **7**.

Simpan informasi bahwa pemain sudah menemukan **petunjuk pertama**.

Pemain tidak boleh mendapatkan petunjuk pertama berulang kali.

Jika pemain kembali memeriksa lukisan setelah sebelumnya menemukan petunjuk tersebut, tampilkan pesan bahwa petunjuk sudah pernah ditemukan.

---

# 🗿 2. Ruang Patung

Jika pemain memilih **Ruang Patung**, tampilkan informasi bahwa terdapat sebuah patung besar di tengah ruangan.

Berikan pilihan:

```text
1. Periksa patung
2. Periksa meja
3. Kembali
```

Jika pemain memilih **Periksa patung**, pemain menemukan petunjuk:

> Angka kedua adalah **3**.

Simpan informasi bahwa pemain sudah menemukan **petunjuk kedua**.

Jika pemain memilih **Periksa meja**, tampilkan informasi bahwa meja tersebut kosong.

Petunjuk kedua hanya boleh ditemukan satu kali.

---

# 💎 3. Ruang Permata

Jika pemain memilih **Ruang Permata**, tampilkan informasi bahwa ruangan tersebut berisi berbagai macam batu permata.

Di sudut ruangan terdapat sebuah kotak.

Berikan pilihan:

```text
1. Periksa kotak
2. Kembali
```

Jika pemain memilih **Periksa kotak**, pemain menemukan petunjuk:

> Angka terakhir adalah **5**.

Simpan informasi bahwa pemain sudah menemukan **petunjuk ketiga**.

Petunjuk ketiga hanya boleh ditemukan satu kali.

---

# 🔐 4. Buka Brankas

Pemain dapat memilih menu **Buka Brankas** kapan saja.

Namun, pemain hanya boleh mencoba membuka brankas jika sudah menemukan **ketiga petunjuk**.

Jika belum menemukan semua petunjuk, tampilkan pesan seperti:

```text
Kamu belum menemukan semua petunjuk!
Cari ketiga petunjuk terlebih dahulu.
```

Jika semua petunjuk sudah ditemukan, pemain dapat mencoba membuka brankas.

---

## 🔢 Kode Brankas

Ketiga petunjuk yang ditemukan pemain adalah:

```text
Petunjuk pertama → 7
Petunjuk kedua   → 3
Petunjuk ketiga  → 5
```

Dengan demikian, pemain harus mengetahui sendiri bahwa kode brankas adalah:

```text
735
```

Jangan langsung menampilkan kode tersebut kepada pemain ketika mereka menemukan petunjuk.

---

# 🔑 Kesempatan Membuka Brankas

Pemain memiliki **3 kesempatan** untuk memasukkan kode.

Contoh:

```text
Masukkan kode: 123

❌ Kode salah!

Kesempatan tersisa: 2
```

Jika kode benar:

```text
✅ Kode benar!

Brankas terbuka!
```

Kemudian tampilkan pesan kemenangan:

```text
========================================
          🎉 SELAMAT!
========================================

Di dalam brankas terdapat sebuah kotak.

Kamu membuka kotak tersebut...

💎 BLUE DIAMOND 💎

Kamu berhasil menemukan berlian!

              YOU WIN!
========================================
```

Jika pemain salah sebanyak 3 kali:

```text
========================================
             GAME OVER
========================================

Kamu gagal membuka brankas.

Blue Diamond masih tersembunyi...
```

---

# 🔄 Game Loop

Game harus tetap berjalan setelah pemain selesai mengunjungi sebuah ruangan.

Contohnya:

```text
Menu utama
    ↓
Ruang Lukisan
    ↓
Kembali ke menu utama
    ↓
Ruang Patung
    ↓
Kembali ke menu utama
    ↓
Ruang Permata
    ↓
Kembali ke menu utama
    ↓
Buka Brankas
```

Game hanya berhenti jika:

1. Pemain memilih menu **Keluar**, atau
2. Pemain berhasil menemukan berlian, atau
3. Pemain gagal membuka brankas setelah 3 kesempatan.

---

# ❌ Validasi Input

Program harus menangani pilihan yang tidak tersedia.

Misalnya pemain memasukkan:

```text
Pilihan: 9
```

Tampilkan:

```text
Pilihan tidak tersedia!
Silakan pilih menu yang tersedia.
```

Hal yang sama berlaku ketika pemain berada di dalam ruangan.

Contohnya:

```text
Pilihan: 7

Pilihan tidak tersedia!
```

---


---

# 📌 Ketentuan Penting

Program harus memenuhi semua ketentuan berikut:

* [ ] Memiliki judul **Museum Berlian**
* [ ] Memiliki cerita pembuka
* [ ] Memiliki menu utama
* [ ] Memiliki Ruang Lukisan
* [ ] Memiliki Ruang Patung
* [ ] Memiliki Ruang Permata
* [ ] Memiliki brankas
* [ ] Memiliki 3 petunjuk
* [ ] Menggunakan variable untuk menyimpan keadaan petunjuk
* [ ] Petunjuk tidak dapat diperoleh berkali-kali
* [ ] Pemain tidak dapat membuka brankas sebelum menemukan semua petunjuk
* [ ] Brankas memiliki 3 kesempatan
* [ ] Memiliki kondisi menang
* [ ] Memiliki kondisi kalah
* [ ] Memiliki validasi pilihan
* [ ] Menggunakan `while`
* [ ] Menggunakan `for`
* [ ] Menggunakan `if / elif / else`
* [ ] Tidak menggunakan `list`
* [ ] Tidak menggunakan `function` buatan sendiri

---

# ⭐ Bonus Challenge

Setelah versi utama selesai, coba tambahkan fitur tambahan.

### Bonus 1 — Password

Sebelum membuka brankas, pemain harus memasukkan password.

Password dapat ditentukan sendiri.

Contoh:

```text
Masukkan password: diamond

Password benar!
```

---

### Bonus 2 — Nyawa

Tambahkan sistem nyawa.

Contoh:

```text
❤️ Nyawa: 3
```

Kesalahan tertentu dapat mengurangi nyawa pemain.

Jika nyawa habis, game berakhir.

---

### Bonus 3 — Batas Gerakan

Batasi jumlah pemain dapat berpindah atau melakukan aksi.

Misalnya pemain hanya memiliki:

```text
Langkah tersisa: 10
```

Setiap kali melakukan aksi tertentu, jumlah langkah berkurang.

Jika langkah habis, game berakhir.

---

### Bonus 4 — Cerita Tambahan

Tambahkan ruangan atau kejadian baru.

Contohnya:

* Ruang Keamanan
* Ruang Penyimpanan
* Penjaga museum
* Pintu rahasia
* Petunjuk palsu

Pastikan fitur tambahan tetap dibuat menggunakan materi Python yang sudah dipelajari.

---

# 🏆 Target Akhir

Ketika project selesai, pemain harus dapat memainkan game dari awal sampai akhir seperti berikut:

```text
Start
  ↓
Cerita
  ↓
Menu Museum
  ↓
Mencari petunjuk
  ↓
Petunjuk 1
  ↓
Petunjuk 2
  ↓
Petunjuk 3
  ↓
Membuka brankas
  ↓
Memasukkan kode
  ↓
Berhasil
  ↓
💎 BLUE DIAMOND
  ↓
YOU WIN!
```

**Selamat mencoba dan selamat membangun Museum Berlian! 💎**

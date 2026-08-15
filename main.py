print("Masukkan berat orang pertama:", end=" ")
orang1 = int(input())
print("Masukkan berat orang kedua:", end=" ")
orang2 = int(input())
print("Masukkan berat orang ketiga:", end=" ")
orang3 = int(input())
print("Masukkan berat orang keempat:", end=" ")
orang4 = int(input())
print("Masukkan berat orang kelima:", end=" ")
orang5 = int(input())
total_berat = orang1 + orang2 + orang3 + orang4 + orang5


if total_berat <= 400 and total_berat > 0:
    print("Lift dijalankan.")
    print(f"Total berat: {total_berat}")
elif total_berat > 400:
    print("Lift tidak bisa dijalankan.")
    print(f"Total berat: {total_berat}")







# Masukkan berat orang ke-1:
# Masukkan berat orang ke-2:
# Masukkan berat orang ke-3:
# Masukkan berat orang ke-4:
# Masukkan berat orang ke-5:

# Lift dapat dijalankan.
# atau
# Lift kelebihan beban.




print("Pilih menu:", end=" ")
menu = int(input())
print("Jumlah:", end=" ")
jumlah = int(input())
print("Memiliki member atau tidak?", end=" ")
member = input()
print("Apakah memiliki voucher?", end=" ")
vocer = input()


#pilih menu
if menu == 1:
    harga = 25000
elif menu == 2:
    harga = 35000
elif menu == 3:
    harga = 60000

diskon = 0
if member == "ya":
    diskon = 10

if total_harga > 100000:
    diskon = diskon + 5 


total_harga = harga * jumlah
harga_akhir = total_harga - (diskon/100 * total_harga)
diskon_harga = diskon/100 * total_harga 

if vocer == "ya":
    harga_akhir = harga_akhir - 40000
    diskon_harga = diskon_harga + 40000

if harga_akhir < 0:
    harga_akhir = 0


print(f"Subtotal: {int(total_harga)}")
print(f"Diskon: {int(diskon_harga)}")
print(f"Harga akhir: {int(harga_akhir)}")  

print("Pilih menu:", end=" ")
menu = int(input())
print("Jumlah:", end=" ")
jumlah = int(input())
print("Memiliki member atau tidak?", end=" ")
member = input()
print("Apakah memiliki voucher?", end=" ")
vocer = input()


#pilih menu
if menu == 1:
    harga1 = 25000
    total_harga = harga1 * jumlah
elif menu == 2:
    harga2 = 35000
    total_harga = harga2 * jumlah
elif menu == 3:
    harga3 = 60000
    total_harga = harga3 * jumlah

if member == "ya":
    diskon = 10
else:
    diskon = 0

if total_harga > 100000:
    diskon = diskon + 5 


harga_akhir = total_harga - (diskon/100 * total_harga)
diskon_harga = diskon/100 * total_harga 

if vocer == "ya":
    harga_akhir = harga_akhir - 40000
    diskon_harga = diskon_harga + 40000


print(f"Subtotal: {int(total_harga)}")
print(f"Diskon: {int(diskon_harga)}")
if harga_akhir < 0:
    print(f"Harga akhir: 0") 
else:
    print(f"Harga akhir: {int(harga_akhir)}")  




# hitung harga akhir sesuai diskon


# harga_akhir = harga - (diskon/100*harga)
# 100000 - (30/100 * 100000) = 70000


# menu * jumlah =
# 1 * 6 = 6
# 25000 * 6 = 150000
# total_harga?

# TODO: Kita bisa membeli beberapa kali

print("=== Mesin minuman ===")
print()
print("1. Kopi (Rp10.000)")
print("2. Teh  (Rp8.000)")
print("3. Susu (Rp12.000)")
print()
print("Pilih menu:", end=" ")
menu = int(input()) 
print("Masukkan uang:", end=" ")
uang = int(input()) 

if menu == 1 and uang >= 10000:
    print("Anda membeli kopi.")
    kembalian_kopi = uang - 10000
    if kembalian_kopi == 0:
        print("Uangnya pas, terima kasih!")
    else:
        print(f"Kembalian: Rp{kembalian_kopi}")
elif menu == 2 and uang >= 8000:
    print("Anda membeli Teh.")
    kembalian_teh = uang - 8000
    if uang == 8000:
        print("Uangnya pas, terima kasih!")
    else:
        print(f"Kembalian: Rp{kembalian_teh}")
elif menu == 3 and uang >= 12000:
    print("Anda membeli Susu.")
    kembalian_susu = uang - 12000
    if uang == 12000:
        print("Uangnya pas, terima kasih!")
    else:
        print(f"Kembalian: Rp{kembalian_susu}")
else:
    if menu >= 4:
        print("Menu tidak tersedia.")
    else:
        print("Uang tidak cukup.")









print("Masukkan umur:", end=" ")
umur = int(input())
tidak = "tidak"
ya = "ya"
print("Punya kartu anggota? (ya/tidak):", end=" ")
kartu_anggota = input()

if umur < 17 and kartu_anggota == tidak:
    print("Gerbang tertutup.")
    print("Alasan: belum cukup umur dan tidak memilki kartu anggota.")
elif umur >= 17 and kartu_anggota == ya:
    print("Gerbang terbuka.")
    print("Alasan: cukup umur dan memiliki kartu anggota.")
elif umur < 17 and kartu_anggota == ya:
    print("Gerbang tertutup.")
    print("Alasan: belum cukup umur.")
elif umur >= 17 and kartu_anggota == tidak:
    print("Gerbang tertutup.")
    print("Alasan: tidak memiliki kartu anggota.")



# Masukkan umur: 
# 20
# Punya kartu anggota? (ya/tidak): 
# tidak


print("Masukkan attack:", end=" ")
attack = int(input())
print("Masukkan defence:", end=" ")
defence = int(input())
print("Masukkan hp player:", end=" ")
hp = int(input())

#kondisi rank pemain s
if attack >= 80 and defence >= 70 and hp >= 120:
    print("Rank pemain = S")
elif attack >= 70 and defence >= 60 and hp >= 100:
    print("Rank pemain = A")
elif attack >= 60 and defence >= 50 and hp >= 80:
    print("Rank pemain = B")
else:
    print("Rank pemain = C")














# 📥 Input
# Masukkan Attack:
# Masukkan Defense:
# Masukkan HP:
# 📤 Output
# Rank pemain: A

print("Masukkan suhu:", end=" ")
suhu = int(input())
print("Masukkan Kelembapan:", end=" ")
kelembapan = int(input())
print("Masukkan kecepatan angin:", end=" ")
kecepatan = int(input())

if kecepatan >= 70 and kelembapan >= 85:
    print("Hujan badai")
elif kecepatan >= 70:
    print("Badai")
elif kelembapan >= 85:
    print("Hujan")
elif suhu >= 32:
    print("Cerah")
else:
    print("Berawan")







# 📝 Deskripsi

# Sebuah stasiun cuaca menggunakan tiga data:

# Suhu
# Kelembapan
# Kecepatan angin


# Aturan:
# Jika angin ≥ 70 km/jam → Badai
# Jika kelembapan ≥ 85 → Hujan
# Jika suhu ≥ 32°C → Cerah Panas
# Jika angin angin ≥ 70 km/jam dan kelembapan ≥ 85 maka → Hujan Badai
# Selain itu → Berawan


# Prioritas pengecekan mengikuti urutan di atas.

# 📥 Input
# Masukkan suhu (°C):
# Masukkan kelembapan (%):
# Masukkan kecepatan angin (km/jam):

# 📤 Output
# Prediksi cuaca: ...

# 💡 Contoh 1
# Input
# Suhu: 30
# Kelembapan: 90
# Kecepatan angin: 70
# Output
# Prediksi cuaca: Hujan Badai



# TODO: Bisa login masimal 3x
# TODO: Ada beberapa username dan password

print("Please log in again.")
print("====================")
print("Username:", end=" ")
username = input()   # andromeda
print("Password:", end=" ")
password = input()

#login berhasil
if username == "admin" and password == "python123":
    print("Login successfully.")

#login gagal karena password
elif username == "admin" and password != "python123":
    print("Login failed.")
    print("Reason: unknown password.")

#login gagal karena username
elif username != "admin" and password == "python123":
    print("Login failed.")
    print("Reason: unknown username.")

#login gagal karena tidak memenuhi kedua syaratnya 
elif username != "admin" and password != "python123":
    print("Login failed.")
    print("Reason: password and username unknown.")

# jika username dan password benar maka Login successfully jika tidak Login failed

# Login successfully.
# Login failed.

# Username: andromeda
# Password: python123


# TODO: Bagaimana jika bisa membeli senjata lebih dari satu

print("Senjata          Minimal level       Minimal gold")
print("===================================================")
print("Pedang kayu      1                   50 Gold")
print("Pedang besi      5                   150 Gold")
print("Pedang naga      10                  500 Gold")

print("Masukkan level pemain:", end=" ")
level = int(input())
print("Masukkan jumlah gold:", end=" ")
gold = int(input())


if level >= 1 and level < 5 and gold >= 50:
    print("Pedang terbaik yang dapat dibeli adalah pedang kayu.")
    kembalian_kayu = gold - 50
    print("Kamu membeli pedang kayu.")
    if kembalian_kayu > 0:
        print(f"Kembalian gold = {kembalian_kayu}")
    elif kembalian_kayu == 0:
        print("Kembalian goldnya pas.")
    
elif level >= 5 and level > 10 and gold >= 150:
    print("Pedang terbaik yang dapat dibeli adalah pedang besi.")
    kembalian_besi = gold - 150
    print("Kamu membeli pedang besi.")
    if kembalian_besi > 0:
        print(f"Kembalian gold = {kembalian_besi}")
    elif kembalian_besi == 0:
        print("Kembalian goldnya pas.")
        
elif level >= 10 and gold >= 500:
    print("Pedang terbaik yang dapat dibeli adalah pedang naga.")
    kembalian_naga = gold - 500
    print("Kamu membeli pedang naga.")
    if kembalian_naga > 0:
        print(f"Kembalian gold = {kembalian_naga}")
    elif kembalian_naga == 0:
        print("Kembalian goldnya pas.")

else:
    print("Anda tidak bisa membeli pedang")


# Anda tidak bisa membeli pedang

# Masukkan level pemain: -4
# Masukkan jumlah gold: 600




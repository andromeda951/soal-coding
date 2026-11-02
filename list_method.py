warna = ["merah", "hijau"]

# 1. append() - Menambah di akhir
warna.append("biru")
print(warna)  # Output: ['merah', 'hijau', 'biru']

# 2. insert() - Menambah di indeks ke-1
warna.insert(1, "kuning")
print(warna)  # Output: ['merah', 'kuning', 'hijau', 'biru']

# 3. extend() - Menggabungkan list
warna_tambahan = ["ungu", "jingga"]
warna.extend(warna_tambahan)
print(warna)  # Output: ['merah', 'kuning', 'hijau', 'biru', 'ungu', 'jingga']
print()
print()

angka_list = [10, 20, 30, 20, 40]

# 1. remove() - Berdasarkan nilai
angka_list.remove(30)
print(angka_list)  # Output: [10, 20, 20, 40]

# 2. pop() - Berdasarkan indeks (misal indeks ke-1)
dihapus = angka_list.pop(1)
print(dihapus)     # Output: 20 (elemen yang dihapus)
print(angka_list)  # Output: [10, 20, 40]

# 3. del statement - Hapus berdasarkan indeks ke-0
del angka_list[0]
print(angka_list)  # Output: [20, 40]

# 4. clear() - Mengosongkan list
angka_list.clear()
print(angka_list)  # Output: []
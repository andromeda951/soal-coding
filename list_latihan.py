# Simulasi Database menggunakan List
database_barang = ["Buku", "Pulpen", "Penghapus"]

# --- 1. CREATE (Menambah Data) ---
def tambah_barang(nama_barang):
    pass
    
# --- 2. READ (Membaca/Menampilkan Data) ---
def lihat_barang():
    pass
    
# --- 3. UPDATE (Memperbarui Data) ---
def update_barang(indeks, nama_baru):
    pass
    
# --- 4. DELETE (Menghapus Data) ---
def hapus_barang(indeks):
    pass

# ==========================================
# CONTOH MENJALANKAN OPERASI CRUD
# ==========================================

# 1. READ Awal
lihat_barang()

# 2. CREATE (Tambah "Penggaris")
tambah_barang("Penggaris")
lihat_barang()

# 3. UPDATE (Ubah "Pulpen" di indeks 1 menjadi "Spidol")
update_barang(1, "Spidol")
lihat_barang()

# 4. DELETE (Hapus data di indeks 0 yaitu "Buku")
hapus_barang(0)
lihat_barang()
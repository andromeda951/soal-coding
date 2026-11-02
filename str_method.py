teks = "halo dunia python"

print(teks.upper())       # Output: HALO DUNIA PYTHON
print("PYTHON".lower())   # Output: python
print(teks.capitalize())  # Output: Halo dunia python
print(teks.title())       # Output: Halo Dunia Python
print("PyThOn".swapcase()) # Output: pYtHoN


print("Python3".isalnum())   # Output: True
print("Python".isalpha())    # Output: True
print("12345".isdigit())     # Output: True
print("   ".isspace())       # Output: True
print("python".islower())    # Output: True
print("Halo Dunia".istitle()) # Output: True

pesan = "Selamat pagi"
print(pesan.startswith("Selamat")) # Output: True
print(pesan.endswith("pagi"))      # Output: True

kalimat = "belajar python itu menyenangkan"

print(kalimat.find("be"))   # Output: 8
print(kalimat.count("a"))       # Output: 3
print(kalimat.rfind("n"))       # Output: 24

kotor = "   halo python!   "
print(kotor.strip())        # Output: "halo python!"

teks = "aku suka apel"
print(teks.replace("apel", "mangga")) # Output: aku suka mangga

print("Python".center(10, "-"))       # Output: --Python--
print("42".zfill(5))                  # Output: 00042


# Split
buah = "apel,mangga,jeruk"
list_buah = buah.split(",")
print(list_buah)              # Output: ['apel', 'mangga', 'jeruk']

# Partition
print("python-lang".partition("-")) # Output: ('python', '-', 'lang')

# Join
pemisah = " - "
print(pemisah.join(list_buah)) # Output: apel - mangga - jeruk


teks_tab = "A\tB\tC"
print(teks_tab.expandtabs(3)) # Output: A   B   C



# A   B   C
# A       B       C
# A  B  C
# 1. Bikin function hitung luas persegi panjang tanpa parameter
def luas_persegi():
    p = int(input("masukan panjang: "))    
    l = int(input("masukan lebar: "))    
    luas = p*l
    print("luas = ", luas)
        
# 2. Bikin function hitung luas persegi panjang dengan parameter masukan
def luas_persegi2(p, l):
    luas = p*l
    print("luas =", luas)
    
    global x
    
    x = x + 10
    print(x)
    
    x = 6
    print(x)
    
    
x = 5 
# panjang = int(input("masukan panjang: "))    
# lebar = int(input("masukan lebar: "))   
# luas_persegi2(panjang, lebar)

# print("x=", x)

# luas_persegi2(10, 3)
    
# 3. Bikin function hitung luas persegi panjang dengan parameter masukan serta parameter  keluaran luas
# 4. Bikin function tambah 10 dari nilai a dan b dengan parameter masukan dan keluaran pada a dan b




def hitung_luas_r(p, l):
    return p*l

result = hitung_luas_r(5,3)
print("luas=", result)

print(hitung_luas_r(10,7))
    

def myabs(x):
    if x < 0:
        return -x
        
    return x

print(myabs(-7))
print(myabs(5))

    
    
    
    




# print("Awal")
# luas_persegi()  
# luas_persegi()  
# print("akhir")








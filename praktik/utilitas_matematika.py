def luas_persegi_panjang(p, l):
    return p * l
 
 
def luas_segitiga(a, t):
    return 0.5 * a * t
 
 
def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
 
 
def faktorial(n):
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil
 
 
def tampilkan_menu():
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")
 
 
def baca_n():
    """Membaca n dan mengembalikan None jika bukan bilangan bulat nonnegatif."""
    teks = input("n: ")
    try:
        n = int(teks)
    except ValueError:
        return None
    if n < 0:
        return None
    return n
 
 
def main():
    tampilkan_menu()
    pilihan = input("Pilihan: ")
 
    if pilihan == "1":
        p = float(input("Panjang: "))
        l = float(input("Lebar: "))
        print("Luas =", luas_persegi_panjang(p, l))
    elif pilihan == "2":
        a = float(input("Alas: "))
        t = float(input("Tinggi: "))
        print("Luas =", luas_segitiga(a, t))
    elif pilihan == "3":
        n = baca_n()
        if n is None:
            print("n harus bilangan bulat nonnegatif")
        else:
            print("Jumlah =", jumlah_n(n))
    elif pilihan == "4":
        n = baca_n()
        if n is None:
            print("n harus bilangan bulat nonnegatif")
        else:
            print("Faktorial =", faktorial(n))
    else:
        print("Pilihan tidak valid")
 
if __name__ == "__main__":
    main()
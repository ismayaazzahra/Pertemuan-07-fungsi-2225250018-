# Pertemuan 07 Fungsi Python

## Identitas
Nama: Ismaya Catur Dewi Azzahra
NIM: 2225250018
Kelas: 3A

## Tujuan

Tujuan dari tugas ini adalah mempelajari penggunaan fungsi, parameter, return value, dan scope variabel dalam Python, memecah program menjadi fungsi-fungsi yang memiliki satu tugas jelas, menguji setiap fungsi dengan test case, serta mengunggah hasil pengerjaan ke GitHub.

## Cara Menjalankan Program

Program dijalankan melalui VS Code menggunakan Python.

Langkah-langkah:

Buka folder pertemuan-07-fungsi-NIM di VS Code
Buka file praktik/utilitas_matematika.py
Jalankan program melalui terminal dengan perintah python3 praktik/utilitas_matematika.py (di Windows gunakan python)
Pilih menu 1 sampai 4, lalu masukkan input sesuai dengan yang diminta program
Periksa hasil program berdasarkan test case yang diberikan

## Struktur Fungsi

Fungsi	Parameter	Nilai return	Keterangan
luas_persegi_panjang(p, l)	p (panjang), l (lebar)	p * l	Menghitung luas persegi panjang.
luas_segitiga(a, t)	a (alas), t (tinggi)	0.5 * a * t	Menghitung luas segitiga.
jumlah_n(n)	n (bilangan bulat >= 0)	1 + 2 + ... + n	Akumulasi dengan for; n = 0 menghasilkan 0.
faktorial(n)	n (bilangan bulat >= 0)	n!	Perkalian dengan for dari 2 sampai n; 0! = 1.
tampilkan_menu()	tidak ada	tidak ada (None)	Hanya mencetak pilihan menu; sengaja memakai print.
baca_n()	tidak ada	n atau None	Membaca n; None jika bukan bilangan bulat nonnegatif.

## Hasil Pengujian

Operasi	Input	Diharapkan	Aktual	Status	Lewat menu
Luas persegi panjang	p=8, l=5	40	40	Lulus	40.0 *
Luas segitiga	a=10, t=6	30.0	30.0	Lulus	30.0
Jumlah 1..n	n=10	55	55	Lulus	55
Faktorial	n=5	120	120	Lulus	120
Faktorial	n=0	1	1	Lulus	1
Faktorial (validasi)	n=-3	Pesan galat	Pesan galat	Lulus	Pesan galat
Jumlah (validasi)	n=abc	Pesan galat	Pesan galat	Lulus	Pesan galat
Menu	pilihan 9	Tidak valid	Tidak valid	Lulus	Tidak valid

## Refleksi

Bagian program yang menjadi lebih sederhana setelah dipisah menjadi fungsi adalah perhitungan faktorial dan jumlah 1 sampai n. Sebelumnya, perulangan dan variabel penampung (hasil dan total) bercampur dengan kode input dan menu. Setelah dipisah, setiap fungsi hanya menerima n, menghitung, lalu mengembalikan nilai, sehingga bisa diuji langsung (faktorial(5) harus 120, faktorial(0) harus 1) tanpa menjalankan seluruh menu. Variabel hasil dan total juga menjadi lokal sehingga tidak mengganggu bagian program lain, dan perbaikan rumus cukup dilakukan di satu tempat.

Kesalahan yang saya perhatikan: 
hasil menu luas persegi panjang tampil 40.0, bukan 40, karena input dibaca sebagai float. Saya mengujinya dengan memanggil fungsi langsung memakai bilangan bulat, sehingga hasilnya 40 sesuai test case.
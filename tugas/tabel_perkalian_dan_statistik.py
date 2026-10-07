"""
Tugas - Tabel Perkalian dan Statistik
Pertemuan 06 Algoritma dan Pemrograman

Program:
1. Menerima input bilangan positif n.
2. Menampilkan tabel perkalian dari 1 sampai n.
3. Menghitung jumlah hasil perkalian pada setiap baris.
4. Menghitung total seluruh hasil perkalian.
5. Menghitung banyak hasil perkalian yang merupakan bilangan genap.
6. Menggunakan nested loop untuk proses perhitungan.
"""

print("=" * 70)
print("TUGAS - TABEL PERKALIAN DAN STATISTIK")
print("=" * 70)

# Meminta input n dan memastikan n merupakan bilangan positif.
while True:
    try:
        n = int(input("Masukkan nilai n (bilangan positif): "))

        if n > 0:
            break

        print("Input harus lebih besar dari 0.")

    except ValueError:
        print("Input harus berupa bilangan bulat.")

print("\n" + "=" * 70)
print(f"TABEL PERKALIAN 1 SAMPAI {n}")
print("=" * 70)

# Variabel untuk menyimpan total seluruh hasil perkalian.
total_semua = 0

# Variabel untuk menghitung banyak hasil perkalian yang genap.
jumlah_genap = 0

# Nested loop.
# Loop luar digunakan untuk menentukan baris.
for i in range(1, n + 1):

    # Akumulator untuk menghitung jumlah pada setiap baris.
    total_baris = 0

    print(f"\nBaris {i}:")

    # Loop dalam digunakan untuk menghitung perkalian
    # dari i dengan setiap nilai j.
    for j in range(1, n + 1):

        # Menghitung hasil perkalian.
        hasil = i * j

        # Menampilkan proses perkalian.
        print(f"{i} x {j} = {hasil}")

        # Menambahkan hasil ke jumlah baris.
        total_baris += hasil

        # Menambahkan hasil ke total keseluruhan.
        total_semua += hasil

        # Mengecek apakah hasil perkalian merupakan bilangan genap.
        if hasil % 2 == 0:
            jumlah_genap += 1

    # Menampilkan jumlah hasil perkalian pada baris tersebut.
    print(f"Jumlah baris {i} = {total_baris}")

print("\n" + "=" * 70)
print("STATISTIK HASIL PERHITUNGAN")
print("=" * 70)

# Menampilkan statistik akhir.
print(f"Nilai n                 = {n}")
print(f"Total seluruh hasil     = {total_semua}")
print(f"Jumlah bilangan genap   = {jumlah_genap}")

print("=" * 70)
print("Program selesai.")
print("=" * 70)
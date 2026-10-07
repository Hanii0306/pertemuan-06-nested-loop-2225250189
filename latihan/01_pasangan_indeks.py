"""
Latihan 1 - Pasangan Indeks
Pertemuan 06 Algoritma dan Pemrograman

Program menampilkan seluruh pasangan (i, j)
untuk i = 1 sampai 3 dan j = 1 sampai 4.
Program juga menghitung banyak pasangan yang dihasilkan.
"""

print("=" * 50)
print("LATIHAN 1 - PASANGAN INDEKS")
print("=" * 50)

count = 0

print("\nDaftar pasangan (i, j):")

for i in range(1, 4):
    for j in range(1, 5):
        print(f"({i}, {j})")
        count += 1

print("-" * 50)
print(f"Banyak pasangan = {count}")
print("=" * 50)
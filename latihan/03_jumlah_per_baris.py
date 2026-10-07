"""
Latihan 3 - Jumlah Per Baris
Pertemuan 06 Algoritma dan Pemrograman

Untuk i = 1 sampai 4 dan j = 1 sampai 3,
program menghitung nilai i * j dan menampilkan
jumlah hasil perkalian pada setiap baris.
"""

print("=" * 60)
print("LATIHAN 3 - JUMLAH PER BARIS")
print("=" * 60)

for i in range(1, 5):

    # Akumulator direset untuk setiap baris.
    total_baris = 0

    print(f"\nBaris {i}:")

    for j in range(1, 4):

        nilai = i * j

        print(f"{i} x {j} = {nilai}")

        total_baris += nilai

    print(f"Jumlah baris {i} = {total_baris}")

print("\n" + "=" * 60)
print("Program selesai.")
print("=" * 60)
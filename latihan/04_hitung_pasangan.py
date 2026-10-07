"""
Latihan 4 - Menghitung Pasangan
Pertemuan 06 Algoritma dan Pemrograman

Program menerima bilangan positif n.
Untuk i dan j dari 1 sampai n,
program menghitung banyak pasangan yang memenuhi:

i + j <= n
"""

print("=" * 60)
print("LATIHAN 4 - MENGHITUNG PASANGAN")
print("=" * 60)

while True:
    try:
        n = int(input("Masukkan nilai n (bilangan positif): "))

        if n > 0:
            break

        print("n harus lebih besar dari 0.")

    except ValueError:
        print("Input harus berupa bilangan bulat.")

count = 0

print("\nPasangan yang memenuhi i + j <= n:")
print("-" * 60)

for i in range(1, n + 1):
    for j in range(1, n + 1):

        if i + j <= n:
            print(f"({i}, {j})")
            count += 1

print("-" * 60)
print(f"Banyak pasangan = {count}")
print("=" * 60)
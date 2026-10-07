"""
Latihan 2 - Pola Segitiga
Pertemuan 06 Algoritma dan Pemrograman

Program menerima bilangan positif n dan membuat
pola segitiga menggunakan nested loop.

Baris pertama memiliki 1 simbol.
Baris kedua memiliki 2 simbol.
Baris ketiga memiliki 3 simbol.
Dan seterusnya sampai baris ke-n.
"""

print("=" * 50)
print("LATIHAN 2 - POLA SEGITIGA")
print("=" * 50)

while True:
    try:
        n = int(input("Masukkan nilai n (bilangan positif): "))

        if n > 0:
            break

        print("n harus lebih besar dari 0.")

    except ValueError:
        print("Input harus berupa bilangan bulat.")

print("\nPola segitiga:")
print("-" * 30)

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("-" * 30)
print(f"Jumlah baris = {n}")
print("Program selesai.")